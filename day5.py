# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:26:03 2022
Advent of Code 2022 
Day 5

@author: elenaara
"""

def reorganize_crates(crates_list, l):
    reorg_crates = dict()
    for i in range(0,l):
        reorg_crates[i+1] = list()
    for line in crates_list:
        for i in range(0,l):
            if len(line) > i:
                if line[i] != "":
                   reorg_crates[i+1].append(line[i].strip())
                if line[i] == "" and line[i+1] == "" and line[i+2] == "" and line[i+3] == "":
                    line.remove(line[i])
                    line.remove(line[i])
                    line.remove(line[i])
    return reorg_crates

def move_crates(crates,n,fr,to):
    #l = len(crates[1])
    # For the stack where we want to get the crate
    # Get first place that is not empty
    count = 0
    while count < n:
        if crates[fr]:
            x = crates[fr][0]
            crates[to].insert(0,x)
            #idx = crates[fr].index(i)
            crates[fr].remove(x)
            count += 1
    return crates
        
    
    
    
        
crates = list()
with open("C:/Users/earam/Desktop/adventofcode22/day5example.txt","r") as in1:
    for line in in1:
        if "[" in line:

            line = line.strip("\n")
            line = line.split(" ")
            crates.append(line)
            
        elif line.startswith(" 1"):
            line = line.strip(" ")
            line = line.strip("\n")
            line = line.replace(" ", "")
            length = len(list(line))
            crates_reorg = reorganize_crates(crates, length)
            crates_new = dict(crates_reorg.copy())
        
        elif line.startswith("move"):
            line = line.strip("\n")
            line = line.split(" ")
            # how many
            n = int(line[1])
            # from where
            fr = int(line[3])
            # to
            to = int(line[5])
            crates_new = move_crates(crates_new,n,fr,to)

# Print result, first letter of each stack
final_arr = ""
for stack in crates_new:
    x = crates_new[stack][0]
    x = x.replace("[", "")
    x = x.replace("]", "")
    final_arr += x


print(f"Final arrangement: {final_arr}")
# Does not work :/


# PART 2
def new_crate_move(crates,n,fr,to):
    # For the stack where we want to get the crate
    # Get first place that is not empty
    count = 0
    if crates[fr]:
        x = crates[fr][0:n]
        for i in list(reversed(x)):
            crates[to].insert(0, i)
            crates[fr].remove(i)

    return crates


crates = list()
with open("C:/Users/earam/Desktop/adventofcode22/day5input.txt", "r") as in1:
    for line in in1:
        if "[" in line:

            line = line.strip("\n")
            line = line.split(" ")
            crates.append(line)

        elif line.startswith(" 1"):
            line = line.strip(" ")
            line = line.strip("\n")
            line = line.replace(" ", "")
            length = len(list(line))
            crates_reorg = reorganize_crates(crates, length)
            crates_new = dict(crates_reorg.copy())

        elif line.startswith("move"):
            line = line.strip("\n")
            line = line.split(" ")
            # how many
            n = int(line[1])
            # from where
            fr = int(line[3])
            # to
            to = int(line[5])
            crates_new = new_crate_move(crates_new, n, fr, to)

# Print result, first letter of each stack
final_arr = ""
for stack in crates_new:
    x = crates_new[stack][0]
    x = x.replace("[", "")
    x = x.replace("]", "")
    final_arr += x

print(f"Final arrangement with new crane: {final_arr}")