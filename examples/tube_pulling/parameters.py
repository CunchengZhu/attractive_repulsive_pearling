import pymem3dg as dg
def parameters():
    p = dg.Parameters()

    p.proteinMobility = 0
    p.temperature = 0

    p.point.pt = [0,0]
    p.point.isFloatVertex = True
    
    p.proteinDistribution.profile = "none"
    p.proteinDistribution.protein0 = [1]
    
    p.boundary.shapeBoundaryCondition = "fixed"
    p.boundary.proteinBoundaryCondition = "none"
    
    p.variation.isProteinVariation = False
    p.variation.isShapeVariation = True
    p.variation.radius = -1
    
    p.bending.Kb = 0
    p.bending.Kbc = 8.22e-5 
    p.bending.H0c = 0
    
    p.tension.isConstantSurfaceTension = True
    p.tension.Ksg = 1e-3
    p.tension.A_res = 0
    p.tension.At = 0
    p.tension.lambdaSG = 0
    
    p.adsorption.epsilon = 0 #-1e-3
    
    p.osmotic.isPreferredVolume = False
    p.osmotic.isConstantOsmoticPressure = True
    p.osmotic.Kv = 0
    p.osmotic.V_res = 0
    p.osmotic.n = 1
    p.osmotic.Vt = -1  # 1 * 4 * 3.1416 / 3
    p.osmotic.cam = -1
    p.osmotic.lambdaV = 0
    
    p.dirichlet.eta = 0
    
    p.dpd.gamma = 0
    
    p.external.Kf = 0.1
    return p;


if __name__ == '__main__':
    p = parameters()
