

print("creating controls for each joint and geo")
import maya.cmds as cmds


def create_controls_for_selected():
    print("Creating controls for each selected object.")

    # Loop over each selected object
    for obj in cmds.ls(selection=True):
        # Get the position and rotation of the selected object
        # Create a control for each selection. The simplest control to make is a NURBS circle (found in the menu under Create > NURBS Primitives > Circle).

        # cmds.xform(control_circle, worldSpace=True, rotation = (90,0,0))
        # Create a parent group for each control also matching the transformations of the control/selected object.
        # Create a parent group for the control circle
        # Parent the control under its respective parent group.
        # Change the naming of the control and parent group using these parameters:
        # Each control will inherit its naming from the respective selected object but will end in "_Ctrl".
        # If the selected object already contains a suffix (such as "_Jnt" or "_Geo"), it will be removed and replaced with "_Ctrl". If the selected object does not have a suffix, then "_Ctrl" is simply appended to the control name.
        # The control parent group will end in "_Grp".
        position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)

        # Determine the base name for the control and group
        if "_Jnt" in obj:
            base_name = obj.partition("_Jnt")[0]
        elif "_Geo" in obj:
            base_name = obj.partition("_Geo")[0]
        else:
            base_name = obj

        # Create a NURBS circle control and rename it
        control_circle = cmds.circle(name=f"{base_name}_Ctrl", radius=0.5, normal=(1, 0, 0))[0]

        # Move and rotate the control to match the object's transformations
        cmds.xform(control_circle, worldSpace=True, translation=position)
        cmds.xform(control_circle, worldSpace=True, rotation=rotation)

        # Create a parent group and name it based on the base name
        parent_group = cmds.group(empty=True, name=f"{base_name}_Ctrl_Grp")

        # Move and rotate the group to match the object's transformations
        cmds.xform(parent_group, worldSpace=True, translation=position)
        cmds.xform(parent_group, worldSpace=True, rotation=rotation)

        # Parent the control under the group
        cmds.parent(control_circle, parent_group)

    print("Controls created successfully.")


# Run the function
create_controls_for_selected()
