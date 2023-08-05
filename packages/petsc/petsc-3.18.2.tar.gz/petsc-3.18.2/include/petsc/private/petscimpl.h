
/*
    Defines the basic header of all PETSc objects.
*/
#ifndef PETSCIMPL_H
#define PETSCIMPL_H
#include <petscsys.h>

/* SUBMANSEC = Sys */

#if defined(PETSC_CLANG_STATIC_ANALYZER)
  #define PetscDisableStaticAnalyzerForExpressionUnderstandingThatThisIsDangerousAndBugprone(expr)
#else
  #define PetscDisableStaticAnalyzerForExpressionUnderstandingThatThisIsDangerousAndBugprone(expr) expr
#endif

#if PetscDefined(USE_DEBUG)
PETSC_INTERN PetscErrorCode PetscStackSetCheck(PetscBool);
PETSC_INTERN PetscErrorCode PetscStackView(FILE *);
PETSC_INTERN PetscErrorCode PetscStackReset(void);
PETSC_INTERN PetscErrorCode PetscStackCopy(PetscStack *, PetscStack *);
PETSC_INTERN PetscErrorCode PetscStackPrint(PetscStack *, FILE *);
#else
  #define PetscStackSetCheck(check)         0
  #define PetscStackView(file)              0
  #define PetscStackReset()                 0
  #define PetscStackCopy(stackin, stackout) 0
  #define PetscStackPrint(stack, file)      0
#endif /* PetscDefined(USE_DEBUG) */

/* These are used internally by PETSc ASCII IO routines*/
#include <stdarg.h>
PETSC_EXTERN PetscErrorCode PetscVFPrintfDefault(FILE *, const char[], va_list);

/*
   All major PETSc data structures have a common core; this is defined
   below by PETSCHEADER.

   PetscHeaderCreate() should be used whenever creating a PETSc structure.
*/

/*
   PetscOps: structure of core operations that all PETSc objects support.

      getcomm()         - Gets the object's communicator.
      view()            - Is the routine for viewing the entire PETSc object; for
                          example, MatView() is the general matrix viewing routine.
                          This is used by PetscObjectView((PetscObject)obj) to allow
                          viewing any PETSc object.
      destroy()         - Is the routine for destroying the entire PETSc object;
                          for example,MatDestroy() is the general matrix
                          destruction routine.
                          This is used by PetscObjectDestroy((PetscObject*)&obj) to allow
                          destroying any PETSc object.
      compose()         - Associates a PETSc object with another PETSc object with a name
      query()           - Returns a different PETSc object that has been associated
                          with the first object using a name.
      composefunction() - Attaches an a function to a PETSc object with a name.
      queryfunction()   - Requests a registered function that has been attached to a PETSc object.
*/

typedef struct {
  PetscErrorCode (*view)(PetscObject, PetscViewer);
  PetscErrorCode (*destroy)(PetscObject *);
  PetscErrorCode (*compose)(PetscObject, const char[], PetscObject);
  PetscErrorCode (*query)(PetscObject, const char[], PetscObject *);
  PetscErrorCode (*composefunction)(PetscObject, const char[], void (*)(void));
  PetscErrorCode (*queryfunction)(PetscObject, const char[], void (**)(void));
} PetscOps;

typedef enum {
  PETSC_FORTRAN_CALLBACK_CLASS,
  PETSC_FORTRAN_CALLBACK_SUBTYPE,
  PETSC_FORTRAN_CALLBACK_MAXTYPE
} PetscFortranCallbackType;
typedef size_t PetscFortranCallbackId;
#define PETSC_SMALLEST_FORTRAN_CALLBACK ((PetscFortranCallbackId)1000)
PETSC_EXTERN PetscErrorCode PetscFortranCallbackRegister(PetscClassId, const char *, PetscFortranCallbackId *);
PETSC_EXTERN PetscErrorCode PetscFortranCallbackGetSizes(PetscClassId, PetscFortranCallbackId *, PetscFortranCallbackId *);

typedef struct {
  void (*func)(void);
  void *ctx;
} PetscFortranCallback;

/*
   All PETSc objects begin with the fields defined in PETSCHEADER.
   The PetscObject is a way of examining these fields regardless of
   the specific object. In C++ this could be a base abstract class
   from which all objects are derived.
*/
#define PETSC_MAX_OPTIONS_HANDLER 5
typedef struct _p_PetscObject {
  PetscOps      bops[1];
  PetscClassId  classid;
  MPI_Comm      comm;
  PetscObjectId id; /* this is used to compare object for identity that may no longer exist since memory addresses get recycled for new objects */
  PetscInt      refct;
  PetscErrorCode (*non_cyclic_references)(PetscObject, PetscInt *);
  PetscInt64        cidx;
  PetscMPIInt       tag;
  PetscFunctionList qlist;
  PetscObjectList   olist;
  char             *class_name; /*  for example, "Vec" */
  char             *description;
  char             *mansec;
  char             *type_name; /*  this is the subclass, for example VECSEQ which equals "seq" */
  char             *name;
  char             *prefix;
  PetscInt          tablevel;
  void             *cpp;
  PetscObjectState  state;
  PetscInt          int_idmax, intstar_idmax;
  PetscObjectState *intcomposedstate, *intstarcomposedstate;
  PetscInt         *intcomposeddata, **intstarcomposeddata;
  PetscInt          real_idmax, realstar_idmax;
  PetscObjectState *realcomposedstate, *realstarcomposedstate;
  PetscReal        *realcomposeddata, **realstarcomposeddata;
  PetscInt          scalar_idmax, scalarstar_idmax;
  PetscObjectState *scalarcomposedstate, *scalarstarcomposedstate;
  PetscScalar      *scalarcomposeddata, **scalarstarcomposeddata;
  void (**fortran_func_pointers)(void);             /* used by Fortran interface functions to stash user provided Fortran functions */
  PetscFortranCallbackId num_fortran_func_pointers; /* number of Fortran function pointers allocated */
  PetscFortranCallback  *fortrancallback[PETSC_FORTRAN_CALLBACK_MAXTYPE];
  PetscFortranCallbackId num_fortrancallback[PETSC_FORTRAN_CALLBACK_MAXTYPE];
  void                  *python_context;
  PetscErrorCode (*python_destroy)(void *);

  PetscInt noptionhandler;
  PetscErrorCode (*optionhandler[PETSC_MAX_OPTIONS_HANDLER])(PetscObject, PetscOptionItems *, void *);
  PetscErrorCode (*optiondestroy[PETSC_MAX_OPTIONS_HANDLER])(PetscObject, void *);
  void *optionctx[PETSC_MAX_OPTIONS_HANDLER];
#if defined(PETSC_HAVE_SAWS)
  PetscBool amsmem;          /* if PETSC_TRUE then this object is registered with SAWs and visible to clients */
  PetscBool amspublishblock; /* if PETSC_TRUE and publishing objects then will block at PetscObjectSAWsBlock() */
#endif
  PetscOptions options; /* options database used, NULL means default */
  PetscBool    optionsprinted;
  PetscBool    donotPetscObjectPrintClassNamePrefixType;
} _p_PetscObject;

