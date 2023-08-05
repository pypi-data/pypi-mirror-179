
#requiresdefine   'PETSC_HAVE_FORTRAN'
ALL: lib
CPPFLAGS = ${NETCFD_INCLUDE} ${EXODUSII_INCLUDE}
CFLAGS   =
FFLAGS   =
SOURCEC  = plexdistributef.c plexgeometryf.c plexinterpolatef.c plexmetricf.c plexreorderf.c plexf.c plexcgnsf.c plexcheckinterfacef.c plexcreatef.c plexegadsf.c plexexodusiif.c plexfemf.c plexfvmf.c plexgmshf.c plexindicesf.c plexnaturalf.c plexorientf.c plexpartitionf.c plexpointf.c plexprojectf.c plexrefinef.c plexsubmeshf.c plextreef.c
SOURCEF  =
SOURCEH  = 
DIRS     =
LIBBASE  = libpetscdm
LOCDIR   = src/dm/impls/plex/ftn-auto/
include ${PETSC_DIR}/lib/petsc/conf/variables
include ${PETSC_DIR}/lib/petsc/conf/rules
include ${PETSC_DIR}/lib/petsc/conf/test
