
/*
    Routines for matrix products. Calling procedure:

    MatProductCreate(A,B,C,&D); or MatProductCreateWithMat(A,B,C,D)
    MatProductSetType(D, MATPRODUCT_AB/AtB/ABt/PtAP/RARt/ABC)
    MatProductSetAlgorithm(D, alg)
    MatProductSetFill(D,fill)
    MatProductSetFromOptions(D)
      -> MatProductSetFromOptions_Private(D)
           # Check matrix global sizes
           if the matrices have the same setfromoptions routine, use it
           if not, try:
             -> Query MatProductSetFromOptions_Atype_Btype_Ctype_C(D) from A, B and C (in order)
             if found -> run the specific setup that must set the symbolic operation (these callbacks should never fail)
           if callback not found or no symbolic operation set
             -> Query MatProductSetFromOptions_anytype_C(D) from A, B and C (in order) (e.g, matrices may have inner matrices like MATTRANSPOSEVIRTUAL)
           if dispatch found but combination still not present do
             -> check if B is dense and product type AtB or AB -> if true, basic looping of dense columns
             -> check if triple product (PtAP, RARt or ABC) -> if true, set the Basic routines

    #  The setfromoptions calls MatProductSetFromOptions_Atype_Btype_Ctype should
    #    Check matrix local sizes for mpi matrices
    #    Set default algorithm
    #    Get runtime option
    #    Set D->ops->productsymbolic = MatProductSymbolic_productype_Atype_Btype_Ctype if found

    MatProductSymbolic(D)
      # Call MatProductSymbolic_productype_Atype_Btype_Ctype()
        the callback must set the numeric phase D->ops->productnumeric = MatProductNumeric_productype_Atype_Btype_Ctype

    MatProductNumeric(D)
      # Call the numeric phase

    # The symbolic phases are allowed to set extra data structures and attach those to the product
    # this additional data can be reused between multiple numeric phases with the same matrices
    # if not needed, call
    MatProductClear(D)
*/

#include <petsc/private/matimpl.h> /*I "petscmat.h" I*/

const char *const MatProductTypes[] = {"UNSPECIFIED", "AB", "AtB", "ABt", "PtAP", "RARt", "ABC"};

/* these are basic implementations relying on the old function pointers
 * they are dangerous and should be removed in the future */
