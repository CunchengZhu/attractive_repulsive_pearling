import pymem3dg as dg
def parameters():
    p = dg.Parameters()

    p.proteinMobility = 0
    p.temperature = 0

    p.point.pt = [0,0]
    p.point.isFloatVertex = True
    
    p.proteinDistribution.profile = "tanh"
    p.proteinDistribution.protein0 = [2.7,2.7,1,0]
    
    p.boundary.shapeBoundaryCondition = "pin"
    p.boundary.proteinBoundaryCondition = "none"
    
    p.variation.isProteinVariation = False
    p.variation.isShapeVariation = True
    p.variation.radius = -1
    
    p.bending.Kb = 8.22e-5
    p.bending.Kbc = 8.22e-5
    p.bending.H0c = 6
    
    p.tension.isConstantSurfaceTension = True
    p.tension.Ksg = 2e-3
    p.tension.A_res = 0
    p.tension.At = 0
    p.tension.lambdaSG = 0
    
    p.adsorption.epsilon = 0 #-1e-3
    
    p.osmotic.isPreferredVolume = False
    p.osmotic.isConstantOsmoticPressure = True
    p.osmotic.Kv = 2.5e-2
    p.osmotic.V_res = 0
    p.osmotic.n = 1
    p.osmotic.Vt = -1  # 1 * 4 * 3.1416 / 3
    p.osmotic.cam = -1
    p.osmotic.lambdaV = 0
    
    p.dirichlet.eta = 0
    
    p.dpd.gamma = 0
    
    p.external.Kf = 0
    return p;


if __name__ == '__main__':
    p = parameters()
