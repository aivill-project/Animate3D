import os
import sys

import argparse

argparse = argparse.ArgumentParser(description = 'renameCapturePics')
argparse.add_argument('-path', '--path', help='path to the folder', required=True)
args = argparse.parse_args()

def renameCapturePics(path):
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            os.rename(os.path.join(path, file), os.path.join(path, file.replace(" ", "_")))

renameCapturePics(args.path)