'''
modify the origin_name and dest_name as you wanted.
put this file in the root director then run it.
'''
import os, sys, re
import _io
origin_name = 'PyHello'
dest_name = 'SFoam'
def get_sub_list(origin_name,dest_name):
    d = ((origin_name,dest_name),
        (origin_name.lower(),dest_name.lower()),
        (origin_name.upper(),dest_name.upper()),
        (origin_name.lower().capitalize(),dest_name.lower().capitalize()))
    return d

sl = get_sub_list(origin_name, dest_name) # sl short for sub list
print(sl[0][0]+" ==> "+sl[0][1])
print(sl[1][0]+" ==> "+sl[1][1])
print(sl[2][0]+" ==> "+sl[2][1])
print(sl[3][0]+" ==> "+sl[3][1])
print()
file_tree = os.walk(os.getcwd())
for path, dir_list, file_list in file_tree:
    if os.path.sep +'.' not in path:
        for filename in file_list:
            file = os.path.join(path,filename)
            if file != sys.argv[0] :
                print(os.path.relpath(file))
                if os.path.splitext(file)[1] not in ['.png','.doc']:
                    with open(file,'r') as f:
                        text = f.read()
                        text = text.replace(sl[0][0],sl[0][1]).replace(sl[1][0],sl[1][1]).replace(sl[2][0],sl[2][1]).replace(sl[3][0],sl[3][1])
                        # print(text)
                    with open(file,'w') as f:    
                        f.write(text)
                    print('    Substitution: done')
                else:
                    print('    Substitution: skip')
                if 'PYHELLO' in filename:
                    os.rename(file, os.path.join(path,filename.replace('PYHELLO','SFOAM')))
                    print('    Rename      : done')
                else:
                    print('    Rename      : skip')
                print()
        relpath_name = os.path.relpath(path)
        print(relpath_name)
        if "PYHELLO" in relpath_name:
            os.rename(relpath_name,relpath_name.replace('PYHELLO','SFOAM'))
            print('    Rename      : done')
        else:
            print('    Rename      : skip')
        print()


