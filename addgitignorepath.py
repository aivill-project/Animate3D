import os, sys, argparse

argparse = argparse.ArgumentParser()
argparse.add_argument('-path', '--path', type=str, default='', help='Path to add to .gitignore')
args = argparse.parse_args()

def addgitignorepath(path):
    if os.path.exists(path):
        with open('.gitignore', 'a') as f:
            f.write(path + '\n')
    else:
        print('Path does not exist:', path)
        return False

    return True

if __name__ == '__main__':
    addgitignorepath(args.path)
    print('added a lin on .gitignore {} Done'.format(args.path))