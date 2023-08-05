#define TAOLINESEARCH_DLL
#include <petsc/private/taolinesearchimpl.h>

PETSC_EXTERN PetscErrorCode TaoLineSearchCreate_Unit(TaoLineSearch);
PETSC_EXTERN PetscErrorCode TaoLineSearchCreate_MT(TaoLineSearch);
PETSC_EXTERN PetscErrorCode TaoLineSearchCreate_GPCG(TaoLineSearch);
PETSC_EXTERN PetscErrorCode TaoLineSearchCreate_Armijo(TaoLineSearch);
PETSC_EXTERN PetscErrorCode TaoLineSearchCreate_OWArmijo(TaoLineSearch);
static PetscBool            TaoLineSearchPackageInitialized = PETSC_FALSE;

/*@C
  TaoLineSearchFinalizePackage - This function destroys everything in the PETSc/TAO
  interface to the TaoLineSearch package. It is called from PetscFinalize().

  Level: developer
@*/
PetscErrorCode TaoLineSearchFinalizePackage(void)
{
  PetscFunctionBegin;
  PetscCall(PetscFunctionListDestroy(&TaoLineSearchList));
  TaoLineSearchPackageInitialized = PETSC_FALSE;
  PetscFunctionReturn(0);
}

/*@C
  TaoLineSearchInitializePackage - This function registers the line-search
  algorithms in TAO.  When using shared or static libraries, this function is called from the
  first entry to TaoCreate(); when using dynamic, it is called
  from PetscDLLibraryRegister_tao()

  Level: developer

.seealso: `TaoLineSearchCreate()`
@*/
PetscErrorCode TaoLineSearchInitializePackage(void)
{
  PetscFunctionBegin;
  if (TaoLineSearchPackageInitialized) PetscFunctionReturn(0);
  TaoLineSearchPackageInitialized = PETSC_TRUE;
#if !defined(PETSC_USE_COMPLEX)
  PetscCall(PetscClassIdRegister("TaoLineSearch", &TAOLINESEARCH_CLASSID));
  PetscCall(TaoLineSearchRegister("unit", TaoLineSearchCreate_Unit));
  PetscCall(TaoLineSearchRegister("more-thuente", TaoLineSearchCreate_MT));
  PetscCall(TaoLineSearchRegister("gpcg", TaoLineSearchCreate_GPCG));
  PetscCall(TaoLineSearchRegister("armijo", TaoLineSearchCreate_Armijo));
  PetscCall(TaoLineSearchRegister("owarmijo", TaoLineSearchCreate_OWArmijo));
  PetscCall(PetscLogEventRegister("TaoLSApply", TAOLINESEARCH_CLASSID, &TAOLINESEARCH_Apply));
  PetscCall(PetscLogEventRegister("TaoLSEval", TAOLINESEARCH_CLASSID, &TAOLINESEARCH_Eval));
#endif
  PetscCall(PetscRegisterFinalize(TaoLineSearchFinalizePackage));
  PetscFunctionReturn(0);
}