static PetscErrorCode MatProductNumeric_PtAP_Unsafe(Mat C)
{
  Mat_Product *product = C->product;
  Mat          P = product->B, AP = product->Dwork;

  PetscFunctionBegin;
  /* AP = A*P */
  PetscCall(MatProductNumeric(AP));
  /* C = P^T*AP */
  PetscCall((*C->ops->transposematmultnumeric)(P, AP, C));
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductSymbolic_PtAP_Unsafe(Mat C)
{
  Mat_Product *product = C->product;
  Mat          A = product->A, P = product->B, AP;
  PetscReal    fill = product->fill;

  PetscFunctionBegin;
  PetscCall(PetscInfo((PetscObject)C, "for A %s, P %s is used\n", ((PetscObject)product->A)->type_name, ((PetscObject)product->B)->type_name));
  /* AP = A*P */
  PetscCall(MatProductCreate(A, P, NULL, &AP));
  PetscCall(MatProductSetType(AP, MATPRODUCT_AB));
  PetscCall(MatProductSetAlgorithm(AP, MATPRODUCTALGORITHMDEFAULT));
  PetscCall(MatProductSetFill(AP, fill));
  PetscCall(MatProductSetFromOptions(AP));
  PetscCall(MatProductSymbolic(AP));

  /* C = P^T*AP */
  PetscCall(MatProductSetType(C, MATPRODUCT_AtB));
  PetscCall(MatProductSetAlgorithm(C, MATPRODUCTALGORITHMDEFAULT));
  product->A = P;
  product->B = AP;
  PetscCall(MatProductSetFromOptions(C));
  PetscCall(MatProductSymbolic(C));

  /* resume user's original input matrix setting for A and B */
  product->A     = A;
  product->B     = P;
  product->Dwork = AP;

  C->ops->productnumeric = MatProductNumeric_PtAP_Unsafe;
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductNumeric_RARt_Unsafe(Mat C)
{
  Mat_Product *product = C->product;
  Mat          R = product->B, RA = product->Dwork;

  PetscFunctionBegin;
  /* RA = R*A */
  PetscCall(MatProductNumeric(RA));
  /* C = RA*R^T */
  PetscCall((*C->ops->mattransposemultnumeric)(RA, R, C));
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductSymbolic_RARt_Unsafe(Mat C)
{
  Mat_Product *product = C->product;
  Mat          A = product->A, R = product->B, RA;
  PetscReal    fill = product->fill;

  PetscFunctionBegin;
  PetscCall(PetscInfo((PetscObject)C, "for A %s, R %s is used\n", ((PetscObject)product->A)->type_name, ((PetscObject)product->B)->type_name));
  /* RA = R*A */
  PetscCall(MatProductCreate(R, A, NULL, &RA));
  PetscCall(MatProductSetType(RA, MATPRODUCT_AB));
  PetscCall(MatProductSetAlgorithm(RA, MATPRODUCTALGORITHMDEFAULT));
  PetscCall(MatProductSetFill(RA, fill));
  PetscCall(MatProductSetFromOptions(RA));
  PetscCall(MatProductSymbolic(RA));

  /* C = RA*R^T */
  PetscCall(MatProductSetType(C, MATPRODUCT_ABt));
  PetscCall(MatProductSetAlgorithm(C, MATPRODUCTALGORITHMDEFAULT));
  product->A = RA;
  PetscCall(MatProductSetFromOptions(C));
  PetscCall(MatProductSymbolic(C));

  /* resume user's original input matrix setting for A */
  product->A             = A;
  product->Dwork         = RA; /* save here so it will be destroyed with product C */
  C->ops->productnumeric = MatProductNumeric_RARt_Unsafe;
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductNumeric_ABC_Unsafe(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, BC = product->Dwork;

  PetscFunctionBegin;
  /* Numeric BC = B*C */
  PetscCall(MatProductNumeric(BC));
  /* Numeric mat = A*BC */
  PetscCall((*mat->ops->matmultnumeric)(A, BC, mat));
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductSymbolic_ABC_Unsafe(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          B = product->B, C = product->C, BC;
  PetscReal    fill = product->fill;

  PetscFunctionBegin;
  PetscCall(PetscInfo((PetscObject)mat, "for A %s, B %s, C %s is used\n", ((PetscObject)product->A)->type_name, ((PetscObject)product->B)->type_name, ((PetscObject)product->C)->type_name));
  /* Symbolic BC = B*C */
  PetscCall(MatProductCreate(B, C, NULL, &BC));
  PetscCall(MatProductSetType(BC, MATPRODUCT_AB));
  PetscCall(MatProductSetAlgorithm(BC, MATPRODUCTALGORITHMDEFAULT));
  PetscCall(MatProductSetFill(BC, fill));
  PetscCall(MatProductSetFromOptions(BC));
  PetscCall(MatProductSymbolic(BC));

  /* Symbolic mat = A*BC */
  PetscCall(MatProductSetType(mat, MATPRODUCT_AB));
  PetscCall(MatProductSetAlgorithm(mat, MATPRODUCTALGORITHMDEFAULT));
  product->B     = BC;
  product->Dwork = BC;
  PetscCall(MatProductSetFromOptions(mat));
  PetscCall(MatProductSymbolic(mat));

  /* resume user's original input matrix setting for B */
  product->B               = B;
  mat->ops->productnumeric = MatProductNumeric_ABC_Unsafe;
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductSymbolic_Unsafe(Mat mat)
{
  Mat_Product *product = mat->product;

  PetscFunctionBegin;
  switch (product->type) {
  case MATPRODUCT_PtAP:
    PetscCall(MatProductSymbolic_PtAP_Unsafe(mat));
    break;
  case MATPRODUCT_RARt:
    PetscCall(MatProductSymbolic_RARt_Unsafe(mat));
    break;
  case MATPRODUCT_ABC:
    PetscCall(MatProductSymbolic_ABC_Unsafe(mat));
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)mat), PETSC_ERR_SUP, "ProductType %s is not supported", MatProductTypes[product->type]);
  }
  PetscFunctionReturn(0);
}

/* ----------------------------------------------- */
/*@C
   MatProductReplaceMats - Replace input matrices for a matrix product.

   Collective on Mat

   Input Parameters:
+  A - the matrix or NULL if not being replaced
.  B - the matrix or NULL if not being replaced
.  C - the matrix or NULL if not being replaced
-  D - the matrix product

   Level: intermediate

   Note:
     To reuse the symbolic phase, the input matrices must have exactly the same data structure as the replaced one.
     If the type of any of the input matrices is different than what was previously used, or their symmetry flag changed but
     the symbolic phase took advantage of their symmetry, the product is cleared and `MatProductSetFromOptions()` and `MatProductSymbolic()` are invoked again.

.seealso: `MatProductCreate()`, `MatProductSetFromOptions()`, `MatProductSymbolic().` `MatProductClear()`
@*/
PetscErrorCode MatProductReplaceMats(Mat A, Mat B, Mat C, Mat D)
{
  Mat_Product *product;
  PetscBool    flgA = PETSC_TRUE, flgB = PETSC_TRUE, flgC = PETSC_TRUE, isset, issym;

  PetscFunctionBegin;
  PetscValidHeaderSpecific(D, MAT_CLASSID, 4);
  MatCheckProduct(D, 4);
  product = D->product;
  if (A) {
    PetscValidHeaderSpecific(A, MAT_CLASSID, 1);
    PetscCall(PetscObjectReference((PetscObject)A));
    PetscCall(PetscObjectTypeCompare((PetscObject)product->A, ((PetscObject)A)->type_name, &flgA));
    PetscCall(MatIsSymmetricKnown(A, &isset, &issym));
    if (product->symbolic_used_the_fact_A_is_symmetric && isset && !issym) { /* symbolic was built around a symmetric A, but the new A is not anymore */
      flgA                                           = PETSC_FALSE;
      product->symbolic_used_the_fact_A_is_symmetric = PETSC_FALSE; /* reinit */
    }
    PetscCall(MatDestroy(&product->A));
    product->A = A;
  }
  if (B) {
    PetscValidHeaderSpecific(B, MAT_CLASSID, 2);
    PetscCall(PetscObjectReference((PetscObject)B));
    PetscCall(PetscObjectTypeCompare((PetscObject)product->B, ((PetscObject)B)->type_name, &flgB));
    PetscCall(MatIsSymmetricKnown(B, &isset, &issym));
    if (product->symbolic_used_the_fact_B_is_symmetric && isset && !issym) {
      flgB                                           = PETSC_FALSE;
      product->symbolic_used_the_fact_B_is_symmetric = PETSC_FALSE; /* reinit */
    }
    PetscCall(MatDestroy(&product->B));
    product->B = B;
  }
  if (C) {
    PetscValidHeaderSpecific(C, MAT_CLASSID, 3);
    PetscCall(PetscObjectReference((PetscObject)C));
    PetscCall(PetscObjectTypeCompare((PetscObject)product->C, ((PetscObject)C)->type_name, &flgC));
    PetscCall(MatIsSymmetricKnown(C, &isset, &issym));
    if (product->symbolic_used_the_fact_C_is_symmetric && isset && !issym) {
      flgC                                           = PETSC_FALSE;
      product->symbolic_used_the_fact_C_is_symmetric = PETSC_FALSE; /* reinit */
    }
    PetscCall(MatDestroy(&product->C));
    product->C = C;
  }
  /* Any of the replaced mats is of a different type, reset */
  if (!flgA || !flgB || !flgC) {
    if (D->product->destroy) PetscCall((*D->product->destroy)(D->product->data));
    D->product->destroy = NULL;
    D->product->data    = NULL;
    if (D->ops->productnumeric || D->ops->productsymbolic) {
      PetscCall(MatProductSetFromOptions(D));
      PetscCall(MatProductSymbolic(D));
    }
  }
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductNumeric_X_Dense(Mat C)
{
  Mat_Product *product = C->product;
  Mat          A = product->A, B = product->B;
  PetscInt     k, K              = B->cmap->N;
  PetscBool    t = PETSC_TRUE, iscuda = PETSC_FALSE;
  PetscBool    Bcpu = PETSC_TRUE, Ccpu = PETSC_TRUE;
  char        *Btype = NULL, *Ctype = NULL;

  PetscFunctionBegin;
  switch (product->type) {
  case MATPRODUCT_AB:
    t = PETSC_FALSE;
  case MATPRODUCT_AtB:
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)C), PETSC_ERR_SUP, "MatProductNumeric type %s not supported for %s and %s matrices", MatProductTypes[product->type], ((PetscObject)A)->type_name, ((PetscObject)B)->type_name);
  }
  if (PetscDefined(HAVE_CUDA)) {
    VecType vtype;

    PetscCall(MatGetVecType(A, &vtype));
    PetscCall(PetscStrcmp(vtype, VECCUDA, &iscuda));
    if (!iscuda) PetscCall(PetscStrcmp(vtype, VECSEQCUDA, &iscuda));
    if (!iscuda) PetscCall(PetscStrcmp(vtype, VECMPICUDA, &iscuda));
    if (iscuda) { /* Make sure we have up-to-date data on the GPU */
      PetscCall(PetscStrallocpy(((PetscObject)B)->type_name, &Btype));
      PetscCall(PetscStrallocpy(((PetscObject)C)->type_name, &Ctype));
      PetscCall(MatConvert(B, MATDENSECUDA, MAT_INPLACE_MATRIX, &B));
      if (!C->assembled) { /* need to flag the matrix as assembled, otherwise MatConvert will complain */
        PetscCall(MatAssemblyBegin(C, MAT_FINAL_ASSEMBLY));
        PetscCall(MatAssemblyEnd(C, MAT_FINAL_ASSEMBLY));
      }
      PetscCall(MatConvert(C, MATDENSECUDA, MAT_INPLACE_MATRIX, &C));
    } else { /* Make sure we have up-to-date data on the CPU */
#if defined(PETSC_HAVE_CUDA) || defined(PETSC_HAVE_VIENNACL)
      Bcpu = B->boundtocpu;
      Ccpu = C->boundtocpu;
#endif
      PetscCall(MatBindToCPU(B, PETSC_TRUE));
      PetscCall(MatBindToCPU(C, PETSC_TRUE));
    }
  }
  for (k = 0; k < K; k++) {
    Vec x, y;

    PetscCall(MatDenseGetColumnVecRead(B, k, &x));
    PetscCall(MatDenseGetColumnVecWrite(C, k, &y));
    if (t) {
      PetscCall(MatMultTranspose(A, x, y));
    } else {
      PetscCall(MatMult(A, x, y));
    }
    PetscCall(MatDenseRestoreColumnVecRead(B, k, &x));
    PetscCall(MatDenseRestoreColumnVecWrite(C, k, &y));
  }
  PetscCall(MatAssemblyBegin(C, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(C, MAT_FINAL_ASSEMBLY));
  if (PetscDefined(HAVE_CUDA)) {
    if (iscuda) {
      PetscCall(MatConvert(B, Btype, MAT_INPLACE_MATRIX, &B));
      PetscCall(MatConvert(C, Ctype, MAT_INPLACE_MATRIX, &C));
    } else {
      PetscCall(MatBindToCPU(B, Bcpu));
      PetscCall(MatBindToCPU(C, Ccpu));
    }
  }
  PetscCall(PetscFree(Btype));
  PetscCall(PetscFree(Ctype));
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductSymbolic_X_Dense(Mat C)
{
  Mat_Product *product = C->product;
  Mat          A = product->A, B = product->B;
  PetscBool    isdense;

  PetscFunctionBegin;
  switch (product->type) {
  case MATPRODUCT_AB:
    PetscCall(MatSetSizes(C, A->rmap->n, B->cmap->n, A->rmap->N, B->cmap->N));
    break;
  case MATPRODUCT_AtB:
    PetscCall(MatSetSizes(C, A->cmap->n, B->cmap->n, A->cmap->N, B->cmap->N));
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)C), PETSC_ERR_SUP, "MatProductSymbolic type %s not supported for %s and %s matrices", MatProductTypes[product->type], ((PetscObject)A)->type_name, ((PetscObject)B)->type_name);
  }
  PetscCall(PetscObjectBaseTypeCompareAny((PetscObject)C, &isdense, MATSEQDENSE, MATMPIDENSE, ""));
  if (!isdense) {
    PetscCall(MatSetType(C, ((PetscObject)B)->type_name));
    /* If matrix type of C was not set or not dense, we need to reset the pointer */
    C->ops->productsymbolic = MatProductSymbolic_X_Dense;
  }
  C->ops->productnumeric = MatProductNumeric_X_Dense;
  PetscCall(MatSetUp(C));
  PetscFunctionReturn(0);
}

