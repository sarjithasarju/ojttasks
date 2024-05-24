class FileProcessor:
    @staticmethod
    def read_file(file_path):
        """Reads data from a file and returns its content."""
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"The file {file_path} does not exist."
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def write_file(file_path, data):
        """Writes data to a file. If the file exists, it will be overwritten."""
        try:
            with open(file_path, 'w') as file:
                file.write(data)
            return f"Data written to {file_path} successfully."
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def append_file(file_path, data):
        """Appends data to an existing file. If the file does not exist, it will be created."""
        try:
            with open(file_path, 'a') as file:
                file.write(data)
            return f"Data appended to {file_path} successfully."
        except Exception as e:
            return f"An error occurred: {e}"


file_path = 'example.txt'


print(FileProcessor.write_file(file_path, "Hello, World!\n"))


print(FileProcessor.append_file(file_path, "This is an appended line.\n"))


print(FileProcessor.read_file(file_path))
