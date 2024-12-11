import maya.cmds as cmds
import random


def recolor_objects(random_color, selected_color):
    """
    Recolors selected objects with a specific or random color.
    """
    sels = cmds.ls(selection=True, long=True)
    if not sels:
        cmds.warning("No objects selected.")
        return

    for sel in sels:
        if cmds.objectType(sel) == "transform":
            # Find associated shape node
            shapes = cmds.listRelatives(sel, shapes=True, fullPath=True)
            if not shapes:
                continue
            sel = shapes[0]

        # Check if object is a shape node
        if cmds.objectType(sel) in ["mesh", "nurbsCurve", "nurbsSurface"]:
            override = sel + ".overrideEnabled"
            letcolor = sel + ".overrideColor"

            if random_color:
                new_color = random.randint(0, 31)
            else:
                new_color = selected_color

            cmds.setAttr(override, 1)
            cmds.setAttr(letcolor, new_color)
            print(f"Set {sel} to color {new_color}")


def create_recolor_ui():
    """
    Creates a UI to allow users to recolor selected objects.
    """
    window_name = "RecolorUI"

    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    window = cmds.window(window_name, title="Recolor Tool", widthHeight=(300, 200))

    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Select Recolor Options", align="center")

    random_color_cb = cmds.checkBox(label="Random Color", value=False)

    cmds.separator(height=10, style="in")
    cmds.text(label="Choose Color (if not random):", align="center")
    color_slider = cmds.intSliderGrp(
        field=True, minValue=0, maxValue=31, value=8, label="Color Index"
    )

    cmds.separator(height=10, style="in")

    cmds.button(
        label="Apply Color",
        command=lambda _: recolor_objects(
            cmds.checkBox(random_color_cb, query=True, value=True),
            cmds.intSliderGrp(color_slider, query=True, value=True)
        )
    )

    cmds.separator(height=10, style="in")

    cmds.button(label="Close", command=lambda _: cmds.deleteUI(window))

    cmds.showWindow(window)


# Run the UI
create_recolor_ui()
