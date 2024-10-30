import random

import maya.cmds as cmds

gridx = 6
gridy = 3
gridz = 5
size = 2
placechance = 3  # 0 = every time, 1 = 50%, 2 = 33.3%, 3 = 25%, etc.

placedCubes = []
for x in range(gridx):
    for y in range(gridy):
        for z in range(gridz):
            placenum = random.randint(0, placechance)
            if placenum == 0:
                newcubeName = "pcube-" + str(x) + str(y) + str(z)
                # Create the cube and unpack transform and shape
                #this was fixed by ai when i was struggling with making a list and putting the right one to the right place,
                # it said to use unpacking, which i dont know if mel does?
                cube_transform, cube_shape = cmds.polyCube(width=size, depth=size, height=size, name=newcubeName)

                #f character before a string allows you to pass data in? this was also done with AI when debugging, and seems pretty useful.
                print(f"Placing cube with size {size} at position XYZ: {x}, {y}, {z}, named {newcubeName}")
                placedCubes.append(cube_transform)

                # Move the cube to the desired location
                cmds.move(x * size, y * size, z * size, cube_transform)

print("Total placed cubes:", len(placedCubes))
cmds.group(placedCubes, name = "CubeGrid")
