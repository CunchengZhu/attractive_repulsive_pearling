import pymem3dg as dg
import pymem3dg.util as util
import numpy as np
import parameters

####################################################
#                 Initialize pathes                #
####################################################
""" Linux """
outputDir = "/home/cuzhu/attractive_repulsive_pearling/results/temp5_cont_cont_cont"

""" Windows """
# outputDir = (
#     "C://Users//Kieran//Dev//2020-Mem3DG-Applications//results//bud//asymm//testTraj//boundaryMutation"
# )

# trajFile = "/home/cuzhu/2020-Mem3DG-Applications/results/bud/testrefactor3/traj.nc"
inputMesh = "/home/cuzhu/attractive_repulsive_pearling/results/temp5_cont_cont/frame1193.ply"
# trajFile = "/home/cuzhu/attractive_repulsive_pearling/results/temp/traj.nc"
# inputMesh = "/home/cuzhu/attractive_repulsive_pearling/results/temp/frame0.ply"

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
# Vertex = util.spherical_harmonics_perturbation(Vertex, 5, 6, 0.1)
# Vertex = util.spherical_harmonics_perturbation(Vertex, 2, 5, 0.1)

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
mP.meshMutator.curvTol = 0.006
mP.meshMutator.collapseSkinny = True
mP.meshMutator.collapseSmall = True
mP.meshMutator.collapseSmallNeedFlat = True
mP.meshMutator.targetFaceArea = 0.0003

mP.meshRegularizer.isSmoothenMesh = True
# mP.meshRegularizer.Kst = 0.1 # 2e-6
# mP.meshRegularizer.Ksl = 0
# mP.meshRegularizer.Kse = 0
# mP.meshRegularizer.readReferenceData(icoFace, icoVertex, 0)


####################################################
#                 System                           #
####################################################
nSub = 0
nMutation = 0
isContinue = True

""" System construction """
# g = dg.System(inputMesh, nSub)
g = dg.System(inputMesh, p, mP, nSub, nMutation, isContinue)
# g = dg.System(Face, Vertex, p, mP, nSub)
# g = dg.System(trajFile, -1, p, mP, nSub)
# g = dg.System(cyFace, cyVertex, p, nSub)

# g.saveRichData(outputDir+"/hemisphere.obj", True)
###################################################
#          Time integration / Optimization
####################################################
""" Integrator setups (essential) """
h = 0.05
T = 10000000
eps = 1e-4
tSave = 10
verbosity = 5

""" Integrator construction """
fe = dg.Euler(g, h, T, tSave, eps, outputDir)

""" Integrator setups (optional) """
# fe.tUpdateGeodesics = 50
fe.processMeshPeriod = 10
# fe.fluctuatePeriod = 10
# fe.fluctuateAmplitude = 0.001
fe.isBacktrack = True
fe.isAdaptiveStep = False
fe.verbosity = verbosity
fe.integrate()