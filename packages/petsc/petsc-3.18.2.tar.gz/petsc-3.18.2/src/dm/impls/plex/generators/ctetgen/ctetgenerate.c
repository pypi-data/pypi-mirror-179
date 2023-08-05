#include <petsc/private/dmpleximpl.h> /*I      "petscdmplex.h"   I*/

#ifdef PETSC_HAVE_EGADS
  #include <egads.h>
#endif

#include <ctetgen.h>

/* This is to fix the tetrahedron orientation from TetGen */
static PetscErrorCode DMPlexInvertCells_CTetgen(PetscInt numCells, PetscInt numCorners, PetscInt cells[])
{
  PetscInt bound = numCells * numCorners, coff;

  PetscFunctionBegin;
#define SWAP(a, b) \
  do { \
    PetscInt tmp = (a); \
    (a)          = (b); \
    (b)          = tmp; \
  } while (0)
  for (coff = 0; coff < bound; coff += numCorners) SWAP(cells[coff], cells[coff + 1]);
#undef SWAP
  PetscFunctionReturn(0);
}

PETSC_EXTERN PetscErrorCode DMPlexGenerate_CTetgen(DM boundary, PetscBool interpolate, DM *dm)
{
  MPI_Comm               comm;
  const PetscInt         dim = 3;
  PLC                   *in, *out;
  DMUniversalLabel       universal;
  PetscInt               vStart, vEnd, v, eStart, eEnd, e, fStart, fEnd, f, defVal, verbose = 0;
  DMPlexInterpolatedFlag isInterpolated;
  PetscMPIInt            rank;

  PetscFunctionBegin;
  PetscCall(PetscOptionsGetInt(NULL, ((PetscObject)boundary)->prefix, "-ctetgen_verbose", &verbose, NULL));
  PetscCall(PetscObjectGetComm((PetscObject)boundary, &comm));
  PetscCallMPI(MPI_Comm_rank(comm, &rank));
  PetscCall(DMPlexIsInterpolatedCollective(boundary, &isInterpolated));
  PetscCall(DMUniversalLabelCreate(boundary, &universal));
  PetscCall(DMLabelGetDefaultValue(universal->label, &defVal));

  PetscCall(PLCCreate(&in));
  PetscCall(PLCCreate(&out));

  PetscCall(DMPlexGetDepthStratum(boundary, 0, &vStart, &vEnd));
  in->numberofpoints = vEnd - vStart;
  if (in->numberofpoints > 0) {
    PetscSection       coordSection;
    Vec                coordinates;
    const PetscScalar *array;

    PetscCall(PetscMalloc1(in->numberofpoints * dim, &in->pointlist));
    PetscCall(PetscCalloc1(in->numberofpoints, &in->pointmarkerlist));
    PetscCall(DMGetCoordinatesLocal(boundary, &coordinates));
    PetscCall(DMGetCoordinateSection(boundary, &coordSection));
    PetscCall(VecGetArrayRead(coordinates, &array));
    for (v = vStart; v < vEnd; ++v) {
      const PetscInt idx = v - vStart;
      PetscInt       off, d, m;

      PetscCall(PetscSectionGetOffset(coordSection, v, &off));
      for (d = 0; d < dim; ++d) in->pointlist[idx * dim + d] = PetscRealPart(array[off + d]);
      PetscCall(DMLabelGetValue(universal->label, v, &m));
      if (m != defVal) in->pointmarkerlist[idx] = (int)m;
    }
    PetscCall(VecRestoreArrayRead(coordinates, &array));
  }

  PetscCall(DMPlexGetHeightStratum(boundary, 1, &eStart, &eEnd));
  in->numberofedges = eEnd - eStart;
  if (isInterpolated == DMPLEX_INTERPOLATED_FULL && in->numberofedges > 0) {
    PetscCall(PetscMalloc1(in->numberofedges * 2, &in->edgelist));
    PetscCall(PetscMalloc1(in->numberofedges, &in->edgemarkerlist));
    for (e = eStart; e < eEnd; ++e) {
      const PetscInt  idx = e - eStart;
      const PetscInt *cone;
      PetscInt        coneSize, val;

      PetscCall(DMPlexGetConeSize(boundary, e, &coneSize));
      PetscCall(DMPlexGetCone(boundary, e, &cone));
      in->edgelist[idx * 2]     = cone[0] - vStart;
      in->edgelist[idx * 2 + 1] = cone[1] - vStart;

      PetscCall(DMLabelGetValue(universal->label, e, &val));
      if (val != defVal) in->edgemarkerlist[idx] = (int)val;
    }
  }

  PetscCall(DMPlexGetHeightStratum(boundary, 0, &fStart, &fEnd));
  in->numberoffacets = fEnd - fStart;
  if (in->numberoffacets > 0) {
    PetscCall(PetscMalloc1(in->numberoffacets, &in->facetlist));
    PetscCall(PetscMalloc1(in->numberoffacets, &in->facetmarkerlist));
    for (f = fStart; f < fEnd; ++f) {
      const PetscInt idx    = f - fStart;
      PetscInt      *points = NULL, numPoints, p, numVertices = 0, v, m = -1;
      polygon       *poly;

      in->facetlist[idx].numberofpolygons = 1;
      PetscCall(PetscMalloc1(in->facetlist[idx].numberofpolygons, &in->facetlist[idx].polygonlist));
      in->facetlist[idx].numberofholes = 0;
      in->facetlist[idx].holelist      = NULL;

      PetscCall(DMPlexGetTransitiveClosure(boundary, f, PETSC_TRUE, &numPoints, &points));
      for (p = 0; p < numPoints * 2; p += 2) {
        const PetscInt point = points[p];
        if ((point >= vStart) && (point < vEnd)) points[numVertices++] = point;
      }

      poly                   = in->facetlist[idx].polygonlist;
      poly->numberofvertices = numVertices;
      PetscCall(PetscMalloc1(poly->numberofvertices, &poly->vertexlist));
      for (v = 0; v < numVertices; ++v) {
        const PetscInt vIdx = points[v] - vStart;
        poly->vertexlist[v] = vIdx;
      }
      PetscCall(DMLabelGetValue(universal->label, f, &m));
      if (m != defVal) in->facetmarkerlist[idx] = (int)m;
      PetscCall(DMPlexRestoreTransitiveClosure(boundary, f, PETSC_TRUE, &numPoints, &points));
    }
  }
  if (rank == 0) {
    TetGenOpts t;

    PetscCall(TetGenOptsInitialize(&t));
    t.in        = boundary; /* Should go away */
    t.plc       = 1;
    t.quality   = 1;
    t.edgesout  = 1;
    t.zeroindex = 1;
    t.quiet     = 1;
    t.verbose   = verbose;
#if 0
  #ifdef PETSC_HAVE_EGADS
    /* Need to add in more TetGen code */
    t.nobisect  = 1; /* Add Y to preserve Surface Mesh for EGADS */
  #endif
#endif

    PetscCall(TetGenCheckOpts(&t));
    PetscCall(TetGenTetrahedralize(&t, in, out));
  }
  {
    const PetscInt numCorners  = 4;
    const PetscInt numCells    = out->numberoftetrahedra;
    const PetscInt numVertices = out->numberofpoints;
    PetscReal     *meshCoords  = NULL;
    PetscInt      *cells       = NULL;

    if (sizeof(PetscReal) == sizeof(out->pointlist[0])) {
      meshCoords = (PetscReal *)out->pointlist;
    } else {
      PetscInt i;

      PetscCall(PetscMalloc1(dim * numVertices, &meshCoords));
      for (i = 0; i < dim * numVertices; ++i) meshCoords[i] = (PetscReal)out->pointlist[i];
    }
    if (sizeof(PetscInt) == sizeof(out->tetrahedronlist[0])) {
      cells = (PetscInt *)out->tetrahedronlist;
    } else {
      PetscInt i;

      PetscCall(PetscMalloc1(numCells * numCorners, &cells));
      for (i = 0; i < numCells * numCorners; i++) cells[i] = (PetscInt)out->tetrahedronlist[i];
    }

    PetscCall(DMPlexInvertCells_CTetgen(numCells, numCorners, cells));
    PetscCall(DMPlexCreateFromCellListPetsc(comm, dim, numCells, numVertices, numCorners, interpolate, cells, dim, meshCoords, dm));
    if (sizeof(PetscReal) != sizeof(out->pointlist[0])) PetscCall(PetscFree(meshCoords));
    if (sizeof(PetscInt) != sizeof(out->tetrahedronlist[0])) PetscCall(PetscFree(cells));

    /* Set labels */
    PetscCall(DMUniversalLabelCreateLabels(universal, PETSC_TRUE, *dm));
    for (v = 0; v < numVertices; ++v) {
      if (out->pointmarkerlist[v]) PetscCall(DMUniversalLabelSetLabelValue(universal, *dm, PETSC_TRUE, v + numCells, out->pointmarkerlist[v]));
    }
    if (interpolate) {
      PetscInt e;

      for (e = 0; e < out->numberofedges; e++) {
        if (out->edgemarkerlist[e]) {
          const PetscInt  vertices[2] = {out->edgelist[e * 2 + 0] + numCells, out->edgelist[e * 2 + 1] + numCells};
          const PetscInt *edges;
          PetscInt        numEdges;

          PetscCall(DMPlexGetJoin(*dm, 2, vertices, &numEdges, &edges));
          PetscCheck(numEdges == 1, PETSC_COMM_SELF, PETSC_ERR_PLIB, "Two vertices must cover only one edge, not %" PetscInt_FMT, numEdges);
          PetscCall(DMUniversalLabelSetLabelValue(universal, *dm, PETSC_TRUE, edges[0], out->edgemarkerlist[e]));
          PetscCall(DMPlexRestoreJoin(*dm, 2, vertices, &numEdges, &edges));
        }
      }
      for (f = 0; f < out->numberoftrifaces; f++) {
        if (out->trifacemarkerlist[f]) {
          const PetscInt  vertices[3] = {out->trifacelist[f * 3 + 0] + numCells, out->trifacelist[f * 3 + 1] + numCells, out->trifacelist[f * 3 + 2] + numCells};
          const PetscInt *faces;
          PetscInt        numFaces;

          PetscCall(DMPlexGetFullJoin(*dm, 3, vertices, &numFaces, &faces));
          PetscCheck(numFaces == 1, PETSC_COMM_SELF, PETSC_ERR_PLIB, "Three vertices must cover only one face, not %" PetscInt_FMT, numFaces);
          PetscCall(DMUniversalLabelSetLabelValue(universal, *dm, PETSC_TRUE, faces[0], out->trifacemarkerlist[f]));
          PetscCall(DMPlexRestoreJoin(*dm, 3, vertices, &numFaces, &faces));
        }
      }
    }

#ifdef PETSC_HAVE_EGADS
    {
      DMLabel        bodyLabel;
      PetscContainer modelObj;
      PetscInt       cStart, cEnd, c, eStart, eEnd, fStart, fEnd;
      ego           *bodies;
      ego            model, geom;
      int            Nb, oclass, mtype, *senses;

      /* Get Attached EGADS Model from Original DMPlex */
      PetscCall(PetscObjectQuery((PetscObject)boundary, "EGADS Model", (PetscObject *)&modelObj));
      if (modelObj) {
        PetscCall(PetscContainerGetPointer(modelObj, (void **)&model));
        PetscCall(EG_getTopology(model, &geom, &oclass, &mtype, NULL, &Nb, &bodies, &senses));
        /* Transfer EGADS Model to Volumetric Mesh */
        PetscCall(PetscObjectCompose((PetscObject)*dm, "EGADS Model", (PetscObject)modelObj));

        /* Set Cell Labels */
        PetscCall(DMGetLabel(*dm, "EGADS Body ID", &bodyLabel));
        PetscCall(DMPlexGetHeightStratum(*dm, 0, &cStart, &cEnd));
        PetscCall(DMPlexGetHeightStratum(*dm, 1, &fStart, &fEnd));
        PetscCall(DMPlexGetDepthStratum(*dm, 1, &eStart, &eEnd));

        for (c = cStart; c < cEnd; ++c) {
          PetscReal centroid[3] = {0., 0., 0.};
          PetscInt  b;

          /* Deterimine what body the cell's centroid is located in */
          if (!interpolate) {
            PetscSection coordSection;
            Vec          coordinates;
            PetscScalar *coords = NULL;
            PetscInt     coordSize, s, d;

            PetscCall(DMGetCoordinatesLocal(*dm, &coordinates));
            PetscCall(DMGetCoordinateSection(*dm, &coordSection));
            PetscCall(DMPlexVecGetClosure(*dm, coordSection, coordinates, c, &coordSize, &coords));
            for (s = 0; s < coordSize; ++s)
              for (d = 0; d < dim; ++d) centroid[d] += coords[s * dim + d];
            PetscCall(DMPlexVecRestoreClosure(*dm, coordSection, coordinates, c, &coordSize, &coords));
          } else PetscCall(DMPlexComputeCellGeometryFVM(*dm, c, NULL, centroid, NULL));
          for (b = 0; b < Nb; ++b) {
            if (EG_inTopology(bodies[b], centroid) == EGADS_SUCCESS) break;
          }
          if (b < Nb) {
            PetscInt  cval    = b, eVal, fVal;
            PetscInt *closure = NULL, Ncl, cl;

            PetscCall(DMLabelSetValue(bodyLabel, c, cval));
            PetscCall(DMPlexGetTransitiveClosure(*dm, c, PETSC_TRUE, &Ncl, &closure));
            for (cl = 0; cl < Ncl; ++cl) {
              const PetscInt p = closure[cl * 2];

              if (p >= eStart && p < eEnd) {
                PetscCall(DMLabelGetValue(bodyLabel, p, &eVal));
                if (eVal < 0) PetscCall(DMLabelSetValue(bodyLabel, p, cval));
              }
              if (p >= fStart && p < fEnd) {
                PetscCall(DMLabelGetValue(bodyLabel, p, &fVal));
                if (fVal < 0) PetscCall(DMLabelSetValue(bodyLabel, p, cval));
              }
            }
            PetscCall(DMPlexRestoreTransitiveClosure(*dm, c, PETSC_TRUE, &Ncl, &closure));
          }
        }
      }
    }
#endif
    PetscCall(DMPlexSetRefinementUniform(*dm, PETSC_FALSE));
  }

  PetscCall(DMUniversalLabelDestroy(&universal));
  PetscCall(PLCDestroy(&in));
  PetscCall(PLCDestroy(&out));
  PetscFunctionReturn(0);
}

