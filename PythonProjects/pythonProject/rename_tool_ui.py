import maya.cmds as cmds


def rename_objects(sequence):
    """
    Renames selected objects based on the provided naming sequence.
    """
    index = 1
    sels = cmds.ls(sl=True)
    if not sels:
        cmds.warning("No objects selected.")
        return

    # Count the number of '#' characters in the sequence
    spacing_amt = sequence.count("#")
    if spacing_amt == 0:
        cmds.warning("Invalid naming sequence. Must include '#' characters.")
        return

    spacing_string = "#" * spacing_amt
    parts = sequence.split(spacing_string)

    for sel in sels:
        # Format the index with leading zeros
        formatted_index = f'{index:0{spacing_amt}d}'  # Adds leading zeros based on spacing_amt
        # Construct the new name
        new_name = parts[0] + formatted_index + parts[1]
        # Rename the object
        cmds.rename(sel, new_name)
        print(f"Renamed {sel} to {new_name}")
        index += 1


def create_renaming_ui():
    """
    Creates a UI to specify a naming sequence and rename selected objects.
    """
    window_name = "RenameUI"

    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    window = cmds.window(window_name, title="Renaming Tool", widthHeight=(300, 150))

    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Enter Naming Scheme (e.g., 'Leg_##_Jnt'):", align="left")
    naming_field = cmds.textField(text="Leg_##_Jnt")

    cmds.separator(height=10, style="in")

    cmds.button(
        label="Rename Selected",
        command=lambda _: rename_objects(cmds.textField(naming_field, query=True, text=True))
    )

    cmds.separator(height=10, style="in")

    cmds.button(label="Close", command=lambda _: cmds.deleteUI(window))

    cmds.showWindow(window)


# Run the UI
create_renaming_ui()
