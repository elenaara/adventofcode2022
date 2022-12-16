# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16
Advent of Code 2022
Day 10

@author: elenaara
"""

# "noop" does nothing, takes 1 cycle
# addx N modifies X, takes 2 cycles
def sum_cycles(commands):
    sum_cycle = []
    N = []
    cycle = 1
    for c in commands:
        if c[0] == 'addx':
            cycle += 2
            N.append(int(c[1]))
            sum_cycle.append(cycle)

        if c[0] == "noop":
            cycle += 1
    return N,sum_cycle

def signal_st(N,sum_cycle):
    int_cycles = [20,60,100,140,180,220]
    sum_signals = 0
    X = 1
    for i in range(sum_cycle[-1] + 2):
        if i in sum_cycle:
            X += N[sum_cycle.index(i)]


        if i in int_cycles:
            print(f"Value of X in cycle {i}: {X}")
            print(f"Signal strength in cycle {i}: {i*X}")
            sum_signals += i*X

    print(f"The sum of signal strengths is {sum_signals}")

def draw(N,sum_cycle):
    line = ""
    X = 1
    test = False
    position = 1
    for i in range(1,sum_cycle[-1] + 3):

        if i in sum_cycle:
            X += N[sum_cycle.index(i)]

        if len(line) >= 40:
            print(line)
            line = ""
            position = 1

        if position in range(X,X+3):
            line += "#"
        elif position not in range(X,X+3):
            line += "."

        position += 1


input_path = "C:/Users/earam/Desktop/adventofcode22/day10input.txt"
commands = [el.split() for el in open(input_path, 'r').readlines()]

def solve_pt1(commands):
    N, sum_cycle = sum_cycles(commands)
    signal_st(N,sum_cycle)

def solve_pt2(commands):
    N, sum_cycle = sum_cycles(commands)
    draw(N,sum_cycle)

solve_pt2(commands)

