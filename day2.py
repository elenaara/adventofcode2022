# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:05:46 2022
Advent of Code 2022 
Day 2

@author: elenaara
"""

#%% Part 1

import pandas as pd

in1 = open("C:/Users/Admin/Desktop/aoc/inputday2.txt")

game_results = pd.DataFrame({"op":["rock","rock","rock","paper","paper","paper","scissors","scissors","scissors"],
                            "you":["rock","paper","scissors","rock","paper","scissors","rock","paper","scissors"],
                            "result":[3,6,0,0,3,6,6,0,3]})

game_dict = {"A":"rock","X":"rock",
             "B":"paper","Y":"paper",
             "C":"scissors","Z":"scissors"}

game_points = {"A":1,"X":1,
        "B":2,"Y":2,
        "C":3,"Z":3}

draw = 3
win = 6

total_points = 0

for line in in1:
    line = line.strip()
    line = line.split(" ")

    op = line[0]
    you = line[1]
    
    result = game_results.loc[(game_results['op'] == game_dict[op]) & (game_results['you'] == game_dict[you])]['result']
    result = list(result)[0]
    total_points += result
    total_points += game_points[you]
    
    
print('The total number of points is {}'.format(total_points))

#%% Part 2

import pandas as pd

in1 = open("C:/Users/Admin/Desktop/aoc/inputday2.txt")

game_results = pd.DataFrame({"op":["rock","rock","rock","paper","paper","paper","scissors","scissors","scissors"],
                            "you":["rock","paper","scissors","rock","paper","scissors","rock","paper","scissors"],
                            "result":[3,6,0,0,3,6,6,0,3]})

game_dict = {"A":"rock","X":0,
             "B":"paper","Y":3,
             "C":"scissors","Z":6}

game_points = {"rock":1,
               "paper":2,
               "scissors":3}

draw = 3
win = 6

total_points = 0

for line in in1:
    line = line.strip()
    line = line.split(" ")

    op = line[0]
    you = line[1]
    
    result = game_results.loc[(game_results['op'] == game_dict[op]) & (game_results['result'] == game_dict[you]),'you']
    result = list(result)[0]
    total_points += game_points[result]
    total_points += game_dict[you]
    
    
print('The total number of points is {}'.format(total_points))