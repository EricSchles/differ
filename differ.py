import os
import argparse

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    if i != 0:
        return i+1
    else:
        return i

def diff(cur,past):
    with open(cur,"r") as f:
        cur_contents = f.read()
    with open(past,"r") as f:
        past_contents = f.read()

    for ind,val in enumerate(cur_contents):
        if val != past_contents[ind]:
            return "different"
    return "same"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("root",nargs=1)
    parser.add_argument("files_to_check",nargs="*")
    args = parser.parse_args()
    root = args.root[0]
    files_to_check = args.files_to_check

    files_found = dict((el,[]) for el in files_to_check)

    for rootdir,dir,files in os.walk(root):
        for file in files:
            if file in files_to_check:
                if files_found[file] == []:
                    files_found[file].append(file)
                else:
                    for checked in files_found[file]:
                        cur_len = file_len(file)
                        past_len = file_len(file)
                    
