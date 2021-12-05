import pymem3dg as dg
def parameters():
    p = dg.Parameters()

    p.proteinMobility = 10
    p.temperature = 0

    p.point.pt = [0,0]
    p.point.isFloatVertex = False
    
    p.proteinDistribution.profile = "none"
    p.proteinDistribution.protein0 = [-1]
    p.proteinDistribution.lambdaPhi = 1e-7
    
    p.boundary.shapeBoundaryCondition = "fixed"
    p.boundary.proteinBoundaryCondition = "pin"
    
    p.variation.isProteinVariation = True
    p.variation.isShapeVariation = True
    p.variation.radius = -1
    
    p.bending.Kb = 8.22e-5
    p.bending.Kbc = 2 * 8.22e-5  # 8.22e-4 #DEFINITION OF LARGE AND SMALL VALUE
    p.bending.H0c = 60
    
    p.tension.isConstantSurfaceTension = False
    p.tension.Ksg = 1
    p.tension.A_res = 0
    p.tension.At = 3.40904
    p.tension.lambdaSG = 0
    
    p.adsorption.epsilon = -1e-4

    p.aggregation.chi = -5e-2
    
    p.osmotic.isPreferredVolume = False
    p.osmotic.isConstantOsmoticPressure = True
    p.osmotic.Kv = 1e-4
    p.osmotic.V_res = 0
    p.osmotic.n = 1
    p.osmotic.Vt = -1  # 1 * 4 * 3.1416 / 3
    p.osmotic.cam = -1
    p.osmotic.lambdaV = 0
    
    p.dirichlet.eta = 0.0001

    p.selfAvoidance.d = 0.001
    p.selfAvoidance.mu = 0.0001
    
    p.dpd.gamma = 0
    
    p.external.Kf = 0
    return p;


if __name__ == '__main__':
    p = parameters()
