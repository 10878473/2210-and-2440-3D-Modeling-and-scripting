import maya.cmds as cmds

# Example sequence string for reference
sequence = "Leg_L_#####_Ctrl_grp"
index = 1
sels = cmds.ls(sl=True)

for sel in sels:
    print(f"Renaming: {sel}")

    # Count the number of '#' characters in the sequence
    spacingamt = sequence.count("#")
    spacingstring = "#" * spacingamt

    # Split the sequence around the '#' characters
    parts = sequence.split(spacingstring)

    # Format the index with leading zeros
    formatted_index = f'{index:0{spacingamt}d}'  # Adds leading zeros based on spacingamt

    # Construct the new name
    newname = parts[0] + formatted_index + parts[1]

    # Rename the object
    cmds.rename(sel, newname)
    print(f"Renamed to: {newname}")

    index += 1

    #Create a function that requires an argument string in the format "Name_##_NodeType" that will be used to
    # specify the naming scheme. For example, the argument for a leg joint chain might be named "Leg_##_Jnt".
    #The script will look for the "#" characters and replace them with the next number in a sequence.
    #The number of "#" characters will also determine where number padding is needed, meaning the inserted
    #number must be at least as many digits as there are "#" characters. For example, if two "##" characters were input,
    #then the resultant number output must be at least 2 digits. Numbers that are too small are to be preceded by a zero
    # (i.e. "Leg_##_Jnt" would begin converting to "Leg_01_Jnt", "Leg_02_Jnt", ... , "Leg_09_Jnt", "Leg_10_Jnt", etc.
    # "Leg_####_Jnt" would convert to "Leg_0001_Jnt", etc.

