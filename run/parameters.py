import pymem3dg as dg
import numpy as np

def scalingVariables():
    # temp variable 
    xi = 1
    A_bar = 12.4866
    R_bar = np.sqrt(A_bar/ 4 / np.pi)
    Kb = 8.22e-5
    h = 4e-6 * (xi * R_bar**2 / Kb)
    return xi, A_bar, R_bar, Kb, h

def parameters(xi, A_bar, R_bar, Kb):
    p = dg.Parameters()

    p.proteinMobility = 3 * (1 / xi / R_bar**2)
    p.temperature = 0

    p.point.pt = [0, 0]
    p.point.isFloatVertex = False
    
    p.protein.profile = "none"
    p.protein.geodesicProteinDensityDistribution = [-1]
    p.protein.proteinInteriorPenalty = 0
    
    p.boundary.shapeBoundaryCondition = "none"
    p.boundary.proteinBoundaryCondition = "none"
    
    p.variation.isProteinVariation = True
    p.variation.isShapeVariation = True
    p.variation.geodesicMask = -1
    
    p.bending.Kd = 0
    p.bending.Kdc = 0
    p.bending.Kb = Kb
    p.bending.Kbc = 0  # 8.22e-4 #DEFINITION OF LARGE AND SMALL VALUE
    p.bending.H0c = -12 / R_bar
    
    p.tension.isConstantSurfaceTension = False
    p.tension.Ksg = 12000 * (Kb / R_bar**2)
    p.tension.A_res = 0
    p.tension.At = A_bar

    p.tension.lambdaSG = 0
    
    p.adsorption.epsilon = -2 * Kb / R_bar**2

    p.aggregation.chi = 5 * Kb / R_bar**2
    
    p.osmotic.isPreferredVolume = True
    p.osmotic.isConstantOsmoticPressure = False
    p.osmotic.Kv = 500 * Kb
    p.osmotic.V_res = 0
    p.osmotic.n = 1
    p.osmotic.Vt = 0.85 * (4/3 * np.pi * R_bar**3)
    p.osmotic.cam = -1
    p.osmotic.lambdaV = 0
    

    p.dirichlet.eta = 0.1 * Kb

    p.selfAvoidance.d = 0.001
    p.selfAvoidance.mu = 0
    p.selfAvoidance.p = 0
    p.selfAvoidance.n = 2
    
    p.dpd.gamma = 0
    
    p.external.Kf = 100000 * (Kb / R_bar)
    return p;


if __name__ == '__main__':
    p = parameters()
