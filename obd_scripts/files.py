import os

def write_value(val):
    script_dir = os.path.dirname(__file__)
    rel_path = "testFile"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path,"a+")
    file_object.write(str(val)+"\n")
    file_object.close()

def read_values():
    script_dir = os.path.dirname(__file__)
    rel_path = "testFile"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path,"r")
    lines = file_object.readlines()
    val_to_use = []
    for line in lines:
        val_to_use.append(int(line))
    file_object.close()
    return val_to_use