/* a single driver to query the dispatching */
static PetscErrorCode MatProductSetFromOptions_Private(Mat mat)
{
  Mat_Product      *product = mat->product;
  PetscInt          Am, An, Bm, Bn, Cm, Cn;
  Mat               A = product->A, B = product->B, C = product->C;
  const char *const Bnames[] = {"B", "R", "P"};
  const char       *bname;
  PetscErrorCode (*fA)(Mat);
  PetscErrorCode (*fB)(Mat);
  PetscErrorCode (*fC)(Mat);
  PetscErrorCode (*f)(Mat) = NULL;

  PetscFunctionBegin;
  mat->ops->productsymbolic = NULL;
  mat->ops->productnumeric  = NULL;
  if (product->type == MATPRODUCT_UNSPECIFIED) PetscFunctionReturn(0);
  PetscCheck(A, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Missing A mat");
  PetscCheck(B, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Missing B mat");
  PetscCheck(product->type != MATPRODUCT_ABC || C, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Missing C mat");
  if (product->type != MATPRODUCT_ABC) C = NULL; /* do not use C if not needed */
  if (product->type == MATPRODUCT_RARt) bname = Bnames[1];
  else if (product->type == MATPRODUCT_PtAP) bname = Bnames[2];
  else bname = Bnames[0];

  /* Check matrices sizes */
  Am = A->rmap->N;
  An = A->cmap->N;
  Bm = B->rmap->N;
  Bn = B->cmap->N;
  Cm = C ? C->rmap->N : 0;
  Cn = C ? C->cmap->N : 0;
  if (product->type == MATPRODUCT_RARt || product->type == MATPRODUCT_ABt) {
    PetscInt t = Bn;
    Bn         = Bm;
    Bm         = t;
  }
  if (product->type == MATPRODUCT_AtB) {
    PetscInt t = An;
    An         = Am;
    Am         = t;
  }
  PetscCheck(An == Bm, PetscObjectComm((PetscObject)mat), PETSC_ERR_ARG_SIZ, "Matrix dimensions of A and %s are incompatible for MatProductType %s: A %" PetscInt_FMT "x%" PetscInt_FMT ", %s %" PetscInt_FMT "x%" PetscInt_FMT, bname,
             MatProductTypes[product->type], A->rmap->N, A->cmap->N, bname, B->rmap->N, B->cmap->N);
  PetscCheck(!Cm || Cm == Bn, PetscObjectComm((PetscObject)mat), PETSC_ERR_ARG_SIZ, "Matrix dimensions of B and C are incompatible for MatProductType %s: B %" PetscInt_FMT "x%" PetscInt_FMT ", C %" PetscInt_FMT "x%" PetscInt_FMT,
             MatProductTypes[product->type], B->rmap->N, B->cmap->N, Cm, Cn);

  fA = A->ops->productsetfromoptions;
  fB = B->ops->productsetfromoptions;
  fC = C ? C->ops->productsetfromoptions : fA;
  if (C) {
    PetscCall(PetscInfo(mat, "MatProductType %s for A %s, %s %s, C %s\n", MatProductTypes[product->type], ((PetscObject)A)->type_name, bname, ((PetscObject)B)->type_name, ((PetscObject)C)->type_name));
  } else {
    PetscCall(PetscInfo(mat, "MatProductType %s for A %s, %s %s\n", MatProductTypes[product->type], ((PetscObject)A)->type_name, bname, ((PetscObject)B)->type_name));
  }
  if (fA == fB && fA == fC && fA) {
    PetscCall(PetscInfo(mat, "  matching op\n"));
    PetscCall((*fA)(mat));
  }
  /* We may have found f but it did not succeed */
  if (!mat->ops->productsymbolic) { /* query MatProductSetFromOptions_Atype_Btype_Ctype */
    char mtypes[256];
    PetscCall(PetscStrncpy(mtypes, "MatProductSetFromOptions_", sizeof(mtypes)));
    PetscCall(PetscStrlcat(mtypes, ((PetscObject)A)->type_name, sizeof(mtypes)));
    PetscCall(PetscStrlcat(mtypes, "_", sizeof(mtypes)));
    PetscCall(PetscStrlcat(mtypes, ((PetscObject)B)->type_name, sizeof(mtypes)));
    if (C) {
      PetscCall(PetscStrlcat(mtypes, "_", sizeof(mtypes)));
      PetscCall(PetscStrlcat(mtypes, ((PetscObject)C)->type_name, sizeof(mtypes)));
    }
    PetscCall(PetscStrlcat(mtypes, "_C", sizeof(mtypes)));

    PetscCall(PetscObjectQueryFunction((PetscObject)A, mtypes, &f));
    PetscCall(PetscInfo(mat, "  querying %s from A? %p\n", mtypes, f));
    if (!f) {
      PetscCall(PetscObjectQueryFunction((PetscObject)B, mtypes, &f));
      PetscCall(PetscInfo(mat, "  querying %s from %s? %p\n", mtypes, bname, f));
    }
    if (!f && C) {
      PetscCall(PetscObjectQueryFunction((PetscObject)C, mtypes, &f));
      PetscCall(PetscInfo(mat, "  querying %s from C? %p\n", mtypes, f));
    }
    if (f) PetscCall((*f)(mat));

    /* We may have found f but it did not succeed */
    /* some matrices (i.e. MATTRANSPOSEVIRTUAL, MATSHELL constructed from MatConvert), knows what to do with their inner matrices */
    if (!mat->ops->productsymbolic) {
      PetscCall(PetscStrncpy(mtypes, "MatProductSetFromOptions_anytype_C", sizeof(mtypes)));
      PetscCall(PetscObjectQueryFunction((PetscObject)A, mtypes, &f));
      PetscCall(PetscInfo(mat, "  querying %s from A? %p\n", mtypes, f));
      if (!f) {
        PetscCall(PetscObjectQueryFunction((PetscObject)B, mtypes, &f));
        PetscCall(PetscInfo(mat, "  querying %s from %s? %p\n", mtypes, bname, f));
      }
      if (!f && C) {
        PetscCall(PetscObjectQueryFunction((PetscObject)C, mtypes, &f));
        PetscCall(PetscInfo(mat, "  querying %s from C? %p\n", mtypes, f));
      }
    }
    if (f) PetscCall((*f)(mat));
  }

  /* We may have found f but it did not succeed */
  if (!mat->ops->productsymbolic) {
    /* we can still compute the product if B is of type dense */
    if (product->type == MATPRODUCT_AB || product->type == MATPRODUCT_AtB) {
      PetscBool isdense;

      PetscCall(PetscObjectBaseTypeCompareAny((PetscObject)B, &isdense, MATSEQDENSE, MATMPIDENSE, ""));
      if (isdense) {
        mat->ops->productsymbolic = MatProductSymbolic_X_Dense;
        PetscCall(PetscInfo(mat, "  using basic looping over columns of a dense matrix\n"));
      }
    } else if (product->type != MATPRODUCT_ABt) { /* use MatProductSymbolic/Numeric_Unsafe() for triple products only */
      /*
         TODO: this should be changed to a proper setfromoptions, not setting the symbolic pointer here, because we do not know if
               the combination will succeed. In order to be sure, we need MatProductGetProductType to return the type of the result
               before computing the symbolic phase
      */
      PetscCall(PetscInfo(mat, "  symbolic product not supported, using MatProductSymbolic_Unsafe() implementation\n"));
      mat->ops->productsymbolic = MatProductSymbolic_Unsafe;
    }
  }
  if (!mat->ops->productsymbolic) PetscCall(PetscInfo(mat, "  symbolic product is not supported\n"));
  PetscFunctionReturn(0);
}

/*@C
   MatProductSetFromOptions - Sets the options for the computation of a matrix-matrix product where the type, the algorithm etc are determined from the options database.

   Logically Collective on Mat

   Input Parameter:
.  mat - the matrix

   Options Database Keys:
.    -mat_product_clear - Clear intermediate data structures after `MatProductNumeric()` has been called

   Level: intermediate

.seealso: `MatSetFromOptions()`, `MatProductCreate()`, `MatProductCreateWithMat()`, `MatProductNumeric()`, `MatProductSetType()`, `MatProductSetAlgorithm()`
@*/
PetscErrorCode MatProductSetFromOptions(Mat mat)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  MatCheckProduct(mat, 1);
  PetscCheck(!mat->product->data, PetscObjectComm((PetscObject)mat), PETSC_ERR_ORDER, "Cannot call MatProductSetFromOptions with already present data");
  PetscObjectOptionsBegin((PetscObject)mat);
  PetscCall(PetscOptionsBool("-mat_product_clear", "Clear intermediate data structures after MatProductNumeric() has been called", "MatProductClear", mat->product->clear, &mat->product->clear, NULL));
  PetscCall(PetscOptionsDeprecated("-mat_freeintermediatedatastructures", "-mat_product_clear", "3.13", "Or call MatProductClear() after MatProductNumeric()"));
  PetscOptionsEnd();
  PetscCall(MatProductSetFromOptions_Private(mat));
  PetscCheck(mat->product, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Missing product after setup phase");
  PetscFunctionReturn(0);
}

/*@C
   MatProductView - View the private `Mat_Product` algorithm object within a matrix

   Logically Collective on mat

   Input Parameter:
.  mat - the matrix obtained with `MatProductCreate()` or `MatProductCreateWithMat()`

   Level: intermediate

.seealso: `MatProductSetFromOptions()`, `MatView()`, `MatProductCreate()`, `MatProductCreateWithMat()`
@*/
PetscErrorCode MatProductView(Mat mat, PetscViewer viewer)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  if (!mat->product) PetscFunctionReturn(0);
  if (!viewer) PetscCall(PetscViewerASCIIGetStdout(PetscObjectComm((PetscObject)mat), &viewer));
  PetscValidHeaderSpecific(viewer, PETSC_VIEWER_CLASSID, 2);
  PetscCheckSameComm(mat, 1, viewer, 2);
  if (mat->product->view) PetscCall((*mat->product->view)(mat, viewer));
  PetscFunctionReturn(0);
}

/* ----------------------------------------------- */
/* these are basic implementations relying on the old function pointers
 * they are dangerous and should be removed in the future */
PetscErrorCode MatProductNumeric_AB(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->matmultnumeric)(A, B, mat));
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductNumeric_AtB(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->transposematmultnumeric)(A, B, mat));
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductNumeric_ABt(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->mattransposemultnumeric)(A, B, mat));
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductNumeric_PtAP(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->ptapnumeric)(A, B, mat));
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductNumeric_RARt(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->rartnumeric)(A, B, mat));
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductNumeric_ABC(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B, C = product->C;

  PetscFunctionBegin;
  PetscCall((*mat->ops->matmatmultnumeric)(A, B, C, mat));
  PetscFunctionReturn(0);
}

