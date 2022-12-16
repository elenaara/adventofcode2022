# -*- coding: utf-8 -*-
"""
Created on Dec 15
Advent of Code 2022
Day 7

@author: elenaara
"""

# PART 1

def most_100000_3dir(dir_dict):
    size_list = list()
    for key in dir_dict:
        if int(dir_dict[key]) <= 100000:
            size_list.append(int(dir_dict[key]))
    size_list.sort()
    top3_sum = 0
    # counter top3
    n = 0
    idx = 0
    top3_sum = sum(size_list)
    print(f"The sum of the total sizes of directories with a total size of at most 100000 is {top3_sum}")


input_path = "C:/Users/earam/Desktop/adventofcode22/day7input.txt"


path = ""
path_list = ["/"]
current_dicts = []
dir_size = dict()

with open(input_path, "r") as in1:
    for line in in1:
        line = line.strip()
        if line.startswith("$ cd"):
            line = line.split("cd")
            dire = line[1].lstrip()

            if dire == "/":
                path = "/"
                current_dicts = ["/"]


            elif dire == "..":
                path = path.split("/")[:-2]
                new_path = ""
                for i in path:
                    new_path += i
                    new_path += "/"

                path = new_path
                current_dicts.pop()
                #print(current_dicts)

            else:
                path += dire
                path += "/"
                path_list.append(path)
                current_dicts.append(path)
                #print(current_dicts)

            # initialize dict entry for this dir if it does not exist
            if path not in dir_size:
                dir_size[path] = 0


        if line[0].isdigit():
            size = int(line.split(" ")[0])
            for d in current_dicts:
                dir_size[d] += size


most_100000_3dir(dir_size)

# PART 2
total_space = 70000000
needed_space = 30000000

def remove_dir(total_space,needed_space,dir_size):

    used_space = dir_size["/"]
    free_space = total_space - used_space
    space_to_free = needed_space - free_space

    possible_dirs = []
    for key in dir_size:
        if dir_size[key] > space_to_free:
            possible_dirs.append(dir_size[key])

    print(f"The directory to remove has a size of {min(possible_dirs)}")

remove_dir(total_space, needed_space, dir_size)