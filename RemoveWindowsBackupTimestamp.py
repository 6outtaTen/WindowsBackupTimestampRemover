import os, pathlib

print("------------------------------")
print("Tool for removing windows backup timestamp from file and folder names")
print("Author: 6outtaTen\n------------------------------\n\n")

print("Note that the script will go through every single folder in a given directory, and through every folder inside that folder etc...")
search_path = input("Enter search directory: ")

for folder, sub_folders, files in os.walk(search_path):
    for f in files:
        if "UTC" in f:
            
            try:
                # The first bracket index marks the beginning of the fucked up way that windows saves file backups
                first_bracket_index = f.find("(")
                file_extension = pathlib.Path(f).suffix

                old_file_name = f
                new_file_name = f[:first_bracket_index-1] + file_extension # -1 because we need to remove the space before the first bracket

                current_path = os.path.join(folder, f)
                new_path = os.path.join(folder, new_file_name)

                print(f"Renaming {old_file_name} to {new_file_name}")
                os.rename(current_path, new_path)
            except:

                # This will be ran when there's already a file with the same name, essentialy creates a copy with a `(1)` at the end (not a perfect soultion, I know)
                # This is the only exception I have ran into, but I am not singling it out just in case


                # The first bracket index marks the beginning of the fucked up way that windows saves file backups
                first_bracket_index = f.find("(")
                file_extension = pathlib.Path(f).suffix

                old_file_name = f
                new_file_name = f[:first_bracket_index-1] + " (1)" + file_extension # -1 because we need to remove the space before the first bracket

                current_path = os.path.join(folder, f)
                new_path = os.path.join(folder, new_file_name)

                print(f"Renaming failed! Adding (1) to the new name")
                os.rename(current_path, new_path)         
            