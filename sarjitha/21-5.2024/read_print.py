def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{file_name}'.")

file_name = "C:\\Users\\hp\\Desktop\\sarjitha\\21-5.2024\\example.txt"
read_file(file_name)
