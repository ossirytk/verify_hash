import click
import sys
import os
import hashlib


def compute_hash_over_dir(dirname):
    '''dirname will be scanned recursively and 
    hash over files will be returned.'''
    h = hashlib.sha256()
    for root, dirs, files in os.walk(dirname):
        dirs[:] = []
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                h.update(f.read())
    return h.hexdigest()


def calculate_folder_hash(path):
    print("Hashkey for folder: {}".format(path))
    hash = compute_hash_over_dir(path)
    print(hash)


def compare_folders(path1, path2):
    print("Hashkey for folder: {}".format(path1))
    hash = compute_hash_over_dir(path1)
    print(hash)

    print("Hashkey for folder: {}".format(path2))
    hash2 = compute_hash_over_dir(path2)
    print(hash2)

    if hash == hash2:
        print("The Hashkeys match")
    else:
        print("The Hashkeys don't match.")
#TODO commands to calculate hash for a file and folder to learn click
@click.command()
@click.option("--dir1", required=True, help="Directory to get a hash for.")
@click.option("--dir2", required=False,  help="Directory to compare hashes.")
def verify_hash(dir1, dir2):
    if dir2 is None:
        isExist = os.path.exists(dir1)
        if isExist:
            calculate_folder_hash(dir1)
        else:
            print("Can not find given path {}".format(dir1))
    else :
        isExist = os.path.exists(dir1)
        isExist2 = os.path.exists(dir2)
        if isExist and isExist2:
            compare_folders(dir1, dir2)
        else:
            if not isExist:
                print("Can not find given path {}".format(dir1))
            if not isExist2:
                print("Can not find given path {}".format(dir2))


# Using the special variable
# __name__
if __name__ == "__main__":
    verify_hash()