#define PETSCHEADER(ObjectOps) \
  _p_PetscObject hdr; \
  ObjectOps      ops[1]

#define PETSCFREEDHEADER -1

PETSC_EXTERN_TYPEDEF typedef PetscErrorCode (*PetscObjectDestroyFunction)(PetscObject *); /* force cast in next macro to NEVER use extern "C" style */
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode (*PetscObjectViewFunction)(PetscObject, PetscViewer);

/*@C
    PetscHeaderCreate - Creates a PETSc object of a particular class

    Input Parameters:
+   classid - the classid associated with this object (for example VEC_CLASSID)
.   class_name - string name of class; should be static (for example "Vec")
.   descr - string containing short description; should be static (for example "Vector")
.   mansec - string indicating section in manual pages; should be static (for example "Vec")
.   comm - the MPI Communicator
.   destroy - the destroy routine for this object (for example `VecDestroy()`)
-   view - the view routine for this object (for example `VecView()`)

    Output Parameter:
.   h - the newly created object

    Level: developer

.seealso: `PetscHeaderDestroy()`, `PetscClassIdRegister()`

@*/
#define PetscHeaderCreate(h, classid, class_name, descr, mansec, comm, destroy, view) \
  (PetscNew(&(h)) || PetscHeaderCreate_Private((PetscObject)(h), classid, class_name, descr, mansec, comm, (PetscObjectDestroyFunction)(destroy), (PetscObjectViewFunction)(view)) || PetscLogObjectCreate(h))

PETSC_EXTERN PetscErrorCode PetscComposedQuantitiesDestroy(PetscObject obj);
PETSC_EXTERN PetscErrorCode PetscHeaderCreate_Private(PetscObject, PetscClassId, const char[], const char[], const char[], MPI_Comm, PetscObjectDestroyFunction, PetscObjectViewFunction);
PETSC_INTERN PetscObjectId  PetscObjectNewId_Internal(void);

/*@C
    PetscHeaderDestroy - Final step in destroying a PetscObject

    Input Parameters:
.   h - the header created with `PetscHeaderCreate()`

    Level: developer

.seealso: `PetscHeaderCreate()`
@*/
#define PetscHeaderDestroy(h) (PetscHeaderDestroy_Private((PetscObject)(*(h)), PETSC_FALSE) || PetscFree(*(h)))

PETSC_EXTERN PetscErrorCode                PetscHeaderDestroy_Private(PetscObject, PetscBool);
PETSC_SINGLE_LIBRARY_INTERN PetscErrorCode PetscHeaderReset_Internal(PetscObject);
PETSC_EXTERN PetscErrorCode                PetscObjectCopyFortranFunctionPointers(PetscObject, PetscObject);
PETSC_EXTERN PetscErrorCode                PetscObjectSetFortranCallback(PetscObject, PetscFortranCallbackType, PetscFortranCallbackId *, void (*)(void), void *ctx);
PETSC_EXTERN PetscErrorCode                PetscObjectGetFortranCallback(PetscObject, PetscFortranCallbackType, PetscFortranCallbackId, void (**)(void), void **ctx);

PETSC_INTERN PetscErrorCode PetscCitationsInitialize(void);
PETSC_INTERN PetscErrorCode PetscFreeMPIResources(void);
PETSC_INTERN PetscErrorCode PetscOptionsHasHelpIntro_Internal(PetscOptions, PetscBool *);

/* Code shared between C and Fortran */
PETSC_INTERN PetscErrorCode PetscInitialize_Common(const char *, const char *, const char *, PetscBool, PetscBool, PetscInt);

#if PetscDefined(HAVE_SETJMP_H)
PETSC_EXTERN PetscBool PetscCheckPointer(const void *, PetscDataType);
#else
  #define PetscCheckPointer(ptr, data_type) (ptr ? PETSC_TRUE : PETSC_FALSE)
