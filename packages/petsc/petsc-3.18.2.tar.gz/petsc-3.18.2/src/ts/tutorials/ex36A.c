
static char help[] = "Transistor amplifier (autonomous).\n";

/*F
  M y'=f(y)

  Useful options: -ts_monitor_lg_solution -ts_monitor_lg_timestep -lg_indicate_data_points 0
F*/

/*
   Include "petscts.h" so that we can use TS solvers.  Note that this
   file automatically includes:
     petscsys.h       - base PETSc routines   petscvec.h - vectors
     petscmat.h - matrices
     petscis.h     - index sets            petscksp.h - Krylov subspace methods
     petscviewer.h - viewers               petscpc.h  - preconditioners
     petscksp.h   - linear solvers
*/
#include <petscts.h>

FILE *gfilepointer_data, *gfilepointer_info;

/* Defines the source  */
PetscErrorCode Ue(PetscScalar t, PetscScalar *U)
{
  PetscFunctionBeginUser;
  U = 0.4 * sin(200 * pi * t);
  PetscFunctionReturn(0);
}
* /

  /*
     Defines the DAE passed to the time solver
*/
  static PetscErrorCode IFunctionImplicit(TS ts, PetscReal t, Vec Y, Vec Ydot, Vec F, void *ctx)
{
  const PetscScalar *y, *ydot;
  PetscScalar       *f;

  PetscFunctionBeginUser;
  /*  The next three lines allow us to access the entries of the vectors directly */
  PetscCall(VecGetArrayRead(Y, &y));
  PetscCall(VecGetArrayRead(Ydot, &ydot));
  PetscCall(VecGetArray(F, &f));

  f[0] = PetscSinReal(200 * PETSC_PI * y[5]) / 2500. - y[0] / 1000. - ydot[0] / 1.e6 + ydot[1] / 1.e6;
  f[1] = 0.0006666766666666667 - PetscExpReal((500 * (y[1] - y[2])) / 13.) / 1.e8 - y[1] / 4500. + ydot[0] / 1.e6 - ydot[1] / 1.e6;
  f[2] = -1.e-6 + PetscExpReal((500 * (y[1] - y[2])) / 13.) / 1.e6 - y[2] / 9000. - ydot[2] / 500000.;
  f[3] = 0.0006676566666666666 - (99 * PetscExpReal((500 * (y[1] - y[2])) / 13.)) / 1.e8 - y[3] / 9000. - (3 * ydot[3]) / 1.e6 + (3 * ydot[4]) / 1.e6;
  f[4] = -y[4] / 9000. + (3 * ydot[3]) / 1.e6 - (3 * ydot[4]) / 1.e6;
  f[5] = -1 + ydot[5];

  PetscCall(VecRestoreArrayRead(Y, &y));
  PetscCall(VecRestoreArrayRead(Ydot, &ydot));
  PetscCall(VecRestoreArray(F, &f));
  PetscFunctionReturn(0);
}

