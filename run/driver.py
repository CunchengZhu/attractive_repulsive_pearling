import pymem3dg as dg
import pymem3dg.util as util
import numpy as np
import parameters

####################################################
#                 Initialize pathes                #
####################################################
""" Linux """
outputDir = "/home/cuzhu/attractive_repulsive_pearling/results/temp3"

""" Windows """
# outputDir = (
#     "C://Users//Kieran//Dev//2020-Mem3DG-Applications//results//bud//asymm//testTraj//boundaryMutation"
# )

# trajFile = "/home/cuzhu/2020-Mem3DG-Applications/results/bud/testrefactor3/traj.nc"
inputMesh = "/home/cuzhu/attractive_repulsive_pearling/run/input-file/hemisphere.obj"
# trajFile = "/home/cuzhu/attractive_repulsive_pearling/results/temp/traj.nc"
# inputMesh = "/home/cuzhu/attractive_repulsive_pearling/results/temp2/frame3.ply"

####################################################
#            Initialize input geometry             #
####################################################
""" Built-in construction """
# patFace, patVertex = dg.getHexagon(1, 4)
# icoFace, icoVertex = dg.getIcosphere(1, 3)
# tetFace, tetVertex = dg.getTetrahedron()
# diaFace, diaVertex = dg.getDiamond(3.14/3)
# cyFace, cyVertex = dg.getCylinder(1, 16, 60, 7.5, 0)
Face, Vertex = dg.processSoup(inputMesh)
Vertex = util.spherical_harmonics_perturbation(Vertex, 5, 15, 0.02)
Vertex = util.spherical_harmonics_perturbation(Vertex, 2, 10, 0.05)

""" Linux """
# inputMesh = "/home/cuzhu/2020-Mem3DG-Applications/run/input-file/patch.ply"

""" Windows """
# inputMesh = "C://Users//Kieran//Dev//2020-Mem3DG-Applications//run//input-file//patch.ply"

####################################################
#                 Parameters                       #
####################################################
""" Import from file """
p = parameters.parameters()

####################################################
#                 Mesh processor                   #
####################################################
mP = dg.MeshProcessor()
mP.meshMutator.shiftVertex = True
mP.meshMutator.flipNonDelaunay = True
# mP.meshMutator.splitLarge = True
mP.meshMutator.splitFat = True
mP.meshMutator.splitSkinnyDelaunay = True
mP.meshMutator.splitCurved = True
mP.meshMutator.curvTol = 0.002
mP.meshMutator.collapseSkinny = True
mP.meshMutator.collapseSmall = True
mP.meshMutator.collapseSmallNeedFlat = True
mP.meshMutator.targetFaceArea = 0.0005

mP.meshRegularizer.isSmoothenMesh = True
# mP.meshRegularizer.Kst = 0.1 # 2e-6
# mP.meshRegularizer.Ksl = 0
# mP.meshRegularizer.Kse = 0
# mP.meshRegularizer.readReferenceData(icoFace, icoVertex, 0)


####################################################
#                 System                           #
####################################################
nSub = 0
isContinue = True

""" System construction """
# g = dg.System(inputMesh, nSub)
g = dg.System(inputMesh, p, mP, nSub, isContinue)
# g = dg.System(Face, Vertex, p, mP, nSub)
# g = dg.System(trajFile, -1, p, mP, nSub)
# g = dg.System(cyFace, cyVertex, p, nSub)

# g.saveRichData(outputDir+"/hemisphere.obj", True)
###################################################
#          Time integration / Optimization
####################################################
""" Integrator setups (essential) """
h = 0.001
T = 10000000
eps = 1e-4
tSave = 1
verbosity = 5

""" Integrator construction """
fe = dg.Euler(g, h, T, tSave, eps, outputDir)

""" Integrator setups (optional) """
# fe.tUpdateGeodesics = 50
fe.processMeshPeriod = 50
# fe.isBacktrack = False
fe.isAdaptiveStep = True
fe.verbosity = verbosity
fe.integrate()