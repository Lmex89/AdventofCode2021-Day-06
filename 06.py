#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ast import Dict, List


def read_file(file_name):
    lines = []
    with open(file_name, 'r') as fb:
        lines = fb.readlines()
        return lines


def get_numbers():
    lines_str = read_file('example.txt')
    numbers = []
    for line in lines_str:
        numbers_ = line.split(',')
        numbers.extend(int(n) for n in numbers_)
    return numbers

def day(state):
    
    for i,s in enumerate(state,start=0):
        if state[i] != 0: 
            state[i] -= 1
        else:
            state[i] = 6
            state.append(9)

    return state

def main2(days):
    
    initial_state = get_numbers()
    state=None
    for _ in range(days):
        state = day(initial_state)
    print(len(state))


def hast_dict(list_initial_state ):
    result = {i: 0 for i in range(9)}
    for item in list_initial_state:
        if item in result:
            result[item] +=1 
    return result

def day(initial_statate):
    
    new_fish = initial_statate[0] 
    for i in range(1,len(initial_statate)):
        initial_statate[i-1]=initial_statate[i] 
    
    if initial_statate[8] != 0:
        initial_statate[8] -=1
  
    initial_statate[6] += new_fish
    initial_statate[8] = new_fish
    return initial_statate



def main():
    initial_state = get_numbers()
    dict_initial_state = hast_dict(initial_state)
    
    for _ in range(1,257):
        dict_initial_state=day(dict_initial_state)
        
    result = sum(dict_initial_state.values())
    
    print(f"la suma de lanterfish is : {result}")
main()