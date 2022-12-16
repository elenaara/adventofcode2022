# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:27:56 2022

Advent of Code 2022 
Day 8

@author: elenaara
"""

import numpy as np


def checkSameDiag(ma, coords_x, coords_y):
    "Function to check if two integers are on the same diagonal of the matrix "
    
    # Storing indexes of x in I, J
    # Storing Indexes of y in P, Q
    

    I, J = coords_x[0],coords_x[1]
    P, Q = coords_y[0],coords_y[1]
                 
    # Condition to check if the
    # both the elements are in
    # same diagonal of a matrix
    if P-Q == I-J or P + Q == I + J:
        return True
    else:
        return False



def is_visible(coords_x, ma):
    visible = False
    visible_right = True
    visible_left = True
    visible_top = True
    visible_bottom = True

    # Get dim of matrix
    m, n = ma.shape

    # Get coords and value of the point
    r, c = coords_x[0], coords_x[1]
    value = ma[r, c]

    # If point is in the extremes, it is visible
    if r == 0 or r == (m - 1) or c == 0 or c == (n - 1):
        visible = True

    else:
        # Check right
        for i in range(1, n):
            # check if location is within boundary
            if 0 <= c + i < n:
                n_value = ma[r, (c + i)]
                if n_value >= value:
                    visible_right = False
                    break

        # Check left
        for i in range(-n, 0):
            # check if location is within boundary
            if 0 <= c + i < n:
                n_value = ma[r, (c + i)]
                if n_value >= value:
                    visible_left = False
                    break

        # Check top
        for i in range(1, m):
            # check if location is within boundary
            if 0 <= r + i < m:
                n_value = ma[(r + i), c]
                if n_value >= value:
                    visible_top = False
                    break


        # Check bottom
        for i in range(-m, 0):
            # check if location is within boundary
            if 0 <= r + i < m:
                n_value = ma[(r + i), c]
                if n_value >= value:
                    visible_bottom = False
                    break

    if visible_right or visible_left or visible_top or visible_bottom:
        visible = True

    return (visible)

def scenic_score(coords_x, ma):

    score_right = 0
    score_left = 0
    score_top = 0
    score_bottom = 0

    # Get dim of matrix
    m, n = ma.shape

    # Get coords and value of the point
    r, c = coords_x[0], coords_x[1]
    value = ma[r, c]

    # Check right
    for i in range(1, n):
        # check if location is within boundary
        if 0 <= c + i < n:
            n_value = ma[r, (c + i)]
            score_right += 1
            if n_value >= value:
                #score_right -= 1
                break


    # Check left
    for i in reversed(range(-n, 0)):
        # check if location is within boundary
        if 0 <= c + i < n:
            n_value = ma[r, (c + i)]
            score_left += 1
            if n_value >= value:
                #score_left -= 1
                break

    # Check top
    for i in reversed(range(-m, 0)):
        # check if location is within boundary
        if 0 <= r + i < m:
            n_value = ma[(r + i), c]
            score_top += 1
            if n_value >= value:
                #score_top -= 1
                break

    # Check bottom
    for i in range(1, m):
        # check if location is within boundary
        if 0 <= r + i < m:
            n_value = ma[(r + i), c]
            score_bottom += 1
            if n_value >= value:
                #score_bottom -= 1
                break
    score = score_right*score_left*score_top*score_bottom
    #print(score_right)
    #print(score_left)
    #print(score_top)
    #print(score_bottom)

    return(score)



input_path = "C:/Users/earam/Desktop/adventofcode22/day8input.txt"


trees_list = []
line_list = []

# Read matrix
with open(input_path,"r") as in1:
    for line in in1:
        if line_list:
            trees_list.append(line_list)
            line_list = []
        line = line.strip()
        for i in line:
            line_list.append(i)
    # append last line
    trees_list.append(line_list)


trees_matrix = np.array(trees_list)
m, n = trees_matrix.shape
v_trees = 0
score_list = []
for r in range(0,m):
    for c in range(0,n):

        if is_visible([r,c],trees_matrix):
            #print(trees_matrix[r,c])
            v_trees += 1
            score = scenic_score([r, c], trees_matrix)
            score_list.append(score)



print(v_trees)
print(max(score_list))

