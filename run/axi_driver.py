import pymem3dg.axisymmetry as axi
import numpy as np
import matplotlib.pyplot as plt

p = axi.Parameters()

# radius = np.linspace(0, 3.0, num=5)
radius = np.array([0.0,1.0,3.0,2.0,1.0,0.0])
height = np.array([0.0,1.0,2.0,3.0,4.0,5.0])
g = axi.System(radius, height, p)
# g.compute_bendingEnergy()
g.compute_bendingForce()
print(g.arclength_v)
print(g.turningAngle_v)
# print(g.energy.bendingEnergy)
print(g.energy.bendingForce)
print(g.energy.bendingForce.shape)


# Visualization preference
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
SMALL_SIZE = 13
MEDIUM_SIZE = 18
BIGGER_SIZE = 20
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rc('pdf', fonttype=42)

# figure dimension
fig, axs = plt.subplots(4)
fig.set_size_inches(7, 10)
plt.subplots_adjust(left=0.164, bottom=0.07, right=0.988, top=0.988)
axs[0].plot(radius, height, label='$E$')