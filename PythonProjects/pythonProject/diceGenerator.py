import maya.cmds as cmds


def duplicate_on_each_face(flip_object=False):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)

    # Ensure we have exactly two objects selected
    if len(selected_objects) < 2:
        cmds.warning(
            "Please select two objects: the first to place duplicates on, the second as the object to duplicate.")
        return

    # The first selected object will be the base geometry
    base_obj = selected_objects[0]
    # The second selected object will be the template to duplicate
    template_obj = selected_objects[1]

    # Get the total number of faces on the base object
    face_count = cmds.polyEvaluate(base_obj, face=True)

    # Loop through each face of the base object
    for face_index in range(face_count):
        face = f"{base_obj}.f[{face_index}]"

        # Select the current face to process its normal and position
        cmds.select(face, r=True)

        # Get the normal information using polyInfo
        face_normals_info = cmds.polyInfo(faceNormals=True)
        face_normal_parts = face_normals_info[0].split()
        face_normal = [
            float(face_normal_parts[-3]),
            float(face_normal_parts[-2]),
            float(face_normal_parts[-1])
        ]

        # Convert face to vertex list and calculate face center
        face_vertices = cmds.polyListComponentConversion(face, fromFace=True, toVertex=True)
        vertices = cmds.ls(face_vertices, flatten=True)

        # Calculate the center of the face by averaging the positions of its vertices
        face_center = [0.0, 0.0, 0.0]
        for vertex in vertices:
            vertex_pos = cmds.xform(vertex, query=True, worldSpace=True, translation=True)
            face_center[0] += vertex_pos[0]
            face_center[1] += vertex_pos[1]
            face_center[2] += vertex_pos[2]
        face_center = [x / len(vertices) for x in face_center]

        # Duplicate the template object and position it at the face center
        duplicate_name = f"{template_obj}_duplicate_{face_index}"
        duplicate = cmds.duplicate(template_obj, name=duplicate_name)[0]
        cmds.xform(duplicate, worldSpace=True, translation=face_center)

        # Orient the duplicate to align its y-axis with the face normal
        # Create a locator in the direction of the normal for the aim constraint
        locator = cmds.spaceLocator(name=f"target_locator_{face_index}")[0]
        cmds.xform(locator, worldSpace=True, translation=(
            face_center[0] + face_normal[0],
            face_center[1] + face_normal[1],
            face_center[2] + face_normal[2]
        ))

        # Apply the aim constraint with the face normal aiming the y-axis of the duplicate
        cmds.aimConstraint(locator, duplicate, aimVector=(0, 1, 0), upVector=(1, 0, 0), worldUpType="vector",
                           worldUpVector=(face_normal[0], face_normal[1], face_normal[2]))
        cmds.delete(locator)  # Delete locator after alignment is complete

        # If flip_object is True, rotate the object 180 degrees on the x-axis to flip it upside down
        if flip_object:
            cmds.rotate(180, 0, 0, duplicate, relative=True, objectSpace=True)

        # Clear selection after processing each face
        cmds.select(clear=True)

        # Print normal and position information for each face
        print(f"Face {face_index} Normals:", face_normal)
        print(f"Face {face_index} Position:", face_center)

#part one - copy object to each face
# Set the flip_object variable and run the function
#flip_object = True  # Set to False if you don’t want to flip the object
#uplicate_on_each_face(flip_object=flip_object)




#part two - create text on each object