#endif
#if !defined(PETSC_CLANG_STATIC_ANALYZER)
  /*
    Macros to test if a PETSc object is valid and if pointers are valid
*/
  #if !defined(PETSC_USE_DEBUG)

    #define PetscValidHeaderSpecific(h, ck, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidHeaderSpecificType(h, ck, arg, t) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidHeader(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidPointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidCharPointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidIntPointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidInt64Pointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidCountPointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidBoolPointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidScalarPointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidRealPointer(h, arg) \
      do { \
        (void)(h); \
      } while (0)
    #define PetscValidFunction(h, arg) \
      do { \
        (void)(h); \
      } while (0)

  #else

    /*  This check is for subtype methods such as DMDAGetCorners() that do not use the PetscTryMethod() or PetscUseMethod() paradigm */
    #define PetscValidHeaderSpecificType(h, ck, arg, t) \
      do { \
        PetscBool _7_same; \
        PetscValidHeaderSpecific(h, ck, arg); \
        PetscCall(PetscObjectTypeCompare((PetscObject)(h), t, &_7_same)); \
        PetscCheck(_7_same, PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Wrong subtype object:Parameter # %d must have implementation %s it is %s", arg, t, ((PetscObject)(h))->type_name); \
      } while (0)

    #define PetscValidPointer_Internal(ptr, arg, ptype, ptrtype) \
      do { \
        PetscCheck(ptr, PETSC_COMM_SELF, PETSC_ERR_ARG_NULL, "Null Pointer: Parameter # %d", arg); \
        PetscCheck(PetscCheckPointer(ptr, ptype), PETSC_COMM_SELF, PETSC_ERR_ARG_BADPTR, "Invalid Pointer to " PetscStringize(ptrtype) ": Argument '" PetscStringize(ptr) "' (parameter # %d)", arg); \
      } while (0)

    #define PetscValidHeaderSpecific(h, ck, arg) \
      do { \
        PetscValidPointer_Internal(h, arg, PETSC_OBJECT, PetscObject); \
        if (((PetscObject)(h))->classid != ck) { \
          PetscCheck(((PetscObject)(h))->classid != PETSCFREEDHEADER, PETSC_COMM_SELF, PETSC_ERR_ARG_CORRUPT, "Object already free: Parameter # %d", arg); \
          SETERRQ(PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Wrong type of object: Parameter # %d", arg); \
        } \
      } while (0)

    #define PetscValidHeader(h, arg) \
      do { \
        PetscValidPointer_Internal(h, arg, PETSC_OBJECT, PetscObject); \
        PetscCheck(((PetscObject)(h))->classid != PETSCFREEDHEADER, PETSC_COMM_SELF, PETSC_ERR_ARG_CORRUPT, "Object already free: Parameter # %d", arg); \
        PetscCheck(((PetscObject)(h))->classid >= PETSC_SMALLEST_CLASSID && ((PetscObject)(h))->classid <= PETSC_LARGEST_CLASSID, PETSC_COMM_SELF, PETSC_ERR_ARG_CORRUPT, "Invalid type of object: Parameter # %d", arg); \
      } while (0)

    #define PetscValidPointer(h, arg)       PetscValidPointer_Internal(h, arg, PETSC_CHAR, memory)
    #define PetscValidCharPointer(h, arg)   PetscValidPointer_Internal(h, arg, PETSC_CHAR, char)
    #define PetscValidIntPointer(h, arg)    PetscValidPointer_Internal(h, arg, PETSC_INT, PetscInt)
    #define PetscValidInt64Pointer(h, arg)  PetscValidPointer_Internal(h, arg, PETSC_INT64, PetscInt)
    #define PetscValidCountPointer(h, arg)  PetscValidPointer_Internal(h, arg, PETSC_COUNT, PetscCount)
    #define PetscValidBoolPointer(h, arg)   PetscValidPointer_Internal(h, arg, PETSC_BOOL, PetscBool)
    #define PetscValidScalarPointer(h, arg) PetscValidPointer_Internal(h, arg, PETSC_SCALAR, PetscScalar)
    #define PetscValidRealPointer(h, arg)   PetscValidPointer_Internal(h, arg, PETSC_REAL, PetscReal)

    #define PetscValidFunction(f, arg) \
      do { \
        PetscCheck((f), PETSC_COMM_SELF, PETSC_ERR_ARG_NULL, "Null Function Pointer: Parameter # %d", arg); \
      } while (0)
  #endif
#else  /* PETSC_CLANG_STATIC_ANALYZER */
template <typename T>
void PetscValidHeaderSpecificType(T, PetscClassId, int, const char[]);
template <typename T>
void PetscValidHeaderSpecific(T, PetscClassId, int);
template <typename T>
void PetscValidHeaderSpecific(const T, PetscClassId, int);
template <typename T>
void PetscValidHeader(T, int);
template <typename T>
void PetscValidPointer(T, int);
template <typename T>
void PetscValidCharPointer(T *, int);
template <typename T>
void PetscValidIntPointer(T *, int);
template <typename T>
void PetscValidInt64Pointer(T *, int);
template <typename T>
void PetscValidCountPointer(T *, int);
template <typename T>
void PetscValidBoolPointer(T *, int);
template <typename T>
void PetscValidScalarPointer(T *, int);
template <typename T>
void PetscValidRealPointer(T *, int);
template <typename T>
void PetscValidFunction(T, int);
#endif /* PETSC_CLANG_STATIC_ANALYZER */

#define PetscSorted(n, idx, sorted) \
  do { \
    (sorted) = PETSC_TRUE; \
    for (PetscInt _i_ = 1; _i_ < (n); ++_i_) { \
      if ((idx)[_i_] < (idx)[_i_ - 1]) { \
        (sorted) = PETSC_FALSE; \
        break; \
      } \
    } \
  } while (0)

#if !defined(PETSC_CLANG_STATIC_ANALYZER)
  #if !defined(PETSC_USE_DEBUG)

    #define PetscCheckSameType(a, arga, b, argb) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscCheckTypeName(a, type) \
      do { \
        (void)(a); \
      } while (0)
    #define PetscCheckTypeNames(a, type1, type2) \
      do { \
        (void)(a); \
      } while (0)
    #define PetscValidType(a, arg) \
      do { \
        (void)(a); \
      } while (0)
    #define PetscCheckSameComm(a, arga, b, argb) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscCheckSameTypeAndComm(a, arga, b, argb) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscValidLogicalCollectiveScalar(a, b, arg) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscValidLogicalCollectiveReal(a, b, arg) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscValidLogicalCollectiveInt(a, b, arg) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscValidLogicalCollectiveMPIInt(a, b, arg) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscValidLogicalCollectiveBool(a, b, arg) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscValidLogicalCollectiveEnum(a, b, arg) \
      do { \
        (void)(a); \
        (void)(b); \
      } while (0)
    #define PetscCheckSorted(n, idx) \
      do { \
        (void)(n); \
        (void)(idx); \
      } while (0)

  #else

    /*
  This macro currently does nothing, the plan is for each PetscObject to have a PetscInt "type"
  member associated with the string type_name that can be quickly compared.

  **Do not swap this macro to compare string type_name!**

  This macro is used incorrectly in the code. Many places that do not need identity of the
  types incorrectly call this check and would need to be fixed if this macro is enabled.
*/
    #if 0
      #define PetscCheckSameType(a, arga, b, argb) \
        do { \
          PetscBool pcst_type_eq_ = PETSC_TRUE; \
          PetscCall(PetscStrcmp(((PetscObject)(a))->type_name, (((PetscObject)(b)))->type_name, &pcst_type_eq_)); \
          PetscCheck(pcst_type_eq_, PETSC_COMM_SELF, PETSC_ERR_ARG_NOTSAMETYPE, "Objects not of same type : Argument # % d and % d, % s != % s ", arga, argb, ((PetscObject)(a))->type_name, ((PetscObject)(b))->type_name); \
        } while (0)
    #else
      #define PetscCheckSameType(a, arga, b, argb) \
        do { \
          (void)(a); \
          (void)(b); \
        } while (0)
    #endif

    /*
    Check type_name
*/
    #define PetscCheckTypeName(a, type) \
      do { \
        PetscBool _7_match; \
        PetscCall(PetscObjectTypeCompare(((PetscObject)(a)), (type), &_7_match)); \
        PetscCheck(_7_match, PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Object (%s) is not %s", (char *)(((PetscObject)(a))->type_name), type); \
      } while (0)

    #define PetscCheckTypeNames(a, type1, type2) \
      do { \
        PetscBool _7_match; \
        PetscCall(PetscObjectTypeCompareAny(((PetscObject)(a)), &_7_match, (type1), (type2), "")); \
        PetscCheck(_7_match, PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Object (%s) is not %s or %s", (char *)(((PetscObject)(a))->type_name), type1, type2); \
      } while (0)

    /*
   Use this macro to check if the type is set
*/
    #define PetscValidType(a, arg) PetscCheck(((PetscObject)(a))->type_name, PETSC_COMM_SELF, PETSC_ERR_ARG_WRONGSTATE, "%s object's type is not set: Argument # %d", ((PetscObject)(a))->class_name, arg)

    /*
   Sometimes object must live on same communicator to inter-operate
*/
    #define PetscCheckSameComm(a, arga, b, argb) \
      do { \
        PetscMPIInt _7_flag; \
        PetscCallMPI(MPI_Comm_compare(PetscObjectComm((PetscObject)(a)), PetscObjectComm((PetscObject)(b)), &_7_flag)); \
        PetscCheck(_7_flag == MPI_CONGRUENT || _7_flag == MPI_IDENT, PETSC_COMM_SELF, PETSC_ERR_ARG_NOTSAMECOMM, "Different communicators in the two objects: Argument # %d and %d flag %d", arga, argb, _7_flag); \
      } while (0)

    #define PetscCheckSameTypeAndComm(a, arga, b, argb) \
      do { \
        PetscCheckSameType(a, arga, b, argb); \
        PetscCheckSameComm(a, arga, b, argb); \
      } while (0)

    #define PetscValidLogicalCollectiveScalar(a, b, arg) \
      do { \
        PetscScalar b0 = (b); \
        PetscReal   b1[5], b2[5]; \
        if (PetscIsNanScalar(b0)) { \
          b1[4] = 1; \
        } else { \
          b1[4] = 0; \
        }; \
        b1[0] = -PetscRealPart(b0); \
        b1[1] = PetscRealPart(b0); \
        b1[2] = -PetscImaginaryPart(b0); \
        b1[3] = PetscImaginaryPart(b0); \
        PetscCall(MPIU_Allreduce(b1, b2, 5, MPIU_REAL, MPIU_MAX, PetscObjectComm((PetscObject)(a)))); \
        PetscCheck(b2[4] > 0 || (PetscEqualReal(-b2[0], b2[1]) && PetscEqualReal(-b2[2], b2[3])), PetscObjectComm((PetscObject)(a)), PETSC_ERR_ARG_WRONG, "Scalar value must be same on all processes, argument # %d", arg); \
      } while (0)

    #define PetscValidLogicalCollectiveReal(a, b, arg) \
      do { \
        PetscReal b0 = (b), b1[3], b2[3]; \
        if (PetscIsNanReal(b0)) { \
          b1[2] = 1; \
        } else { \
          b1[2] = 0; \
        }; \
        b1[0] = -b0; \
        b1[1] = b0; \
        PetscCall(MPIU_Allreduce(b1, b2, 3, MPIU_REAL, MPIU_MAX, PetscObjectComm((PetscObject)(a)))); \
        PetscCheck(b2[2] > 0 || PetscEqualReal(-b2[0], b2[1]), PetscObjectComm((PetscObject)(a)), PETSC_ERR_ARG_WRONG, "Real value must be same on all processes, argument # %d", arg); \
      } while (0)

    #define PetscValidLogicalCollectiveInt(a, b, arg) \
      do { \
        PetscInt b0 = (b), b1[2], b2[2]; \
        b1[0]       = -b0; \
        b1[1]       = b0; \
        PetscCall(MPIU_Allreduce(b1, b2, 2, MPIU_INT, MPI_MAX, PetscObjectComm((PetscObject)(a)))); \
        PetscCheck(-b2[0] == b2[1], PetscObjectComm((PetscObject)(a)), PETSC_ERR_ARG_WRONG, "Int value must be same on all processes, argument # %d", arg); \
      } while (0)

    #define PetscValidLogicalCollectiveMPIInt(a, b, arg) \
      do { \
        PetscMPIInt b0 = (b), b1[2], b2[2]; \
        b1[0]          = -b0; \
        b1[1]          = b0; \
        PetscCall(MPIU_Allreduce(b1, b2, 2, MPI_INT, MPI_MAX, PetscObjectComm((PetscObject)(a)))); \
        PetscCheck(-b2[0] == b2[1], PetscObjectComm((PetscObject)(a)), PETSC_ERR_ARG_WRONG, "PetscMPIInt value must be same on all processes, argument # %d", arg); \
      } while (0)

    #define PetscValidLogicalCollectiveBool(a, b, arg) \
      do { \
        PetscMPIInt b0 = (PetscMPIInt)(b), b1[2], b2[2]; \
        b1[0]          = -b0; \
        b1[1]          = b0; \
        PetscCall(MPIU_Allreduce(b1, b2, 2, MPI_INT, MPI_MAX, PetscObjectComm((PetscObject)(a)))); \
        PetscCheck(-b2[0] == b2[1], PetscObjectComm((PetscObject)(a)), PETSC_ERR_ARG_WRONG, "Bool value must be same on all processes, argument # %d", arg); \
      } while (0)

    #define PetscValidLogicalCollectiveEnum(a, b, arg) \
      do { \
        PetscMPIInt b0 = (PetscMPIInt)(b), b1[2], b2[2]; \
        b1[0]          = -b0; \
        b1[1]          = b0; \
        PetscCall(MPIU_Allreduce(b1, b2, 2, MPI_INT, MPI_MAX, PetscObjectComm((PetscObject)(a)))); \
        PetscCheck(-b2[0] == b2[1], PetscObjectComm((PetscObject)(a)), PETSC_ERR_ARG_WRONG, "Enum value must be same on all processes, argument # %d", arg); \
      } while (0)

    #define PetscCheckSorted(n, idx) \
      do { \
        PetscBool _1_flg; \
        PetscSorted(n, idx, _1_flg); \
        PetscCheck(_1_flg, PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Input array needs to be sorted"); \
      } while (0)

  #endif
#else  /* PETSC_CLANG_STATIC_ANALYZER */
template <typename Ta, typename Tb>
void PetscCheckSameType(Ta, int, Tb, int);
template <typename Ta, typename Tb>
void PetscCheckTypeName(Ta, Tb);
template <typename Ta, typename Tb, typename Tc>
void PetscCheckTypeName(Ta, Tb, Tc);
template <typename T>
void PetscValidType(T, int);
template <typename Ta, typename Tb>
void PetscCheckSameComm(Ta, int, Tb, int);
template <typename Ta, typename Tb>
void PetscCheckSameTypeAndComm(Ta, int, Tb, int);
template <typename Ta, typename Tb>
void PetscValidLogicalCollectiveScalar(Ta, Tb, int);
template <typename Ta, typename Tb>
void PetscValidLogicalCollectiveReal(Ta, Tb, int);
template <typename Ta, typename Tb>
void PetscValidLogicalCollectiveInt(Ta, Tb, int);
template <typename Ta, typename Tb>
void PetscValidLogicalCollectiveMPIInt(Ta, Tb, int);
template <typename Ta, typename Tb>
void PetscValidLogicalCollectiveBool(Ta, Tb, int);
template <typename Ta, typename Tb>
void PetscValidLogicalCollectiveEnum(Ta, Tb, int);
template <typename T>
void PetscCheckSorted(PetscInt, T);
#endif /* PETSC_CLANG_STATIC_ANALYZER */

/*MC
   PetscTryMethod - Queries an object for a method added with `PetscObjectComposeFunction()`, if it exists then calls it.

  Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscTryMethod(PetscObject obj,const char *name,(arg_types),(arg_value))

   Input Parameters:
+   obj - the object
.   name - the name of the method, for example, "KSPGMRESSetRestart_C" for the function `KSPGMRESSetRestart()`
.   arg_types - the argument types for the method, for example, (KSP,PetscInt)
-   args - the arguements for the method, for example, (ksp,restart))

   Level: developer

   Notes:
   The object is always the implicit first argument of the method and is not listed in arg_types or args

   This does not return an error code, it is a macro that returns with an error code on error.

   Use `PetscUseTypeMethod()` or `PetscTryTypeMethod()` to call functions that are included in the objects function table, the `ops` array
   in the object.

.seealso: `PetscUseMethod()`, `PetscCall()`, `PetscUseTypeMethod()`, `PetscTryTypeMethod()`, `PetscCheck()`
M*/
#define PetscTryMethod(obj, A, B, C) \
  do { \
    PetscErrorCode(*_7_f) B; \
    PetscCall(PetscObjectQueryFunction((PetscObject)(obj), A, &_7_f)); \
    if (_7_f) PetscCall((*_7_f)C); \
  } while (0)

/*MC
   PetscUseMethod - Queries an object for a method added with `PetscObjectComposeFunction()`, if it exists then calls it, otherwise generates an error.

  Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscUseMethod(PetscObject obj,const char *name,(arg_types),(arg_value))

   Input Parameters:
+   obj - the object
.   name - the name of the method, for example, "KSPGMRESSetRestart_C" for the function `KSPGMRESSetRestart()`
.   arg_types - the argument types for the method, for example, (KSP,PetscInt)
-   args - the arguements for the method, for example, (ksp,restart))

   Level: developer

   Notes:
   The object is always the implicit first argument of the method and is not listed in arg_types or args

   This does not return an error code, it is a macro that returns with an error code on error.

   Use `PetscUseTypeMethod()` or `PetscTryTypeMethod()` to call functions that are included in the objects function table, the `ops` array
   in the object.

.seealso: `PetscTryMethod()`, `PetscCall()`, `PetscUseTypeMethod()`, `PetscTryTypeMethod()`, `PetscCheck()`
M*/
#define PetscUseMethod(obj, A, B, C) \
  do { \
    PetscErrorCode(*_7_f) B; \
    PetscCall(PetscObjectQueryFunction((PetscObject)(obj), A, &_7_f)); \
    PetscCheck(_7_f, PetscObjectComm((PetscObject)(obj)), PETSC_ERR_SUP, "Cannot locate function %s in object", A); \
    PetscCall((*_7_f)C); \
  } while (0)

/*
  Use Microsoft traditional preprocessor.

  The Microsoft compiler option -Zc:preprocessor available in recent versions of the compiler
  sets  _MSVC_TRADITIONAL to zero so this code path is not used.

  It appears the Intel Windows compiler icl does not have an equaivalent of  -Zc:preprocessor

  These macros use the trick that Windows compilers remove the , before the __VA_ARGS__ if __VA_ARGS__ does not exist

  PetscCall() cannot be used in the macros because the remove the , trick does not work in a macro in a macro
*/
#if (defined(_MSC_VER) && (!defined(_MSVC_TRADITIONAL) || _MSVC_TRADITIONAL)) || defined(__ICL)

  #define PetscUseTypeMethod(obj, OP, ...) \
    do { \
      PetscErrorCode ierr_p_; \
      PetscStackUpdateLine; \
      PetscCheck((obj)->ops->OP, PetscObjectComm((PetscObject)obj), PETSC_ERR_SUP, "No method %s for %s of type %s", PetscStringize(OP), ((PetscObject)obj)->class_name, ((PetscObject)obj)->type_name); \
      ierr_p_ = (*(obj)->ops->OP)(obj, __VA_ARGS__); \
      PetscCall(ierr_p_); \
    } while (0)

  #define PetscTryTypeMethod(obj, OP, ...) \
    do { \
      if ((obj)->ops->OP) { \
        PetscErrorCode ierr_p_; \
        PetscStackUpdateLine; \
        ierr_p_ = (*(obj)->ops->OP)(obj, __VA_ARGS__); \
        PetscCall(ierr_p_); \
      } \
    } while (0)

#else

  /*MC
   PetscUseTypeMethod - Call a method on a PETSc object, that is a function in the objects function table obj->ops, error if the method does not exist

  Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscUseTypeMethod(obj,method,other_args)

   Input Parameters:
+   obj - the object the method is called on
.   method - the name of the method, for example, mult for the PETSc routine MatMult()
-   other_args - the other arguments for the method, obj is the first argument

   Level: developer

   Note:
   This does not return an error code, it is a macro that returns with an error code on error.

   Use `PetscUseMethod()` or `PetscTryMethod()` to call functions that have been composed to an object with `PetscObjectComposeFunction()`

.seealso: `PetscTryMethod()`, `PetscUseMethod()`, `PetscCall()`, `PetscCheck()`, `PetscTryTypeMethod()`
M*/
  #define PetscUseTypeMethod(obj, ...) \
    do { \
      PetscCheck((obj)->ops->PETSC_FIRST_ARG((__VA_ARGS__, unused)), PetscObjectComm((PetscObject)obj), PETSC_ERR_SUP, "No method %s for %s of type %s", \
                 PetscStringize(PETSC_FIRST_ARG((__VA_ARGS__,unused))), ((PetscObject)obj)->class_name, ((PetscObject)obj)->type_name); \
      PetscCall((*(obj)->ops->PETSC_FIRST_ARG((__VA_ARGS__, unused)))(obj PETSC_REST_ARG(__VA_ARGS__))); \
    } while (0)

  /*MC
   PetscTryTypeMethod - Call a method on a PETSc object, that is a function in the objects function table obj->ops, skip if the method does not exist

  Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscTryTtype(obj,method,other_args)

   Input Parameters:
+   obj - the object the method is called on
.   method - the name of the method, for example, mult for the PETSc routine MatMult()
-   other_args - the other arguments for the method, obj is the first argument

   Level: developer

   Note:
   This does not return an error code, it is a macro that returns with an error code on error.

   Use `PetscUseMethod()` or `PetscTryMethod()` to call functions that have been composed to an object with `PetscObjectComposeFunction()`

.seealso: `PetscTryMethod()`, `PetscUseMethod()`, `PetscCall()`, `PetscCheck()`, `PetscUseTypeMethod()`
M*/
  #define PetscTryTypeMethod(obj, ...) \
    do { \
      if ((obj)->ops->PETSC_FIRST_ARG((__VA_ARGS__, unused))) PetscCall((*(obj)->ops->PETSC_FIRST_ARG((__VA_ARGS__, unused)))(obj PETSC_REST_ARG(__VA_ARGS__))); \
    } while (0)

#endif

/*MC
   PetscObjectStateIncrease - Increases the state of any `PetscObject`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectStateIncrease(PetscObject obj)

   Logically Collective

   Input Parameter:
.  obj - any PETSc object, for example a `Vec`, `Mat` or `KSP`. This must be
         cast with a (PetscObject), for example,
         `PetscObjectStateIncrease`((`PetscObject`)mat);

   Notes:
   Object state is a 64 bit integer which gets increased every time
   the object is changed internally. By saving and later querying the object state
   one can determine whether information about the object is still current.
   Currently, state is maintained for `Vec` and `Mat` objects.

   This routine is mostly for internal use by PETSc; a developer need only
   call it after explicit access to an object's internals. Routines such
   as `VecSet()` or `MatScale()` already call this routine. It is also called, as a
   precaution, in `VecRestoreArray()`, `MatRestoreRow()`, `MatDenseRestoreArray()`.

   Routines such as `VecNorm()` can by-pass the computation if the norm has already been computed and the vector's state has not changed.

   This routine is logically collective because state equality comparison needs to be possible without communication.

   `Mat` also has `MatGetNonzeroState()` and `MatSetNonzeroState()` for tracking changes to the nonzero structure.

   Level: developer

.seealso: `PetscObjectStateGet()`, `MatSetNonzeroState()`, `PetscObject`

M*/
#define PetscObjectStateIncrease(obj) ((obj)->state++, 0)

PETSC_EXTERN PetscErrorCode PetscObjectStateGet(PetscObject, PetscObjectState *);
PETSC_EXTERN PetscErrorCode PetscObjectStateSet(PetscObject, PetscObjectState);
PETSC_EXTERN PetscErrorCode PetscObjectComposedDataRegister(PetscInt *);
PETSC_EXTERN PetscErrorCode PetscObjectComposedDataIncreaseInt(PetscObject);
PETSC_EXTERN PetscErrorCode PetscObjectComposedDataIncreaseIntstar(PetscObject);
PETSC_EXTERN PetscErrorCode PetscObjectComposedDataIncreaseReal(PetscObject);
PETSC_EXTERN PetscErrorCode PetscObjectComposedDataIncreaseRealstar(PetscObject);
PETSC_EXTERN PetscErrorCode PetscObjectComposedDataIncreaseScalar(PetscObject);
PETSC_EXTERN PetscErrorCode PetscObjectComposedDataIncreaseScalarstar(PetscObject);
PETSC_EXTERN PetscInt       PetscObjectComposedDataMax;

/*MC
   PetscObjectComposedDataSetInt - attach integer data to a `PetscObject` that may be accessed with `PetscObjectComposedDataGetInt()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataSetInt(PetscObject obj,int id,int data)

   Not collective

   Input parameters:
+  obj - the object to which data is to be attached
.  id - the identifier for the data
-  data - the data to  be attached

   Notes:
   The data identifier can be created through a call to  `PetscObjectComposedDataRegister()`

   This allows the efficient composition of a single integer value with a `PetscObject`. Complex data may be
   attached with `PetscObjectCompose()`

   Level: developer

.seealso: `PetscObjectComposedDataGetInt()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetReal()`,
          `PetscObjectComposedDataGetIntstar()`, `PetscObjectComposedDataSetIntstar()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`
M*/
#define PetscObjectComposedDataSetInt(obj, id, data) ((((obj)->int_idmax < PetscObjectComposedDataMax) && PetscObjectComposedDataIncreaseInt(obj)) || ((obj)->intcomposeddata[id] = data, (obj)->intcomposedstate[id] = (obj)->state, 0))

/*MC
   PetscObjectComposedDataGetInt - retrieve integer data attached to an object with `PetscObjectComposedDataSetInt()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataGetInt(PetscObject obj,int id,int data,PetscBool  flag)

   Not collective

   Input parameters:
+  obj - the object from which data is to be retrieved
-  id - the identifier for the data

   Output parameters:
+  data - the data to be retrieved
-  flag - `PETSC_TRUE` if the data item exists and is valid, `PETSC_FALSE` otherwise

   Level: developer

   Notes:
   The 'data' and 'flag' variables are inlined, so they are not pointers.

   The length of the array accessed must be known.

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetReal()`,
          `PetscObjectComposedDataGetIntstar()`, `PetscObjectComposedDataSetIntstar()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`
M*/
#define PetscObjectComposedDataGetInt(obj, id, data, flag) (((obj)->intcomposedstate ? (data = (obj)->intcomposeddata[id], flag = (PetscBool)((obj)->intcomposedstate[id] == (obj)->state)) : (flag = PETSC_FALSE)), 0)

/*MC
   PetscObjectComposedDataSetIntstar - attach an integer array data to a `PetscObject` that may be accessed with `PetscObjectComposedDataGetIntstar()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataSetIntstar(PetscObject obj,int id,int *data)

   Not collective

   Input parameters:
+  obj - the object to which data is to be attached
.  id - the identifier for the data
-  data - the data to  be attached

   Notes:
   The data identifier can be determined through a call to `PetscObjectComposedDataRegister()`

   The length of the array accessed must be known, it is not available through this API.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetReal()`,
          `PetscObjectComposedDataGetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`
M*/
#define PetscObjectComposedDataSetIntstar(obj, id, data) \
  ((((obj)->intstar_idmax < PetscObjectComposedDataMax) && PetscObjectComposedDataIncreaseIntstar(obj)) || ((obj)->intstarcomposeddata[id] = data, (obj)->intstarcomposedstate[id] = (obj)->state, 0))

/*MC
   PetscObjectComposedDataGetIntstar - retrieve integer array data attached to an object with `PetscObjectComposedDataSetIntstar()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataGetIntstar(PetscObject obj,int id,int *data,PetscBool  flag)

   Not collective

   Input parameters:
+  obj - the object from which data is to be retrieved
-  id - the identifier for the data

   Output parameters:
+  data - the data to be retrieved
-  flag - `PETSC_TRUE` if the data item exists and is valid, `PETSC_FALSE` otherwise

   Notes:
   The 'data' and 'flag' variables are inlined, so they are not pointers.

   The length of the array accessed must be known, it is not available through this API.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetReal()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`
M*/
#define PetscObjectComposedDataGetIntstar(obj, id, data, flag) (((obj)->intstarcomposedstate ? (data = (obj)->intstarcomposeddata[id], flag = (PetscBool)((obj)->intstarcomposedstate[id] == (obj)->state)) : (flag = PETSC_FALSE)), 0)

/*MC
   PetscObjectComposedDataSetReal - attach real data to a `PetscObject` that may be accessed with `PetscObjectComposedDataGetReal()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataSetReal(PetscObject obj,int id,PetscReal data)

   Not collective

   Input parameters:
+  obj - the object to which data is to be attached
.  id - the identifier for the data
-  data - the data to  be attached

   Note:
   The data identifier can be determined through a call to  `PetscObjectComposedDataRegister()`

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`
M*/
#define PetscObjectComposedDataSetReal(obj, id, data) ((((obj)->real_idmax < PetscObjectComposedDataMax) && PetscObjectComposedDataIncreaseReal(obj)) || ((obj)->realcomposeddata[id] = data, (obj)->realcomposedstate[id] = (obj)->state, 0))

/*MC
   PetscObjectComposedDataGetReal - retrieve real data attached to an object set with `PetscObjectComposedDataSetReal()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataGetReal(PetscObject obj,int id,PetscReal data,PetscBool  flag)

   Not collective

   Input parameters:
+  obj - the object from which data is to be retrieved
-  id - the identifier for the data

   Output parameters:
+  data - the data to be retrieved
-  flag - `PETSC_TRUE` if the data item exists and is valid, `PETSC_FALSE` otherwise

   Note:
   The 'data' and 'flag' variables are inlined, so they are not pointers.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataSetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`
M*/
#define PetscObjectComposedDataGetReal(obj, id, data, flag) (((obj)->realcomposedstate ? (data = (obj)->realcomposeddata[id], flag = (PetscBool)((obj)->realcomposedstate[id] == (obj)->state)) : (flag = PETSC_FALSE)), 0)

/*MC
   PetscObjectComposedDataSetRealstar - attach real array data to a `PetscObject` that may be retrieved with `PetscObjectComposedDataGetRealstar()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataSetRealstar(PetscObject obj,int id,PetscReal *data)

   Not collective

   Input parameters:
+  obj - the object to which data is to be attached
.  id - the identifier for the data
-  data - the data to  be attached

   Notes:
   The data identifier can be determined through a call to `PetscObjectComposedDataRegister()`

   The length of the array accessed must be known, it is not available through this API.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataSetReal()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`, `PetscObjectComposedDataGetRealstar()`
M*/
#define PetscObjectComposedDataSetRealstar(obj, id, data) \
  ((((obj)->realstar_idmax < PetscObjectComposedDataMax) && PetscObjectComposedDataIncreaseRealstar(obj)) || ((obj)->realstarcomposeddata[id] = data, (obj)->realstarcomposedstate[id] = (obj)->state, 0))

/*MC
   PetscObjectComposedDataGetRealstar - retrieve real array data attached to an object with `PetscObjectComposedDataSetRealstar()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataGetRealstar(PetscObject obj,int id,PetscReal *data,PetscBool  flag)

   Not collective

   Input parameters:
+  obj - the object from which data is to be retrieved
-  id - the identifier for the data

   Output parameters:
+  data - the data to be retrieved
-  flag - `PETSC_TRUE` if the data item exists and is valid, `PETSC_FALSE` otherwise

   Notes:
   The 'data' and 'flag' variables are inlined, so they are not pointers.

   The length of the array accessed must be known, it is not available through this API.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataSetReal()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`, `PetscObjectComposedDataSetRealstar()`
M*/
#define PetscObjectComposedDataGetRealstar(obj, id, data, flag) (((obj)->realstarcomposedstate ? (data = (obj)->realstarcomposeddata[id], flag = (PetscBool)((obj)->realstarcomposedstate[id] == (obj)->state)) : (flag = PETSC_FALSE)), 0)

/*MC
   PetscObjectComposedDataSetScalar - attach scalar data to a PetscObject that may be retrieved with `PetscObjectComposedDataGetScalar()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataSetScalar(PetscObject obj,int id,PetscScalar data)

   Not collective

   Input parameters:
+  obj - the object to which data is to be attached
.  id - the identifier for the data
-  data - the data to  be attached

   Note:
   The data identifier can be determined through a call to `PetscObjectComposedDataRegister()`

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataSetReal()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`, `PetscObjectComposedDataSetRealstar()`, `PetscObjectComposedDataGetScalar()`
M*/
#if defined(PETSC_USE_COMPLEX)
  #define PetscObjectComposedDataSetScalar(obj, id, data) ((((obj)->scalar_idmax < PetscObjectComposedDataMax) && PetscObjectComposedDataIncreaseScalar(obj)) || ((obj)->scalarcomposeddata[id] = data, (obj)->scalarcomposedstate[id] = (obj)->state, 0))
#else
  #define PetscObjectComposedDataSetScalar(obj, id, data) PetscObjectComposedDataSetReal(obj, id, data)
#endif
/*MC
   PetscObjectComposedDataGetScalar - retrieve scalar data attached to an object that was set with `PetscObjectComposedDataSetScalar()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataGetScalar(PetscObject obj,int id,PetscScalar data,PetscBool  flag)

   Not collective

   Input parameters:
+  obj - the object from which data is to be retrieved
-  id - the identifier for the data

   Output parameters:
+  data - the data to be retrieved
-  flag - `PETSC_TRUE` if the data item exists and is valid, `PETSC_FALSE` otherwise

   Note:
   The 'data' and 'flag' variables are inlined, so they are not pointers.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataSetReal()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`, `PetscObjectComposedDataSetRealstar()`, `PetscObjectComposedDataSetScalar()`
M*/
#if defined(PETSC_USE_COMPLEX)
  #define PetscObjectComposedDataGetScalar(obj, id, data, flag) (((obj)->scalarcomposedstate ? (data = (obj)->scalarcomposeddata[id], flag = (PetscBool)((obj)->scalarcomposedstate[id] == (obj)->state)) : (flag = PETSC_FALSE)), 0)
#else
  #define PetscObjectComposedDataGetScalar(obj, id, data, flag) PetscObjectComposedDataGetReal(obj, id, data, flag)
#endif

/*MC
   PetscObjectComposedDataSetScalarstar - attach scalar array data to a `PetscObject` that may be retrieved with `PetscObjectComposedDataSetScalarstar()`

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataSetScalarstar(PetscObject obj,int id,PetscScalar *data)

   Not collective

   Input parameters:
+  obj - the object to which data is to be attached
.  id - the identifier for the data
-  data - the data to  be attached

   Notes:
   The data identifier can be determined through a call to `PetscObjectComposedDataRegister()`

   The length of the array accessed must be known, it is not available through this API.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataSetReal()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`, `PetscObjectComposedDataSetRealstar()`, `PetscObjectComposedDataGetScalarstar()`
M*/
#if defined(PETSC_USE_COMPLEX)
  #define PetscObjectComposedDataSetScalarstar(obj, id, data) \
    ((((obj)->scalarstar_idmax < PetscObjectComposedDataMax) && PetscObjectComposedDataIncreaseScalarstar(obj)) || ((obj)->scalarstarcomposeddata[id] = data, (obj)->scalarstarcomposedstate[id] = (obj)->state, 0))
#else
  #define PetscObjectComposedDataSetScalarstar(obj, id, data) PetscObjectComposedDataSetRealstar(obj, id, data)
#endif
/*MC
   PetscObjectComposedDataGetScalarstar - retrieve scalar array data set with `PetscObjectComposedDataSetScalarstar()`
   attached to an object

   Synopsis:
   #include "petsc/private/petscimpl.h"
   PetscErrorCode PetscObjectComposedDataGetScalarstar(PetscObject obj,int id,PetscScalar *data,PetscBool  flag)

   Not collective

   Input parameters:
+  obj - the object from which data is to be retrieved
-  id - the identifier for the data

   Output parameters:
+  data - the data to be retrieved
-  flag - `PETSC_TRUE` if the data item exists and is valid, `PETSC_FALSE` otherwise

   Notes:
   The 'data' and 'flag' variables are inlined, so they are not pointers.

   The length of the array accessed must be known, it is not available through this API.

   Level: developer

.seealso: `PetscObjectComposedDataSetInt()`, `PetscObjectComposedDataSetReal()`, `PetscObjectComposedDataGetReal()`, `PetscObjectComposedDataSetIntstar()`,
          `PetscObjectComposedDataSetIntstar()`, `PetscObjectComposedDataGetInt()`, `PetscObject`,
          `PetscObjectCompose()`, `PetscObjectQuery()`, `PetscObjectComposedDataSetRealstar()`, `PetscObjectComposedDataSetScalarstar()`
M*/
#if defined(PETSC_USE_COMPLEX)
  #define PetscObjectComposedDataGetScalarstar(obj, id, data, flag) (((obj)->scalarstarcomposedstate ? (data = (obj)->scalarstarcomposeddata[id], flag = (PetscBool)((obj)->scalarstarcomposedstate[id] == (obj)->state)) : (flag = PETSC_FALSE)), 0)
#else
  #define PetscObjectComposedDataGetScalarstar(obj, id, data, flag) PetscObjectComposedDataGetRealstar(obj, id, data, flag)
#endif

PETSC_EXTERN PetscMPIInt Petsc_Counter_keyval;
PETSC_EXTERN PetscMPIInt Petsc_InnerComm_keyval;
PETSC_EXTERN PetscMPIInt Petsc_OuterComm_keyval;
PETSC_EXTERN PetscMPIInt Petsc_Seq_keyval;
PETSC_EXTERN PetscMPIInt Petsc_ShmComm_keyval;
PETSC_EXTERN PetscMPIInt Petsc_CreationIdx_keyval;
PETSC_EXTERN PetscMPIInt Petsc_Garbage_HMap_keyval;

struct PetscCommStash {
  struct PetscCommStash *next;
  MPI_Comm               comm;
};

/*
  PETSc communicators have this attribute, see
  PetscCommDuplicate(), PetscCommDestroy(), PetscCommGetNewTag(), PetscObjectGetName()
*/
typedef struct {
  PetscMPIInt            tag;       /* next free tag value */
  PetscInt               refcount;  /* number of references, communicator can be freed when this reaches 0 */
  PetscInt               namecount; /* used to generate the next name, as in Vec_0, Mat_1, ... */
  PetscMPIInt           *iflags;    /* length of comm size, shared by all calls to PetscCommBuildTwoSided_Allreduce/RedScatter on this comm */
  struct PetscCommStash *comms;     /* communicators available for PETSc to pass off to other packages */
} PetscCommCounter;

typedef enum {
  STATE_BEGIN,
  STATE_PENDING,
  STATE_END
} SRState;

typedef enum {
  PETSC_SR_REDUCE_SUM = 0,
  PETSC_SR_REDUCE_MAX = 1,
  PETSC_SR_REDUCE_MIN = 2
} PetscSRReductionType;

typedef struct {
  MPI_Comm     comm;
  MPI_Request  request;
  PetscBool    mix;
  PetscBool    async;
  PetscScalar *lvalues;    /* this are the reduced values before call to MPI_Allreduce() */
  PetscScalar *gvalues;    /* values after call to MPI_Allreduce() */
  void       **invecs;     /* for debugging only, vector/memory used with each op */
  PetscInt    *reducetype; /* is particular value to be summed or maxed? */
  struct {
    PetscScalar v;
    PetscInt    i;
  }       *lvalues_mix, *gvalues_mix; /* used when mixing reduce operations */
  SRState  state;                     /* are we calling xxxBegin() or xxxEnd()? */
  PetscInt maxops;                    /* total amount of space we have for requests */
  PetscInt numopsbegin;               /* number of requests that have been queued in */
  PetscInt numopsend;                 /* number of requests that have been gotten by user */
} PetscSplitReduction;

PETSC_EXTERN PetscErrorCode PetscSplitReductionGet(MPI_Comm, PetscSplitReduction **);
PETSC_EXTERN PetscErrorCode PetscSplitReductionEnd(PetscSplitReduction *);
PETSC_EXTERN PetscErrorCode PetscSplitReductionExtend(PetscSplitReduction *);

#if !defined(PETSC_SKIP_SPINLOCK)
  #if defined(PETSC_HAVE_THREADSAFETY)
    #if defined(PETSC_HAVE_CONCURRENCYKIT)
      #if defined(__cplusplus)
/*  CK does not have extern "C" protection in their include files */
extern "C" {
      #endif
      #include <ck_spinlock.h>
      #if defined(__cplusplus)
}
      #endif
typedef ck_spinlock_t        PetscSpinlock;
static inline PetscErrorCode PetscSpinlockCreate(PetscSpinlock *ck_spinlock)
{
  ck_spinlock_init(ck_spinlock);
  return 0;
}
static inline PetscErrorCode PetscSpinlockLock(PetscSpinlock *ck_spinlock)
{
  ck_spinlock_lock(ck_spinlock);
  return 0;
}
static inline PetscErrorCode PetscSpinlockUnlock(PetscSpinlock *ck_spinlock)
{
  ck_spinlock_unlock(ck_spinlock);
  return 0;
}
static inline PetscErrorCode PetscSpinlockDestroy(PetscSpinlock *ck_spinlock)
{
  return 0;
}
    #elif defined(PETSC_HAVE_OPENMP)

      #include <omp.h>
typedef omp_lock_t           PetscSpinlock;
static inline PetscErrorCode PetscSpinlockCreate(PetscSpinlock *omp_lock)
{
  omp_init_lock(omp_lock);
  return 0;
}
static inline PetscErrorCode PetscSpinlockLock(PetscSpinlock *omp_lock)
{
  omp_set_lock(omp_lock);
  return 0;
}
static inline PetscErrorCode PetscSpinlockUnlock(PetscSpinlock *omp_lock)
{
  omp_unset_lock(omp_lock);
  return 0;
}
static inline PetscErrorCode PetscSpinlockDestroy(PetscSpinlock *omp_lock)
{
  omp_destroy_lock(omp_lock);
  return 0;
}
    #else
      #error "Thread safety requires either --with-openmp or --download-concurrencykit"
    #endif

  #else
typedef int PetscSpinlock;
    #define PetscSpinlockCreate(a)  0
    #define PetscSpinlockLock(a)    0
    #define PetscSpinlockUnlock(a)  0
    #define PetscSpinlockDestroy(a) 0
  #endif

  #if defined(PETSC_HAVE_THREADSAFETY)
PETSC_INTERN PetscSpinlock PetscViewerASCIISpinLockOpen;
PETSC_INTERN PetscSpinlock PetscViewerASCIISpinLockStdout;
PETSC_INTERN PetscSpinlock PetscViewerASCIISpinLockStderr;
PETSC_INTERN PetscSpinlock PetscCommSpinLock;
  #endif
#endif

PETSC_EXTERN PetscLogEvent PETSC_Barrier;
PETSC_EXTERN PetscLogEvent PETSC_BuildTwoSided;
PETSC_EXTERN PetscLogEvent PETSC_BuildTwoSidedF;
PETSC_EXTERN PetscBool     use_gpu_aware_mpi;
PETSC_EXTERN PetscBool     PetscPrintFunctionList;

#if defined(PETSC_HAVE_ADIOS)
PETSC_EXTERN int64_t Petsc_adios_group;
#endif

#if defined(PETSC_HAVE_KOKKOS)
PETSC_INTERN PetscBool      PetscBeganKokkos;
PETSC_EXTERN PetscBool      PetscKokkosInitialized;
PETSC_INTERN PetscErrorCode PetscKokkosIsInitialized_Private(PetscBool *);
PETSC_INTERN PetscErrorCode PetscKokkosFinalize_Private(void);
#endif

#if defined(PETSC_HAVE_OPENMP)
PETSC_EXTERN PetscInt PetscNumOMPThreads;
#endif

#endif /* PETSCIMPL_H */
