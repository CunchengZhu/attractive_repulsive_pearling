import pymem3dg as dg
def parameters():
    p = dg.Parameters()

    p.proteinMobility = 1
    p.temperature = 0

    p.point.pt = [0,0]
    p.point.isFloatVertex = False
    
    p.proteinDistribution.profile = "none"
    p.proteinDistribution.protein0 = [0.1]
    p.proteinDistribution.lambdaPhi = 1e-5
    
    p.boundary.shapeBoundaryCondition = "none"
    p.boundary.proteinBoundaryCondition = "none"
    
    p.variation.isProteinVariation = True
    p.variation.isShapeVariation = True
    p.variation.radius = -1
    
    p.bending.Kd = 0
    p.bending.Kdc = 0
    p.bending.Kb = 8.22e-5
    p.bending.Kbc = 0  # 8.22e-4 #DEFINITION OF LARGE AND SMALL VALUE
    p.bending.H0c = 12
    
    p.tension.isConstantSurfaceTension = False
    p.tension.Ksg = 1
    p.tension.A_res = 0
    p.tension.At = 12.4866

    p.tension.lambdaSG = 0
    
    p.adsorption.epsilon = -0.02

    p.aggregation.chi = 0
    
    p.osmotic.isPreferredVolume = True
    p.osmotic.isConstantOsmoticPressure = False
    p.osmotic.Kv = 1
    p.osmotic.V_res = 0
    p.osmotic.n = 1
    p.osmotic.Vt = 4.14 * 0.8  # 1 * 4 * 3.1416 / 3
    p.osmotic.cam = -1
    p.osmotic.lambdaV = 0
    

    p.dirichlet.eta = 0

    p.selfAvoidance.d = 0.001
    p.selfAvoidance.mu = 0
    p.selfAvoidance.p = 0
    p.selfAvoidance.n = 2
    
    p.dpd.gamma = 0
    
    p.external.Kf = 1
    return p;


if __name__ == '__main__':
    p = parameters()
