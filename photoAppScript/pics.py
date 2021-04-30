import os

def find_all():
    directory = os.fsencode(".")
    all_files = [os.fsdecode(file).lower() for file in os.listdir(directory)]
    files_to_open = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if(filename.lower().endswith(".cr2")) and (filename.lower().replace(".cr2",".xmp") in all_files):
            files_to_open.append(filename)
        else:
         continue
    return files_to_open

def refined_find_all():
    directory = os.fsencode(".")
    all_files = [os.fsdecode(file).lower() for file in os.listdir(directory)]
    testing = list(filter(lambda x: x.lower().endswith("cr2") and x.lower().replace(".cr2",".xmp") in all_files, all_files))
    return testing


files_to_open = find_all()
os.system("open {}".format(*files_to_open))