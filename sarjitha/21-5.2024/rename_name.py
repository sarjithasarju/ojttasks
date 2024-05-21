import os

def rename_file(old_name, new_name):

    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}' successfully.")
    else:
        print(f"The file '{old_name}' does not exist.")


old_name = "old_name.txt"
new_name = "new_name.txt"
rename_file(old_name, new_name)
