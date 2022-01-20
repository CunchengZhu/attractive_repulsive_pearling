import pymem3dg as dg
def parameters():
    p = dg.Parameters()

    p.proteinMobility = 50
    p.temperature = 0

    p.point.pt = [0,0]
    p.point.isFloatVertex = False
    
    p.proteinDistribution.profile = "none"
    p.proteinDistribution.protein0 = [0.5]
    p.proteinDistribution.lambdaPhi = 1e-6
    
    p.boundary.shapeBoundaryCondition = "fixed"
    p.boundary.proteinBoundaryCondition = "pin"
    
    p.variation.isProteinVariation = True
    p.variation.isShapeVariation = True
    p.variation.radius = -1
    
    p.bending.Kb = 8.22e-5
    p.bending.Kbc = 3 * 8.22e-5  # 8.22e-4 #DEFINITION OF LARGE AND SMALL VALUE
    p.bending.H0c = -60
    
    p.tension.isConstantSurfaceTension = False
    p.tension.Ksg = 1
    p.tension.A_res = 0
    p.tension.At = 3.7
    
    p.tension.lambdaSG = 0
    
    p.adsorption.epsilon = -3e-1

    p.aggregation.chi = -25e-2
    
    p.osmotic.isPreferredVolume = False
    p.osmotic.isConstantOsmoticPressure = True
    p.osmotic.Kv = 0.03
    p.osmotic.V_res = 0
    p.osmotic.n = 1
    p.osmotic.Vt = -1  # 1 * 4 * 3.1416 / 3
    p.osmotic.cam = -1
    p.osmotic.lambdaV = 0
    
    p.dirichlet.eta = 0.002

    p.selfAvoidance.d = 0
    p.selfAvoidance.mu = 0
    p.selfAvoidance.p = 0
    p.selfAvoidance.n = 2
    p.dpd.gamma = 0
    
    p.external.Kf = 0
    return p;


if __name__ == '__main__':
    p = parameters()
