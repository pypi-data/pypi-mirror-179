static char help[] = "DMStag slot test (to excerpt for manual)\n\n";

#include <petscdmstag.h>

int main(int argc, char **argv)
{
  DM              dm;
  Vec             x;
  PetscInt        start_x, start_y, start_z, n_x, n_y, n_z, n_extra_x, n_extra_y, n_extra_z, slot_vertex_2;
  PetscScalar ****x_array;

  const DMStagStencilLocation location_vertex = DMSTAG_BACK_DOWN_LEFT;
  const PetscInt              dof0 = 2, dof1 = 2, dof2 = 2, dof3 = 2, N_x = 3, N_y = 3, N_z = 3;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, (char *)0, help));

  PetscCall(DMStagCreate3d(PETSC_COMM_WORLD, DM_BOUNDARY_NONE, DM_BOUNDARY_NONE, DM_BOUNDARY_NONE, N_x, N_y, N_z, PETSC_DECIDE, PETSC_DECIDE, PETSC_DECIDE, dof0, dof1, dof2, dof3, DMSTAG_STENCIL_BOX, 1, NULL, NULL, NULL, &dm));
  PetscCall(DMSetFromOptions(dm));
  PetscCall(DMSetUp(dm));

  PetscCall(DMCreateLocalVector(dm, &x));
  PetscCall(VecZeroEntries(x));

  /* Set the second component of all vertex dof to 2.0 */
  PetscCall(DMStagGetCorners(dm, &start_x, &start_y, &start_z, &n_x, &n_y, &n_z, &n_extra_x, &n_extra_y, &n_extra_z));
  PetscCall(DMStagGetLocationSlot(dm, location_vertex, 1, &slot_vertex_2));
  PetscCall(DMStagVecGetArray(dm, x, &x_array));
  for (PetscInt k = start_z; k < start_z + n_z + n_extra_z; ++k) {
    for (PetscInt j = start_y; j < start_y + n_y + n_extra_y; ++j) {
      for (PetscInt i = start_x; i < start_x + n_x + n_extra_x; ++i) x_array[k][j][i][slot_vertex_2] = 2.0;
    }
  }
  PetscCall(DMStagVecRestoreArray(dm, x, &x_array));
  PetscCall(VecDestroy(&x));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscFinalize());
  return 0;
}

/*TEST

   test:

TEST*/
