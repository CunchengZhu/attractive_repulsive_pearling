import pymem3dg as dg
import pymem3dg.util as dg_util
import pymem3dg.visual as dg_vis
import pymem3dg.read as dg_read

import matplotlib.pyplot as plt
import polyscope as ps
import numpy as np
import imp

if __name__ == "__main__":
    """working directory"""
    wd = "../../results/"

    """ initialize polyscope """
    ps.init()

    """ list all parameters """
    parametersList = [wd + "temp/parameters.py"]
    # parametersList = [wd + '0p7_neg/parameters.py',
    #                   wd + '0p7_neg/parameters.py', wd + '0p7/parameters.py']

    """ list all meshes """
    """ based on .ply file """
    # meshList = ['0p6/frame3', '0p6/frame7', '0p8/frame10',
    #                  '0p8/frame20', '1/frame70', '1/frame140', '1p2/frame166', '1p2/frame332']

    """ based on .nc file """
    # meshList = [(wd + '0p7_neg/traj', 14),
    #             (wd + '0p7_neg/traj', 27), (wd + '0p7/traj', 200)]
    meshList = [(wd + "temp/traj", 10)]

    """ loop over meshes """
    for i in range(len(meshList)):
        trajNc, frame = meshList[i]

        """construct a tag"""
        tag = meshList[i][0] + "{}".format(meshList[i][1])

        """ read mesh """
        face, vertex = dg_read.readMeshByNc(trajNc, frame)
        mesh = ps.register_surface_mesh(tag, vertex, face)

        """ read parameters """
        parameterFile = imp.load_source("module.name", parametersList[i])

        """ construct system """
        xi, A_bar, R_bar, Kb = parameterFile.scalingVariables()
        system = dg.System(
            trajNc + ".nc", frame, parameterFile.parameters(xi, A_bar, R_bar, Kb), True
        )

        """ read protein density """
        proteinDensity = system.getProteinDensity()
        limit = (np.min(proteinDensity), np.max(proteinDensity))
        mesh.add_scalar_quantity("proteinDensity", proteinDensity, vminmax=limit)

        """ read spontaneous curvature """
        spontaneousCurvature = system.getSpontaneousCurvature()
        limit = (np.min(spontaneousCurvature), np.max(spontaneousCurvature))
        mesh.add_scalar_quantity(
            "spontaneousCurvature", spontaneousCurvature, vminmax=limit
        )

        """ compute forces """
        system.computePhysicalForcing()

        """ read line capillary force """
        lineCapillaryForce = system.forces.getLineCapillaryForce()
        mesh.add_vector_quantity("lineCapillaryForce", lineCapillaryForce)
        mesh.add_scalar_quantity(
            "lineCapillaryForce_norm", dg_util.rowwiseNorm(lineCapillaryForce)
        )

        """ read bending force """
        bendingForce = system.forces.getBendingForce()
        mesh.add_vector_quantity("bendingForce", bendingForce)
        mesh.add_scalar_quantity("bendingForce_norm", dg_util.rowwiseNorm(bendingForce))

        """ color map """
        fig, axs = plt.subplots(1, 1)
        fig.set_size_inches(1, 1)
        fig = dg_vis.getColorMap(fig, limit)
        fig.savefig(tag + ".pdf", transparent=True)
        # plt.subplots_adjust(left=0.164, bottom=0.07, right=0.988, top=0.988)
        # fig.savefig(meshFile +"_horizontal.pdf", transparent=True)

    """ configure Polyscope """
    ps.set_up_dir("z_up")
    ps.show()
