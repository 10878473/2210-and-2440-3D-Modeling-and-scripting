import maya.cmds as cmds


def create_text_on_icosahedron():
    # Create an icosahedron without using the platonicSolidType flag
    icosahedron = cmds.polyPlatonic()[0]

    # Get the number of faces of the icosahedron (should be 20)
    face_count = cmds.polyEvaluate(icosahedron, face=True)

    # Check if the face count is 20 (to ensure we have a valid icosahedron)
    if face_count != 20:
        cmds.warning("The object does not have 20 faces.")
        return

    # Loop through each face and place the corresponding number as text
    for face_index in range(face_count):
        face = f"{icosahedron}.f[{face_index}]"

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

        # Create the text for the current face (numbered from 1 to 20)
        text = cmds.CreatePolygonType(query=False, text=str(face_index + 1))

        # Rename the created text object to something unique
        new_name = f"text_{face_index + 1}"
        cmds.rename(text, new_name)

        # Scale the text down to fit within the face (scale down by 0.1)
        cmds.xform(new_name, scale=(0.1, 0.1, 0.1))

        # Move the text to the face center
        cmds.xform(new_name, worldSpace=True, translation=face_center)

        # Create a locator to aim the text along the face normal
        locator = cmds.spaceLocator(name=f"target_locator_{face_index}")[0]
        cmds.xform(locator, worldSpace=True, translation=(
            face_center[0] + face_normal[0],
            face_center[1] + face_normal[1],
            face_center[2] + face_normal[2]
        ))

        # Aim the text along the face normal (making the text "top" point in the direction of the face normal)
        cmds.aimConstraint(locator, new_name, aimVector=(0, 1, 0), upVector=(1, 0, 0), worldUpType="vector",
                           worldUpVector=(face_normal[0], face_normal[1], face_normal[2]))

        # Clean up the locator
        cmds.delete(locator)

        # Print normal and position information for each face
        print(f"Face {face_index + 1} Normals:", face_normal)
        print(f"Face {face_index + 1} Position:", face_center)


# Run the function to create text on each face of the icosahedron
create_text_on_icosahedron()
