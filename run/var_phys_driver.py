import pymem3dg as dg


x = dg.Bending_Physic()
y = dg.Stretching_Physic()
print("\nInitialize with stretching:")
dg.Variable_Physics_System([y])

print("\nInitialize with bending:")
dg.Variable_Physics_System([x])

print("\nInitialize with both:")
dg.Variable_Physics_System([x, y])
