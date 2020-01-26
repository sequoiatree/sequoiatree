import os
import shutil

def read(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def clear_dir(dir_path):
    for fsobj_name in os.listdir(dir_path):
        fsobj_path = os.path.join(dir_path, fsobj_name)
        if os.path.isfile(fsobj_path) or os.path.islink(fsobj_path):
            os.remove(fsobj_path)
        elif os.path.isdir(fsobj_path):
            shutil.rmtree(fsobj_path)
        else:
            assert False

def kebab_case(text):
    return text.lower().replace(' ', '-')
