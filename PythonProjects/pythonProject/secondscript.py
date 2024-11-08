import maya.cmds as cmds
number = 6
print (number)
number = "11"
print(number)
obj = cmds.polySphere()[0]
obj = cmds.rename(obj, "ball")
print(obj)



