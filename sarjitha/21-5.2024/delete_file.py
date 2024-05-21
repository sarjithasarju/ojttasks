import os

def delete_file(file_name):
 
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} has been deleted successfully.")
    else:
        print(f"The file {file_name} does not exist.")

file_name = "C:\\Users\\hp\\Desktop\\sarjitha\\21-5.2024\\example.txt"
delete_file(file_name)