/* ----------------------------------------------- */

/*@
   MatProductNumeric - Compute a matrix product with numerical values.

   Collective on mat

   Input/Output Parameter:
.  mat - the matrix holding the product

   Level: intermediate

   Note:
   `MatProductSymbolic()` must have been called on mat before calling this function

.seealso: `MatProductSetAlgorithm()`, `MatProductSetType()`, `MatProductCreate()`, `MatSetType()`, `MatProductSymbolic()`
@*/
PetscErrorCode MatProductNumeric(Mat mat)
{
  PetscLogEvent eventtype = -1;
  PetscBool     missing   = PETSC_FALSE;

  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  MatCheckProduct(mat, 1);
  switch (mat->product->type) {
  case MATPRODUCT_AB:
    eventtype = MAT_MatMultNumeric;
    break;
  case MATPRODUCT_AtB:
    eventtype = MAT_TransposeMatMultNumeric;
    break;
  case MATPRODUCT_ABt:
    eventtype = MAT_MatTransposeMultNumeric;
    break;
  case MATPRODUCT_PtAP:
    eventtype = MAT_PtAPNumeric;
    break;
  case MATPRODUCT_RARt:
    eventtype = MAT_RARtNumeric;
    break;
  case MATPRODUCT_ABC:
    eventtype = MAT_MatMatMultNumeric;
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)mat), PETSC_ERR_SUP, "ProductType %s is not supported", MatProductTypes[mat->product->type]);
  }

  if (mat->ops->productnumeric) {
    PetscCall(PetscLogEventBegin(eventtype, mat, 0, 0, 0));
    PetscUseTypeMethod(mat, productnumeric);
    PetscCall(PetscLogEventEnd(eventtype, mat, 0, 0, 0));
  } else missing = PETSC_TRUE;

  if (missing || !mat->product) {
    char errstr[256];

    if (mat->product->type == MATPRODUCT_ABC) {
      PetscCall(PetscSNPrintf(errstr, 256, "%s with A %s, B %s, C %s", MatProductTypes[mat->product->type], ((PetscObject)mat->product->A)->type_name, ((PetscObject)mat->product->B)->type_name, ((PetscObject)mat->product->C)->type_name));
    } else {
      PetscCall(PetscSNPrintf(errstr, 256, "%s with A %s, B %s", MatProductTypes[mat->product->type], ((PetscObject)mat->product->A)->type_name, ((PetscObject)mat->product->B)->type_name));
    }
    PetscCheck(!missing, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Unspecified numeric phase for product %s", errstr);
    PetscCheck(mat->product, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Missing struct after symbolic phase for product %s", errstr);
  }

  if (mat->product->clear) PetscCall(MatProductClear(mat));
  PetscCall(PetscObjectStateIncrease((PetscObject)mat));
  PetscFunctionReturn(0);
}

/* ----------------------------------------------- */
/* these are basic implementations relying on the old function pointers
 * they are dangerous and should be removed in the future */
PetscErrorCode MatProductSymbolic_AB(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->matmultsymbolic)(A, B, product->fill, mat));
  mat->ops->productnumeric = MatProductNumeric_AB;
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductSymbolic_AtB(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->transposematmultsymbolic)(A, B, product->fill, mat));
  mat->ops->productnumeric = MatProductNumeric_AtB;
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductSymbolic_ABt(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B;

  PetscFunctionBegin;
  PetscCall((*mat->ops->mattransposemultsymbolic)(A, B, product->fill, mat));
  mat->ops->productnumeric = MatProductNumeric_ABt;
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductSymbolic_ABC(Mat mat)
{
  Mat_Product *product = mat->product;
  Mat          A = product->A, B = product->B, C = product->C;

  PetscFunctionBegin;
  PetscCall((*mat->ops->matmatmultsymbolic)(A, B, C, product->fill, mat));
  mat->ops->productnumeric = MatProductNumeric_ABC;
  PetscFunctionReturn(0);
}

/* ----------------------------------------------- */

/*@
   MatProductSymbolic - Perform the symbolic portion of a matrix product, this creates a data structure for use with the numerical product done with
  `MatProductNumeric()`

   Collective on mat

   Input/Output Parameter:
.  mat - the matrix to hold a product

   Level: intermediate

   Note:
   `MatProductSetFromOptions()` must have been called on mat before calling this function

.seealso: `MatProductCreate()`, `MatProductCreateWithMat()`, `MatProductSetFromOptions()`, `MatProductNumeric()`, `MatProductSetType()`, `MatProductSetAlgorithm()`
@*/
PetscErrorCode MatProductSymbolic(Mat mat)
{
  PetscLogEvent eventtype = -1;
  PetscBool     missing   = PETSC_FALSE;

  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  MatCheckProduct(mat, 1);
  PetscCheck(!mat->product->data, PetscObjectComm((PetscObject)mat), PETSC_ERR_ORDER, "Cannot run symbolic phase. Product data not empty");
  switch (mat->product->type) {
  case MATPRODUCT_AB:
    eventtype = MAT_MatMultSymbolic;
    break;
  case MATPRODUCT_AtB:
    eventtype = MAT_TransposeMatMultSymbolic;
    break;
  case MATPRODUCT_ABt:
    eventtype = MAT_MatTransposeMultSymbolic;
    break;
  case MATPRODUCT_PtAP:
    eventtype = MAT_PtAPSymbolic;
    break;
  case MATPRODUCT_RARt:
    eventtype = MAT_RARtSymbolic;
    break;
  case MATPRODUCT_ABC:
    eventtype = MAT_MatMatMultSymbolic;
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)mat), PETSC_ERR_SUP, "ProductType %s is not supported", MatProductTypes[mat->product->type]);
  }
  mat->ops->productnumeric = NULL;
  if (mat->ops->productsymbolic) {
    PetscCall(PetscLogEventBegin(eventtype, mat, 0, 0, 0));
    PetscUseTypeMethod(mat, productsymbolic);
    PetscCall(PetscLogEventEnd(eventtype, mat, 0, 0, 0));
  } else missing = PETSC_TRUE;

  if (missing || !mat->product || !mat->ops->productnumeric) {
    char errstr[256];

    if (mat->product->type == MATPRODUCT_ABC) {
      PetscCall(PetscSNPrintf(errstr, 256, "%s with A %s, B %s, C %s", MatProductTypes[mat->product->type], ((PetscObject)mat->product->A)->type_name, ((PetscObject)mat->product->B)->type_name, ((PetscObject)mat->product->C)->type_name));
    } else {
      PetscCall(PetscSNPrintf(errstr, 256, "%s with A %s, B %s", MatProductTypes[mat->product->type], ((PetscObject)mat->product->A)->type_name, ((PetscObject)mat->product->B)->type_name));
    }
    PetscCheck(!missing, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Unspecified symbolic phase for product %s. Call MatProductSetFromOptions() first", errstr);
    PetscCheck(mat->product, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Missing struct after symbolic phase for product %s", errstr);
  }
  PetscFunctionReturn(0);
}

/*@
   MatProductSetFill - Set an expected fill of the matrix product.

   Collective on Mat

   Input Parameters:
+  mat - the matrix product result matrix
-  fill - expected fill as ratio of nnz(mat)/(nnz(A) + nnz(B) + nnz(C)); use `PETSC_DEFAULT` if you do not have a good estimate. If the product is a dense matrix, this value is not used.

   Level: intermediate

.seealso: `MatProductSetFromOptions()`, `MatProductSetType()`, `MatProductSetAlgorithm()`, `MatProductCreate()`
@*/
PetscErrorCode MatProductSetFill(Mat mat, PetscReal fill)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  MatCheckProduct(mat, 1);
  if (fill == PETSC_DEFAULT || fill == PETSC_DECIDE) mat->product->fill = 2.0;
  else mat->product->fill = fill;
  PetscFunctionReturn(0);
}

