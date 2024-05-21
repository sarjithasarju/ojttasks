
def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)


def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        return content


file_name = "C:\\Users\\hp\\Desktop\\sarjitha\\21-5.2024\\example.txt"
content_to_write = "Hello, this is a sample text that will be written to a file."
write_to_file(file_name, content_to_write)

content_read = read_from_file(file_name)
print("Content read from file:")
print(content_read)
