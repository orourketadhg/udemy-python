#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"

import os
import fnmatch


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


# my_music_file = find_music('music', 'emp3')

for f in find_music('music', 'emp3'):
    print(f)
