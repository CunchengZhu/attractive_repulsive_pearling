import pymem3dg.util as dg_util
import pymem3dg.visual as dg_vis
import pymem3dg.read as dg_read


import imp
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    parameterFile = imp.load_source("module.name", "../../results/temp/parameters.py")
    xi, A_bar, R_bar, Kb = parameterFile.scalingVariables()
    parameters = parameterFile.parameters(xi, A_bar, R_bar, Kb)
    dg_vis.animate(
        "../../results/temp/traj.nc",
        parameters=parameters,
        meanCurvature=True,
        gaussianCurvature=True,
        bendingForce=True,
        externalForce=True,
        mechanicalForce=True,
        capillaryForce=True,
        lineCapillaryForce=True,
        osmoticForce=True,
        chemicalPotential=True,
        bendingPotential=True,
        diffusionPotential=True,
        aggregationPotential=True,
        adsorptionPotential=True
    )
