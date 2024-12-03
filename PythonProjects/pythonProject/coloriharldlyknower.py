import maya.cmds as cmds
import random
#get selected objects
sels = cmds.ls(selection=True)
print(sels)
randomcolor = False

for sel in sels:
    if "Shape" in sel:
        print(sel)

        override = sel+".overrideEnabled"
        letcolor = sel+".overrideColor"
        if randomcolor :
            newcolor = random.randint(0, 31)
        else:
            newcolor = 8
        cmds.setAttr(letcolor, newcolor)
        cmds.setAttr(override,1)
