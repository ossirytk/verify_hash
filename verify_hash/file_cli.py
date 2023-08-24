import click
import sys
import os
import hashlib
#TODO consider chaining thse in one file
def compute_file_hash(file_path):
    '''calculates a hash for a file.'''
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
                h.update(f.read())
    return h.hexdigest()           

@click.command()
@click.option("--file1", required=True, help="file to get a hash for.")
@click.option("--file2", required=False,  help="File to compare hashes.")
def verify_hash(file1, file2):
    if file2 is None:
        print(compute_file_hash(file1))
    else :
        file1_hash = compute_file_hash(file1)
        file2_hash = compute_file_hash(file2)
        print(file1_hash)
        print(file2_hash)
        if file1_hash == file2_hash:
            print("File hashes match")
        else:
            print("File hashes don't match")

# Using the special variable
# __name__
if __name__ == "__main__":
    verify_hash()
