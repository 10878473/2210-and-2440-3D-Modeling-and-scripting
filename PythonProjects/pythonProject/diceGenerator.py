#TODO
#take a face, and gfind the nand center position of it.
#if you are selecting an obj like a dodecahedron or d20, loop through each face on it.

#testing first with cube

#find selected object and name it

#find a face from the object, and get the face normal and center point of it. 
import maya.cmds as cmds

# Select the face you want to query (replace 'pCube1.f[0]' with your specific face)

cmds.select("pCube1.f[0]", r=True)

# Get the normal information
face_normals = cmds.polyInfo(faceNormals=True)

# Get the face position in world space
face_position = cmds.xform(query=True, worldSpace=True, translation=True)

# Print the normal and position information
print("Face Normals:", face_normals)
print("Face Position:", face_position)
