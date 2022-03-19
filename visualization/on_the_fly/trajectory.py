import netCDF4 as nc
import sys
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
import pymem3dg as dg
import imp
import pymem3dg.visual as dg_vis
import pymem3dg.read as dg_read

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data",
        help="traj.nc and parameter setup file used for visualization of data, such as energy trajectory",
        type=str,
        nargs=2,
    )
    args = parser.parse_args()

    """ parse the netCDF trajectory file """
    trajFile = args.data[1]

    """ parse the parameter.py file """
    parameterFile = imp.load_source("module.name", args.data[0])

    """ initialize numpy array """
    frameLim = (0, dg_read.sizeOf(trajFile))
    frameNum = frameLim[1] - frameLim[0]
    time = np.zeros(frameNum)
    kineticEnergy = np.zeros(frameNum)
    potentialEnergy = np.zeros(frameNum)
    externalWork = np.zeros(frameNum)
    totalEnergy = np.zeros(frameNum)

    dirichletEnergy = np.zeros(frameNum)
    bendingEnergy = np.zeros(frameNum)
    surfaceEnergy = np.zeros(frameNum)
    pressureEnergy = np.zeros(frameNum)
    adsorptionEnergy = np.zeros(frameNum)

    """ loop over trajectory and recover data """
    for frame in range(frameNum):
        """construct the system"""
        xi, A_bar, R_bar, Kb = parameterFile.scalingVariables()
        system = dg.System(
            trajFile,
            frame + frameLim[0],
            parameterFile.parameters(xi, A_bar, R_bar, Kb),
            True,
        )
        time[frame] = system.time

        """ computate energy """
        system.computeTotalEnergy()
        kineticEnergy[frame] = system.energy.kineticEnergy
        potentialEnergy[frame] = system.energy.potentialEnergy
        if frame != 0:
            externalWork[frame] = externalWork[
                frame - 1
            ] + system.computeIntegratedPower(time[frame] - time[frame - 1])

        dirichletEnergy[frame] = system.energy.dirichletEnergy
        bendingEnergy[frame] = system.energy.bendingEnergy
        surfaceEnergy[frame] = system.energy.surfaceEnergy
        pressureEnergy[frame] = system.energy.pressureEnergy
        adsorptionEnergy[frame] = system.energy.adsorptionEnergy
    totalEnergy = potentialEnergy + kineticEnergy - externalWork

    """ plotting """
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(7, 3)
    # plt.subplots_adjust(left=0.164, bottom=0.07, right=0.988, top=0.988)
    dg_vis.matplotlibStyle()
    axs[0].plot(time, kineticEnergy, label="$E_{kinetic}$")
    axs[0].plot(time, potentialEnergy, label="$E_{potential}$")
    axs[0].plot(time, externalWork, label="$W$")
    axs[0].plot(time, totalEnergy, label="$E_{total}$")
    axs[0].legend()

    axs[1].plot(time, bendingEnergy, label="$E_b$")
    axs[1].plot(time, dirichletEnergy, label="$E_d$")
    axs[1].plot(time, surfaceEnergy, label="$E_s$")
    axs[1].plot(time, pressureEnergy, label="$E_p$")
    axs[1].plot(time, adsorptionEnergy, label="$E_a$")
    axs[1].legend()

    plt.tight_layout()
    # plt.savefig("energy.pdf", transparent=True)
    # plt.savefig("energy.png", transparent=True, dpi=1200)
    plt.show()