PETSC_EXTERN PetscErrorCode DMPlexRefine_CTetgen(DM dm, PetscReal *maxVolumes, DM *dmRefined)
{
  MPI_Comm               comm;
  const PetscInt         dim = 3;
  PLC                   *in, *out;
  DMUniversalLabel       universal;
  PetscInt               vStart, vEnd, v, eStart, eEnd, e, fStart, fEnd, f, cStart, cEnd, c, defVal, verbose = 0;
  DMPlexInterpolatedFlag isInterpolated;
  PetscMPIInt            rank;

  PetscFunctionBegin;
  PetscCall(PetscOptionsGetInt(NULL, ((PetscObject)dm)->prefix, "-ctetgen_verbose", &verbose, NULL));
  PetscCall(PetscObjectGetComm((PetscObject)dm, &comm));
  PetscCallMPI(MPI_Comm_rank(comm, &rank));
  PetscCall(DMPlexIsInterpolatedCollective(dm, &isInterpolated));
  PetscCall(DMUniversalLabelCreate(dm, &universal));
  PetscCall(DMLabelGetDefaultValue(universal->label, &defVal));

  PetscCall(PLCCreate(&in));
  PetscCall(PLCCreate(&out));

  PetscCall(DMPlexGetDepthStratum(dm, 0, &vStart, &vEnd));
  in->numberofpoints = vEnd - vStart;
  if (in->numberofpoints > 0) {
    PetscSection coordSection;
    Vec          coordinates;
    PetscScalar *array;

    PetscCall(PetscMalloc1(in->numberofpoints * dim, &in->pointlist));
    PetscCall(PetscCalloc1(in->numberofpoints, &in->pointmarkerlist));
    PetscCall(DMGetCoordinatesLocal(dm, &coordinates));
    PetscCall(DMGetCoordinateSection(dm, &coordSection));
    PetscCall(VecGetArray(coordinates, &array));
    for (v = vStart; v < vEnd; ++v) {
      const PetscInt idx = v - vStart;
      PetscInt       off, d, m;

      PetscCall(PetscSectionGetOffset(coordSection, v, &off));
      for (d = 0; d < dim; ++d) in->pointlist[idx * dim + d] = PetscRealPart(array[off + d]);
      PetscCall(DMLabelGetValue(universal->label, v, &m));
      if (m != defVal) in->pointmarkerlist[idx] = (int)m;
    }
    PetscCall(VecRestoreArray(coordinates, &array));
  }

  PetscCall(DMPlexGetDepthStratum(dm, 1, &eStart, &eEnd));
  in->numberofedges = eEnd - eStart;
  if (isInterpolated == DMPLEX_INTERPOLATED_FULL && in->numberofedges > 0) {
    PetscCall(PetscMalloc1(in->numberofedges * 2, &in->edgelist));
    PetscCall(PetscMalloc1(in->numberofedges, &in->edgemarkerlist));
    for (e = eStart; e < eEnd; ++e) {
      const PetscInt  idx = e - eStart;
      const PetscInt *cone;
      PetscInt        coneSize, val;

      PetscCall(DMPlexGetConeSize(dm, e, &coneSize));
      PetscCall(DMPlexGetCone(dm, e, &cone));
      in->edgelist[idx * 2]     = cone[0] - vStart;
      in->edgelist[idx * 2 + 1] = cone[1] - vStart;

      PetscCall(DMLabelGetValue(universal->label, e, &val));
      if (val != defVal) in->edgemarkerlist[idx] = (int)val;
    }
  }

  PetscCall(DMPlexGetHeightStratum(dm, 1, &fStart, &fEnd));
  in->numberoftrifaces = 0;
  for (f = fStart; f < fEnd; ++f) {
    PetscInt supportSize;

    PetscCall(DMPlexGetSupportSize(dm, f, &supportSize));
    if (supportSize == 1) ++in->numberoftrifaces;
  }
  if (isInterpolated == DMPLEX_INTERPOLATED_FULL && in->numberoftrifaces > 0) {
    PetscInt tf = 0;

    PetscCall(PetscMalloc1(in->numberoftrifaces * 3, &in->trifacelist));
    PetscCall(PetscMalloc1(in->numberoftrifaces, &in->trifacemarkerlist));
    for (f = fStart; f < fEnd; ++f) {
      PetscInt *points = NULL;
      PetscInt  supportSize, numPoints, p, Nv = 0, val;

      PetscCall(DMPlexGetSupportSize(dm, f, &supportSize));
      if (supportSize != 1) continue;
      PetscCall(DMPlexGetTransitiveClosure(dm, f, PETSC_TRUE, &numPoints, &points));
      for (p = 0; p < numPoints * 2; p += 2) {
        const PetscInt point = points[p];
        if ((point >= vStart) && (point < vEnd)) in->trifacelist[tf * 3 + Nv++] = point - vStart;
      }
      PetscCall(DMPlexRestoreTransitiveClosure(dm, f, PETSC_TRUE, &numPoints, &points));
      PetscCheck(Nv == 3, PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Face %" PetscInt_FMT " has %" PetscInt_FMT " vertices, not 3", f, Nv);
      PetscCall(DMLabelGetValue(universal->label, f, &val));
      if (val != defVal) in->trifacemarkerlist[tf] = (int)val;
      ++tf;
    }
  }

  PetscCall(DMPlexGetHeightStratum(dm, 0, &cStart, &cEnd));
  in->numberofcorners       = 4;
  in->numberoftetrahedra    = cEnd - cStart;
  in->tetrahedronvolumelist = maxVolumes;
  if (in->numberoftetrahedra > 0) {
    PetscCall(PetscMalloc1(in->numberoftetrahedra * in->numberofcorners, &in->tetrahedronlist));
    for (c = cStart; c < cEnd; ++c) {
      const PetscInt idx     = c - cStart;
      PetscInt      *closure = NULL;
      PetscInt       closureSize;

      PetscCall(DMPlexGetTransitiveClosure(dm, c, PETSC_TRUE, &closureSize, &closure));
      PetscCheck((closureSize == 5) || (closureSize == 15), comm, PETSC_ERR_ARG_WRONG, "Mesh has cell which is not a tetrahedron, %" PetscInt_FMT " vertices in closure", closureSize);
      for (v = 0; v < 4; ++v) in->tetrahedronlist[idx * in->numberofcorners + v] = closure[(v + closureSize - 4) * 2] - vStart;
      PetscCall(DMPlexRestoreTransitiveClosure(dm, c, PETSC_TRUE, &closureSize, &closure));
    }
  }

  if (rank == 0) {
    TetGenOpts t;

    PetscCall(TetGenOptsInitialize(&t));

    t.in        = dm; /* Should go away */
    t.refine    = 1;
    t.varvolume = 1;
    t.quality   = 1;
    t.edgesout  = 1;
    t.zeroindex = 1;
    t.quiet     = 1;
    t.verbose   = verbose; /* Change this */

    PetscCall(TetGenCheckOpts(&t));
    PetscCall(TetGenTetrahedralize(&t, in, out));
  }

  in->tetrahedronvolumelist = NULL;
  {
    const PetscInt numCorners  = 4;
    const PetscInt numCells    = out->numberoftetrahedra;
    const PetscInt numVertices = out->numberofpoints;
    PetscReal     *meshCoords  = NULL;
    PetscInt      *cells       = NULL;
    PetscBool      interpolate = isInterpolated == DMPLEX_INTERPOLATED_FULL ? PETSC_TRUE : PETSC_FALSE;

    if (sizeof(PetscReal) == sizeof(out->pointlist[0])) {
      meshCoords = (PetscReal *)out->pointlist;
    } else {
      PetscInt i;

      PetscCall(PetscMalloc1(dim * numVertices, &meshCoords));
      for (i = 0; i < dim * numVertices; ++i) meshCoords[i] = (PetscReal)out->pointlist[i];
    }
    if (sizeof(PetscInt) == sizeof(out->tetrahedronlist[0])) {
      cells = (PetscInt *)out->tetrahedronlist;
    } else {
      PetscInt i;

      PetscCall(PetscMalloc1(numCells * numCorners, &cells));
      for (i = 0; i < numCells * numCorners; ++i) cells[i] = (PetscInt)out->tetrahedronlist[i];
    }

    PetscCall(DMPlexInvertCells_CTetgen(numCells, numCorners, cells));
    PetscCall(DMPlexCreateFromCellListPetsc(comm, dim, numCells, numVertices, numCorners, interpolate, cells, dim, meshCoords, dmRefined));
    if (sizeof(PetscReal) != sizeof(out->pointlist[0])) PetscCall(PetscFree(meshCoords));
    if (sizeof(PetscInt) != sizeof(out->tetrahedronlist[0])) PetscCall(PetscFree(cells));

    /* Set labels */
    PetscCall(DMUniversalLabelCreateLabels(universal, PETSC_TRUE, *dmRefined));
    for (v = 0; v < numVertices; ++v) {
      if (out->pointmarkerlist[v]) PetscCall(DMUniversalLabelSetLabelValue(universal, *dmRefined, PETSC_TRUE, v + numCells, out->pointmarkerlist[v]));
    }
    if (interpolate) {
      PetscInt e, f;

      for (e = 0; e < out->numberofedges; e++) {
        if (out->edgemarkerlist[e]) {
          const PetscInt  vertices[2] = {out->edgelist[e * 2 + 0] + numCells, out->edgelist[e * 2 + 1] + numCells};
          const PetscInt *edges;
          PetscInt        numEdges;

          PetscCall(DMPlexGetJoin(*dmRefined, 2, vertices, &numEdges, &edges));
          PetscCheck(numEdges == 1, PETSC_COMM_SELF, PETSC_ERR_PLIB, "Two vertices must cover only one edge, not %" PetscInt_FMT, numEdges);
          PetscCall(DMUniversalLabelSetLabelValue(universal, *dmRefined, PETSC_TRUE, edges[0], out->edgemarkerlist[e]));
          PetscCall(DMPlexRestoreJoin(*dmRefined, 2, vertices, &numEdges, &edges));
        }
      }
      for (f = 0; f < out->numberoftrifaces; f++) {
        if (out->trifacemarkerlist[f]) {
          const PetscInt  vertices[3] = {out->trifacelist[f * 3 + 0] + numCells, out->trifacelist[f * 3 + 1] + numCells, out->trifacelist[f * 3 + 2] + numCells};
          const PetscInt *faces;
          PetscInt        numFaces;

          PetscCall(DMPlexGetFullJoin(*dmRefined, 3, vertices, &numFaces, &faces));
          PetscCheck(numFaces == 1, PETSC_COMM_SELF, PETSC_ERR_PLIB, "Three vertices must cover only one face, not %" PetscInt_FMT, numFaces);
          PetscCall(DMUniversalLabelSetLabelValue(universal, *dmRefined, PETSC_TRUE, faces[0], out->trifacemarkerlist[f]));
          PetscCall(DMPlexRestoreJoin(*dmRefined, 3, vertices, &numFaces, &faces));
        }
      }
    }

#ifdef PETSC_HAVE_EGADS
    {
      DMLabel        bodyLabel;
      PetscContainer modelObj;
      PetscInt       cStart, cEnd, c, eStart, eEnd, fStart, fEnd;
      ego           *bodies;
      ego            model, geom;
      int            Nb, oclass, mtype, *senses;

      /* Get Attached EGADS Model from Original DMPlex */
      PetscCall(PetscObjectQuery((PetscObject)dm, "EGADS Model", (PetscObject *)&modelObj));
      if (modelObj) {
        PetscCall(PetscContainerGetPointer(modelObj, (void **)&model));
        PetscCall(EG_getTopology(model, &geom, &oclass, &mtype, NULL, &Nb, &bodies, &senses));
        /* Transfer EGADS Model to Volumetric Mesh */
        PetscCall(PetscObjectCompose((PetscObject)*dmRefined, "EGADS Model", (PetscObject)modelObj));

        /* Set Cell Labels */
        PetscCall(DMGetLabel(*dmRefined, "EGADS Body ID", &bodyLabel));
        PetscCall(DMPlexGetHeightStratum(*dmRefined, 0, &cStart, &cEnd));
        PetscCall(DMPlexGetHeightStratum(*dmRefined, 1, &fStart, &fEnd));
        PetscCall(DMPlexGetDepthStratum(*dmRefined, 1, &eStart, &eEnd));

        for (c = cStart; c < cEnd; ++c) {
          PetscReal centroid[3] = {0., 0., 0.};
          PetscInt  b;

          /* Deterimine what body the cell's centroid is located in */
          if (!interpolate) {
            PetscSection coordSection;
            Vec          coordinates;
            PetscScalar *coords = NULL;
            PetscInt     coordSize, s, d;

            PetscCall(DMGetCoordinatesLocal(*dmRefined, &coordinates));
            PetscCall(DMGetCoordinateSection(*dmRefined, &coordSection));
            PetscCall(DMPlexVecGetClosure(*dmRefined, coordSection, coordinates, c, &coordSize, &coords));
            for (s = 0; s < coordSize; ++s)
              for (d = 0; d < dim; ++d) centroid[d] += coords[s * dim + d];
            PetscCall(DMPlexVecRestoreClosure(*dmRefined, coordSection, coordinates, c, &coordSize, &coords));
          } else PetscCall(DMPlexComputeCellGeometryFVM(*dmRefined, c, NULL, centroid, NULL));
          for (b = 0; b < Nb; ++b) {
            if (EG_inTopology(bodies[b], centroid) == EGADS_SUCCESS) break;
          }
          if (b < Nb) {
            PetscInt  cval    = b, eVal, fVal;
            PetscInt *closure = NULL, Ncl, cl;

            PetscCall(DMLabelSetValue(bodyLabel, c, cval));
            PetscCall(DMPlexGetTransitiveClosure(*dmRefined, c, PETSC_TRUE, &Ncl, &closure));
            for (cl = 0; cl < Ncl; cl += 2) {
              const PetscInt p = closure[cl];

              if (p >= eStart && p < eEnd) {
                PetscCall(DMLabelGetValue(bodyLabel, p, &eVal));
                if (eVal < 0) PetscCall(DMLabelSetValue(bodyLabel, p, cval));
              }
              if (p >= fStart && p < fEnd) {
                PetscCall(DMLabelGetValue(bodyLabel, p, &fVal));
                if (fVal < 0) PetscCall(DMLabelSetValue(bodyLabel, p, cval));
              }
            }
            PetscCall(DMPlexRestoreTransitiveClosure(*dmRefined, c, PETSC_TRUE, &Ncl, &closure));
          }
        }
      }
    }
#endif
    PetscCall(DMPlexSetRefinementUniform(*dmRefined, PETSC_FALSE));
  }
  PetscCall(DMUniversalLabelDestroy(&universal));
  PetscCall(PLCDestroy(&in));
  PetscCall(PLCDestroy(&out));
  PetscFunctionReturn(0);
}
