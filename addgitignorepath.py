import os

def addgitignorepath(path):
    if os.path.exists(path):
        with open('.gitignore', 'a') as f:
            f.write(path + '\n')
    else:
        print('Path does not exist')