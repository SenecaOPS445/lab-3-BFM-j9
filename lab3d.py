#!/usr/bin/env python3
#Author ID: Jowusu9 
#Script Purpose: is to create a Python function that can return the free disk space on a Linux system's root directory.


import subprocess

def free_space():
        result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()

if __name__ == "__main__":
    print(f"Free space on root directory: {free_space()}")
