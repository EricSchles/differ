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
    different = []
    total_count = 0
    for rootdir,dir,files in os.walk(root):
        for file in files:
            filename = file
            file = os.path.join(rootdir,file)
            if file in files_to_check:
                total_count += 1
                if files_found[file] == []:
                    files_found[filename].append(file)
                else:
                    for checked in files_found[filename]:
                        cur_len = file_len(file)
                        past_len = file_len(file)
                        if cur_len != past_len:
                            different.append([checked,file,"different"])
                            continue
                        else:
                            if diff(checked,file) == "different":
                                different.append([checked,file,"different"])
                    files_found[filename].append(file)
                    


    for elem in different:
        print "For "+elem[0]+" and "+elem[1]+" the files are different"
    
    print "There were ",len(different),"files"
    print "There were ",total_count,"files"
    print "The ratio of changed to unchanged files was:"+len(different)/float(total_count)
        
