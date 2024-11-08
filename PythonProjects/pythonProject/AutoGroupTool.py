

print("creating group from selected objects!")

import maya.cmds as cmds


def group_and_parent_selected():
    # Get selected objects
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("No objects selected. Please select one or more objects.")
        return

    for obj in selected_objects:
        # Query the position and rotation of the selected object
        position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)

        # Create a new group with no initial transformation
        group_name = cmds.group(empty=True, name=obj + "_grp")

        # Move and rotate the group to match the selected object's transformation
        cmds.xform(group_name, worldSpace=True, translation=position)
        cmds.xform(group_name, worldSpace=True, rotation=rotation)

        # Parent the object to the new group
        cmds.parent(obj, group_name)

    print("Grouping and parenting completed for selected objects.")


# Run the function
group_and_parent_selected()
