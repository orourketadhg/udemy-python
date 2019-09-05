#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "05/09/2019"

import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        print("+" * 40)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-5].split(' - ')
            print(song_details)
        print("+" * 40)

    # print(directories)
    # print(files)
    # input()

    # for f in files:
    #     print("\t{}".format(f))