/*
     Defines the Jacobian of the ODE passed to the ODE solver. See TSSetIJacobian() for the meaning of a and the Jacobian.
*/
static PetscErrorCode IJacobianImplicit(TS ts, PetscReal t, Vec Y, Vec Ydot, PetscReal a, Mat A, Mat B, void *ctx)
{
  PetscInt           rowcol[] = {0, 1, 2, 3, 4, 5};
  const PetscScalar *y, *ydot;
  PetscScalar        J[6][6];

  PetscFunctionBeginUser;
  PetscCall(VecGetArrayRead(Y, &y));
  PetscCall(VecGetArrayRead(Ydot, &ydot));

  PetscCall(PetscMemzero(J, sizeof(J)));

  J[0][0] = -0.001 - a / 1.e6;
  J[0][1] = a / 1.e6;
  J[0][5] = (2 * PETSC_PI * PetscCosReal(200 * PETSC_PI * y[5])) / 25.;
  J[1][0] = a / 1.e6;
  J[1][1] = -0.00022222222222222223 - a / 1.e6 - PetscExpReal((500 * (y[1] - y[2])) / 13.) / 2.6e6;
  J[1][2] = PetscExpReal((500 * (y[1] - y[2])) / 13.) / 2.6e6;
  J[2][1] = PetscExpReal((500 * (y[1] - y[2])) / 13.) / 26000.;
  J[2][2] = -0.00011111111111111112 - a / 500000. - PetscExpReal((500 * (y[1] - y[2])) / 13.) / 26000.;
  J[3][1] = (-99 * PetscExpReal((500 * (y[1] - y[2])) / 13.)) / 2.6e6;
  J[3][2] = (99 * PetscExpReal((500 * (y[1] - y[2])) / 13.)) / 2.6e6;
  J[3][3] = -0.00011111111111111112 - (3 * a) / 1.e6;
  J[3][4] = (3 * a) / 1.e6;
  J[4][3] = (3 * a) / 1.e6;
  J[4][4] = -0.00011111111111111112 - (3 * a) / 1.e6;
  J[5][5] = a;

  PetscCall(MatSetValues(B, 6, rowcol, 6, rowcol, &J[0][0], INSERT_VALUES));

  PetscCall(VecRestoreArrayRead(Y, &y));
  PetscCall(VecRestoreArrayRead(Ydot, &ydot));

  PetscCall(MatAssemblyBegin(A, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(A, MAT_FINAL_ASSEMBLY));
  if (A != B) {
    PetscCall(MatAssemblyBegin(B, MAT_FINAL_ASSEMBLY));
    PetscCall(MatAssemblyEnd(B, MAT_FINAL_ASSEMBLY));
  }
  PetscFunctionReturn(0);
}

int main(int argc, char **argv)
{
  TS           ts; /* ODE integrator */
  Vec          Y;  /* solution will be stored here */
  Mat          A;  /* Jacobian matrix */
  PetscMPIInt  size;
  PetscInt     n = 6;
  PetscScalar *y;

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Initialize program
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, (char *)0, help));
  PetscCallMPI(MPI_Comm_size(PETSC_COMM_WORLD, &size));
  PetscCheck(size == 1, PETSC_COMM_WORLD, PETSC_ERR_WRONG_MPI_SIZE, "Only for sequential runs");

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Create necessary matrix and vectors
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(MatCreate(PETSC_COMM_WORLD, &A));
  PetscCall(MatSetSizes(A, n, n, PETSC_DETERMINE, PETSC_DETERMINE));
  PetscCall(MatSetFromOptions(A));
  PetscCall(MatSetUp(A));

  PetscCall(MatCreateVecs(A, &Y, NULL));

  PetscCall(VecGetArray(Y, &y));
  y[0] = 0.0;
  y[1] = 3.0;
  y[2] = y[1];
  y[3] = 6.0;
  y[4] = 0.0;
  y[5] = 0.0;
  PetscCall(VecRestoreArray(Y, &y));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create timestepping solver context
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(TSCreate(PETSC_COMM_WORLD, &ts));
  PetscCall(TSSetProblemType(ts, TS_NONLINEAR));
  PetscCall(TSSetType(ts, TSARKIMEX));
  PetscCall(TSSetEquationType(ts, TS_EQ_DAE_IMPLICIT_INDEX1));
  PetscCall(TSARKIMEXSetFullyImplicit(ts, PETSC_TRUE));
  /*PetscCall(TSSetType(ts,TSROSW));*/
  PetscCall(TSSetIFunction(ts, NULL, IFunctionImplicit, NULL));
  PetscCall(TSSetIJacobian(ts, A, A, IJacobianImplicit, NULL));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Set initial conditions
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(TSSetSolution(ts, Y));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Set solver options
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(TSSetMaxTime(ts, 0.15));
  PetscCall(TSSetExactFinalTime(ts, TS_EXACTFINALTIME_STEPOVER));
  PetscCall(TSSetTimeStep(ts, .001));
  PetscCall(TSSetFromOptions(ts));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Do Time stepping
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(TSSolve(ts, Y));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Free work space.  All PETSc objects should be destroyed when they are no longer needed.
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(MatDestroy(&A));
  PetscCall(VecDestroy(&Y));
  PetscCall(TSDestroy(&ts));
  PetscCall(PetscFinalize());
  return 0;
}