/*@
   MatProductSetAlgorithm - Requests a particular algorithm for a matrix product computation that will perform to compute the given matrix

   Collective on mat

   Input Parameters:
+  mat - the matrix product
-  alg - particular implementation algorithm of the matrix product, e.g., `MATPRODUCTALGORITHMDEFAULT`.

   Options Database Key:
.  -mat_product_algorithm <algorithm> - Sets the algorithm; use -help for a list
    of available algorithms (for instance, scalable, outerproduct, etc.)

   Level: intermediate

.seealso: `MatProductSetType()`, `MatProductSetFill()`, `MatProductCreate()`, `MatProductAlgorithm`, `MatProductType`
@*/
PetscErrorCode MatProductSetAlgorithm(Mat mat, MatProductAlgorithm alg)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  MatCheckProduct(mat, 1);
  PetscCall(PetscFree(mat->product->alg));
  PetscCall(PetscStrallocpy(alg, &mat->product->alg));
  PetscFunctionReturn(0);
}

/*@
   MatProductSetType - Sets a particular matrix product type to be used to compute the given matrix

   Collective on mat

   Input Parameters:
+  mat - the matrix
-  productype   - matrix product type, e.g., `MATPRODUCT_AB`,`MATPRODUCT_AtB`,`MATPRODUCT_ABt`,`MATPRODUCT_PtAP`,`MATPRODUCT_RARt`,`MATPRODUCT_ABC`.

   Level: intermediate

   Note:
   The small t represents the transpose operation.

.seealso: `MatProductCreate()`, `MatProductType`, `MatProductType`,
          `MATPRODUCT_AB`, `MATPRODUCT_AtB`, `MATPRODUCT_ABt`, `MATPRODUCT_PtAP`, `MATPRODUCT_RARt`, `MATPRODUCT_ABC`
@*/
PetscErrorCode MatProductSetType(Mat mat, MatProductType productype)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  MatCheckProduct(mat, 1);
  PetscValidLogicalCollectiveEnum(mat, productype, 2);
  if (productype != mat->product->type) {
    if (mat->product->destroy) PetscCall((*mat->product->destroy)(mat->product->data));
    mat->product->destroy     = NULL;
    mat->product->data        = NULL;
    mat->ops->productsymbolic = NULL;
    mat->ops->productnumeric  = NULL;
  }
  mat->product->type = productype;
  PetscFunctionReturn(0);
}

