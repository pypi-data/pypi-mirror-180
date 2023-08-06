import sys
import os

def mkdir(path): 
    os.system(f"mkdir {path}")

def chdir(path):
    os.system(f"chdir {path}")

def rmdir(path):
    os.system(f"rmdir {path}")

def getcwd():
    os.system("chdir")

def rename(name, newname):
    os.system(f"rename {name} {newname}")

def makedirs(path):
    os.makedirs(path)

def replace(pathA, pathB):
    os.system(f"replace {pathA} {pathB}")

def listdir():
    os.listdir()

def remove(path):
    os.remove(path)

def removedirs(path):
    os.removedirs(path)

def stat(path):
    os.stat(path)

def viewfile(path):
    os.system(f"type {path}")

def copy(pathA, pathB):
    os.system(f"copy {pathA} {pathB}")