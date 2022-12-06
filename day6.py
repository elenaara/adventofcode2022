# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 08:48:03 2022
Advent of Code 2022
Day 6

@author: elenaara
"""

def find_marker(line):
    " Find first position in a string where last 4 letters read are different"
    letters_list = list()
    # counter for position in the string
    p = 0

    for letter in line:

        p += 1
        letters_list.append(letter)

        if len(set(letters_list[p-14:p])) == 14:
            print(letter)
            print(f"First marker is detected on character {p}")
            break

in1 = open("C:/Users/earam/Desktop/adventofcode22/day6input.txt","r")
for line in in1:
    find_marker(line)