/*@
   MatProductClear - Clears matrix product internal datastructures.

   Collective on mat

   Input Parameters:
.  mat - the product matrix

   Level: intermediate

   Notes:
   This function should be called to remove any intermediate data used to compute the matrix to free up memory.

   After having called this function, matrix-matrix operations can no longer be used on mat

.seealso: `MatProductCreate()`
@*/
PetscErrorCode MatProductClear(Mat mat)
{
  Mat_Product *product = mat->product;

  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  if (product) {
    PetscCall(MatDestroy(&product->A));
    PetscCall(MatDestroy(&product->B));
    PetscCall(MatDestroy(&product->C));
    PetscCall(PetscFree(product->alg));
    PetscCall(MatDestroy(&product->Dwork));
    if (product->destroy) PetscCall((*product->destroy)(product->data));
  }
  PetscCall(PetscFree(mat->product));
  mat->ops->productsymbolic = NULL;
  mat->ops->productnumeric  = NULL;
  PetscFunctionReturn(0);
}

/* Create a supporting struct and attach it to the matrix product */
PetscErrorCode MatProductCreate_Private(Mat A, Mat B, Mat C, Mat D)
{
  Mat_Product *product = NULL;

  PetscFunctionBegin;
  PetscValidHeaderSpecific(D, MAT_CLASSID, 4);
  PetscCheck(!D->product, PetscObjectComm((PetscObject)D), PETSC_ERR_PLIB, "Product already present");
  PetscCall(PetscNew(&product));
  product->A        = A;
  product->B        = B;
  product->C        = C;
  product->type     = MATPRODUCT_UNSPECIFIED;
  product->Dwork    = NULL;
  product->api_user = PETSC_FALSE;
  product->clear    = PETSC_FALSE;
  D->product        = product;

  PetscCall(MatProductSetAlgorithm(D, MATPRODUCTALGORITHMDEFAULT));
  PetscCall(MatProductSetFill(D, PETSC_DEFAULT));

  PetscCall(PetscObjectReference((PetscObject)A));
  PetscCall(PetscObjectReference((PetscObject)B));
  PetscCall(PetscObjectReference((PetscObject)C));
  PetscFunctionReturn(0);
}

