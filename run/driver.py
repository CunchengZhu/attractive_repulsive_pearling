import pymem3dg as dg
import pymem3dg.util as dg_util
import pymem3dg.visual as dg_vis
import numpy as np
import parameters
####################################################
#                 Initialize pathes                #
####################################################
""" Linux """
# home = "/home/cuzhu/attractive_repulsive_pearling"
""" Windows """
home = "C:/Users/zhucu/Dev/attractive_repulsive_pearling"

outputDir = home + "/results/temp"
####################################################
#            Initial conditions                    #
####################################################
""" Built-in construction """
# Face, Vertex = dg.getHexagon(1, 4)
Face, Vertex = dg.getIcosphere(1, 3)
# Face, Vertex = dg.getTetrahedron()
# Face, Vertex = dg.getDiamond(3.14/3)
# Face, Vertex = dg.getCylinder(1, 16, 60, 7.5, 0)
# Face, Vertex = dg.processSoup(inputMesh)
# Face, Vertex = dg.stripRichData(inputMesh)
Vertex = dg_util.sphericalHarmonicsPerturbation(Vertex, 5, 6, 0.1)
""" input construction """
trajFile = outputDir + "//traj.nc"
# inputMesh = outputDir + "/temp7/frame1780.ply"
""" additional initial condition """
proteinDensity = np.ones(np.shape(Vertex)[0]) * 0.5
velocity = np.zeros(np.shape(Vertex))
####################################################
#                 Parameters                       #
####################################################
""" Import from file """
xi, A_bar, R_bar, Kb, h = parameters.scalingVariables()
p = parameters.parameters(xi, A_bar, R_bar, Kb)
####################################################
#                 System                           #
####################################################
""" System construction """
# g = dg.System(inputMesh)
g = dg.System(Face, Vertex, proteinDensity, velocity, p)
# g = dg.System(trajFile, 4, p)
""" Mesh processor """
g.meshProcessor.meshMutator.isShiftVertex = True
g.meshProcessor.meshMutator.flipNonDelaunay = True
# g.meshProcessor.meshMutator.splitLarge = True
g.meshProcessor.meshMutator.splitFat = True
g.meshProcessor.meshMutator.splitSkinnyDelaunay = True
g.meshProcessor.meshMutator.splitCurved = True
g.meshProcessor.meshMutator.minimumEdgeLength = 0.001
g.meshProcessor.meshMutator.curvTol = 0.006
g.meshProcessor.meshMutator.collapseSkinny = True
g.meshProcessor.meshMutator.collapseSmall = True
g.meshProcessor.meshMutator.collapseFlat = True
g.meshProcessor.meshMutator.targetFaceArea = 0.0003
g.meshProcessor.meshMutator.isSmoothenMesh = True
# g.meshProcessor.meshRegularizer.Kst = 0.1 # 2e-6
# g.meshProcessor.meshRegularizer.Ksl = 0
# g.meshProcessor.meshRegularizer.Kse = 0
# g.meshProcessor.meshRegularizer.readReferenceData(icoFace, icoVertex, 0)
""" System initialization """
g.initialize(nMutation=2, ifMute=False)
####################################################
#          Time integration / Optimization         #
####################################################
""" Integrator construction """
fe = dg.Euler(
    system=g,
    characteristicTimeStep=h,
    totalTime=10000 * h,
    savePeriod=100 * h,
    tolerance=1e-4,
    outputDirectory=outputDir,
    frame=0,
)
""" settings """
# fe.tUpdateGeodesics = 50
fe.processMeshPeriod = 20
# fe.fluctuatePeriod = 10
# fe.fluctuateAmplitude = 0.001
fe.isBacktrack = True
# fe.ifAdaptiveStep = True
""" Verbosity """
fe.ifPrintToConsole = True
fe.ifOutputTrajFile = True
# fe.ifOutputMeshFile = True

# fe.integrate()
####################################################
#                       Visualization              # 
####################################################
# dg_vis.animate(outputDir+"/traj.nc", meanCurvature = True)