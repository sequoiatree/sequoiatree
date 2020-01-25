def read(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write(file_path, *args, **kwargs):
    with open(file_path, 'w') as file:
        file.write(*args, **kwargs)