/*@
   MatProductCreateWithMat - Setup a given matrix as a matrix product of other matrices

   Collective on Mat

   Input Parameters:
+  A - the first matrix
.  B - the second matrix
.  C - the third matrix (optional)
-  D - the matrix which will be used to hold the product

   Output Parameters:
.  D - the product matrix

   Notes:
   Use `MatProductCreate()` if the matrix you wish computed (the D matrix) does not already exist

   See `MatProductCreate()` for details on the usage of the MatProduct routines

   Any product data currently attached to D will be cleared

   Level: intermediate

.seealso: `MatProductCreate()`, `MatProductClear()`
@*/
PetscErrorCode MatProductCreateWithMat(Mat A, Mat B, Mat C, Mat D)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(A, MAT_CLASSID, 1);
  PetscValidType(A, 1);
  MatCheckPreallocated(A, 1);
  PetscCheck(A->assembled, PetscObjectComm((PetscObject)A), PETSC_ERR_ARG_WRONGSTATE, "Not for unassembled matrix");
  PetscCheck(!A->factortype, PetscObjectComm((PetscObject)A), PETSC_ERR_ARG_WRONGSTATE, "Not for factored matrix");

  PetscValidHeaderSpecific(B, MAT_CLASSID, 2);
  PetscValidType(B, 2);
  MatCheckPreallocated(B, 2);
  PetscCheck(B->assembled, PetscObjectComm((PetscObject)B), PETSC_ERR_ARG_WRONGSTATE, "Not for unassembled matrix");
  PetscCheck(!B->factortype, PetscObjectComm((PetscObject)B), PETSC_ERR_ARG_WRONGSTATE, "Not for factored matrix");

  if (C) {
    PetscValidHeaderSpecific(C, MAT_CLASSID, 3);
    PetscValidType(C, 3);
    MatCheckPreallocated(C, 3);
    PetscCheck(C->assembled, PetscObjectComm((PetscObject)C), PETSC_ERR_ARG_WRONGSTATE, "Not for unassembled matrix");
    PetscCheck(!C->factortype, PetscObjectComm((PetscObject)C), PETSC_ERR_ARG_WRONGSTATE, "Not for factored matrix");
  }

  PetscValidHeaderSpecific(D, MAT_CLASSID, 4);
  PetscValidType(D, 4);
  MatCheckPreallocated(D, 4);
  PetscCheck(D->assembled, PetscObjectComm((PetscObject)D), PETSC_ERR_ARG_WRONGSTATE, "Not for unassembled matrix");
  PetscCheck(!D->factortype, PetscObjectComm((PetscObject)D), PETSC_ERR_ARG_WRONGSTATE, "Not for factored matrix");

  /* Create a supporting struct and attach it to D */
  PetscCall(MatProductClear(D));
  PetscCall(MatProductCreate_Private(A, B, C, D));
  PetscFunctionReturn(0);
}

/*@
   MatProductCreate - create a matrix to hold the result of a matrix-matrix product operation

   Collective on A

   Input Parameters:
+  A - the first matrix
.  B - the second matrix
-  C - the third matrix (optional)

   Output Parameters:
.  D - the product matrix

   Level: intermediate

   Example of Usage:
.vb
    MatProductCreate(A,B,C,&D); or MatProductCreateWithMat(A,B,C,D)
    MatProductSetType(D, MATPRODUCT_AB or MATPRODUCT_AtB or MATPRODUCT_ABt or MATPRODUCT_PtAP or MATPRODUCT_RARt or MATPRODUCT_ABC)
    MatProductSetAlgorithm(D, alg)
    MatProductSetFill(D,fill)
    MatProductSetFromOptions(D)
    MatProductSymbolic(D)
    MatProductNumeric(D)
    Change numerical values in some of the matrices
    MatProductNumeric(D)
.ve

   Notes:
   Use `MatProductCreateWithMat()` if the matrix you wish computed, the D matrix, already exists.

   The information computed during the symbolic stage can be reused for new numerical computations with the same non-zero structure

   Developer Note:
   It is undocumented what happens if the nonzero structure of the input matrices changes. Is the symbolic stage automatically redone? Does it crash?
   Is there error checking for it?

.seealso: `MatProductCreateWithMat()`, `MatProductSetType()`, `MatProductSetAlgorithm()`, `MatProductClear()`
@*/
PetscErrorCode MatProductCreate(Mat A, Mat B, Mat C, Mat *D)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(A, MAT_CLASSID, 1);
  PetscValidType(A, 1);
  PetscValidHeaderSpecific(B, MAT_CLASSID, 2);
  PetscValidType(B, 2);
  PetscCheck(!A->factortype, PetscObjectComm((PetscObject)A), PETSC_ERR_ARG_WRONGSTATE, "Not for factored matrix A");
  PetscCheck(!B->factortype, PetscObjectComm((PetscObject)B), PETSC_ERR_ARG_WRONGSTATE, "Not for factored matrix B");

  if (C) {
    PetscValidHeaderSpecific(C, MAT_CLASSID, 3);
    PetscValidType(C, 3);
    PetscCheck(!C->factortype, PetscObjectComm((PetscObject)C), PETSC_ERR_ARG_WRONGSTATE, "Not for factored matrix C");
  }

  PetscValidPointer(D, 4);
  PetscCall(MatCreate(PetscObjectComm((PetscObject)A), D));
  PetscCall(MatProductCreate_Private(A, B, C, *D));
  PetscFunctionReturn(0);
}

/*
   These are safe basic implementations of ABC, RARt and PtAP
   that do not rely on mat->ops->matmatop function pointers.
   They only use the MatProduct API and are currently used by
   cuSPARSE and KOKKOS-KERNELS backends
*/
typedef struct {
  Mat BC;
  Mat ABC;
} MatMatMatPrivate;

static PetscErrorCode MatDestroy_MatMatMatPrivate(void *data)
{
  MatMatMatPrivate *mmdata = (MatMatMatPrivate *)data;

  PetscFunctionBegin;
  PetscCall(MatDestroy(&mmdata->BC));
  PetscCall(MatDestroy(&mmdata->ABC));
  PetscCall(PetscFree(data));
  PetscFunctionReturn(0);
}

static PetscErrorCode MatProductNumeric_ABC_Basic(Mat mat)
{
  Mat_Product      *product = mat->product;
  MatMatMatPrivate *mmabc;

  PetscFunctionBegin;
  MatCheckProduct(mat, 1);
  PetscCheck(mat->product->data, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Product data empty");
  mmabc = (MatMatMatPrivate *)mat->product->data;
  PetscCheck(mmabc->BC->ops->productnumeric, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Missing numeric stage");
  /* use function pointer directly to prevent logging */
  PetscCall((*mmabc->BC->ops->productnumeric)(mmabc->BC));
  /* swap ABC product stuff with that of ABC for the numeric phase on mat */
  mat->product             = mmabc->ABC->product;
  mat->ops->productnumeric = mmabc->ABC->ops->productnumeric;
  /* use function pointer directly to prevent logging */
  PetscUseTypeMethod(mat, productnumeric);
  mat->ops->productnumeric = MatProductNumeric_ABC_Basic;
  mat->product             = product;
  PetscFunctionReturn(0);
}

PetscErrorCode MatProductSymbolic_ABC_Basic(Mat mat)
{
  Mat_Product      *product = mat->product;
  Mat               A, B, C;
  MatProductType    p1, p2;
  MatMatMatPrivate *mmabc;
  const char       *prefix;

  PetscFunctionBegin;
  MatCheckProduct(mat, 1);
  PetscCheck(!mat->product->data, PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Product data not empty");
  PetscCall(MatGetOptionsPrefix(mat, &prefix));
  PetscCall(PetscNew(&mmabc));
  product->data    = mmabc;
  product->destroy = MatDestroy_MatMatMatPrivate;
  switch (product->type) {
  case MATPRODUCT_PtAP:
    p1 = MATPRODUCT_AB;
    p2 = MATPRODUCT_AtB;
    A  = product->B;
    B  = product->A;
    C  = product->B;
    break;
  case MATPRODUCT_RARt:
    p1 = MATPRODUCT_ABt;
    p2 = MATPRODUCT_AB;
    A  = product->B;
    B  = product->A;
    C  = product->B;
    break;
  case MATPRODUCT_ABC:
    p1 = MATPRODUCT_AB;
    p2 = MATPRODUCT_AB;
    A  = product->A;
    B  = product->B;
    C  = product->C;
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)mat), PETSC_ERR_PLIB, "Not for ProductType %s", MatProductTypes[product->type]);
  }
  PetscCall(MatProductCreate(B, C, NULL, &mmabc->BC));
  PetscCall(MatSetOptionsPrefix(mmabc->BC, prefix));
  PetscCall(MatAppendOptionsPrefix(mmabc->BC, "P1_"));
  PetscCall(MatProductSetType(mmabc->BC, p1));
  PetscCall(MatProductSetAlgorithm(mmabc->BC, MATPRODUCTALGORITHMDEFAULT));
  PetscCall(MatProductSetFill(mmabc->BC, product->fill));
  mmabc->BC->product->api_user = product->api_user;
  PetscCall(MatProductSetFromOptions(mmabc->BC));
  PetscCheck(mmabc->BC->ops->productsymbolic, PetscObjectComm((PetscObject)mat), PETSC_ERR_SUP, "Symbolic ProductType %s not supported with %s and %s", MatProductTypes[p1], ((PetscObject)B)->type_name, ((PetscObject)C)->type_name);
  /* use function pointer directly to prevent logging */
  PetscCall((*mmabc->BC->ops->productsymbolic)(mmabc->BC));

  PetscCall(MatProductCreate(A, mmabc->BC, NULL, &mmabc->ABC));
  PetscCall(MatSetOptionsPrefix(mmabc->ABC, prefix));
  PetscCall(MatAppendOptionsPrefix(mmabc->ABC, "P2_"));
  PetscCall(MatProductSetType(mmabc->ABC, p2));
  PetscCall(MatProductSetAlgorithm(mmabc->ABC, MATPRODUCTALGORITHMDEFAULT));
  PetscCall(MatProductSetFill(mmabc->ABC, product->fill));
  mmabc->ABC->product->api_user = product->api_user;
  PetscCall(MatProductSetFromOptions(mmabc->ABC));
  PetscCheck(mmabc->ABC->ops->productsymbolic, PetscObjectComm((PetscObject)mat), PETSC_ERR_SUP, "Symbolic ProductType %s not supported with %s and %s", MatProductTypes[p2], ((PetscObject)A)->type_name, ((PetscObject)mmabc->BC)->type_name);
  /* swap ABC product stuff with that of ABC for the symbolic phase on mat */
  mat->product              = mmabc->ABC->product;
  mat->ops->productsymbolic = mmabc->ABC->ops->productsymbolic;
  /* use function pointer directly to prevent logging */
  PetscUseTypeMethod(mat, productsymbolic);
  mmabc->ABC->ops->productnumeric = mat->ops->productnumeric;
  mat->ops->productsymbolic       = MatProductSymbolic_ABC_Basic;
  mat->ops->productnumeric        = MatProductNumeric_ABC_Basic;
  mat->product                    = product;
  PetscFunctionReturn(0);
}

/*@
   MatProductGetType - Returns the type of matrix-matrix product associated with the given matrix.

   Not collective

   Input Parameter:
.  mat - the matrix

   Output Parameter:
.  mtype - the `MatProductType`

   Level: intermediate

.seealso: `MatProductCreateWithMat()`, `MatProductSetType()`, `MatProductCreate()`, `MatProductType`, `MatProductAlgorithm`
@*/
PetscErrorCode MatProductGetType(Mat mat, MatProductType *mtype)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  PetscValidPointer(mtype, 2);
  *mtype = MATPRODUCT_UNSPECIFIED;
  if (mat->product) *mtype = mat->product->type;
  PetscFunctionReturn(0);
}

/*@
   MatProductGetMats - Returns the matrices associated with the matrix-matrix product this matrix can receive

   Not collective

   Input Parameter:
.  mat - the product matrix

   Output Parameters:
+  A - the first matrix
.  B - the second matrix
-  C - the third matrix (optional)

   Level: intermediate

.seealso: `MatProductCreateWithMat()`, `MatProductSetType()`, `MatProductSetAlgorithm()`, `MatProductCreate()`
@*/
PetscErrorCode MatProductGetMats(Mat mat, Mat *A, Mat *B, Mat *C)
{
  PetscFunctionBegin;
  PetscValidHeaderSpecific(mat, MAT_CLASSID, 1);
  if (A) *A = mat->product ? mat->product->A : NULL;
  if (B) *B = mat->product ? mat->product->B : NULL;
  if (C) *C = mat->product ? mat->product->C : NULL;
  PetscFunctionReturn(0);
}
