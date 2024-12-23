# -*- coding: utf-8 -*-
"""Usaco#4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JZ7_azC4q8KEeoRk233NUTpvlNpQQN_i
"""

with open('file.in', 'r') as file:
    lines = file.readlines()

total_cows, total_canes = map(int, lines[0].split())
cow_heights = list(map(int, lines[1].split()))
cane_heights = list(map(int, lines[2].split()))
initial_cane_heights = cane_heights[:]

for i in range(total_canes):
    while cane_heights[i] > 0:
        any_cow_ate = False
        for j in range(total_cows):
            cane_eaten_so_far = initial_cane_heights[i] - cane_heights[i]

            if cow_heights[j] <= initial_cane_heights[i]:
                chunk_to_eat = cow_heights[j] - cane_eaten_so_far
            else:
                chunk_to_eat = initial_cane_heights[i] - cane_eaten_so_far

            if chunk_to_eat > 0 and cane_heights[i] > 0:
                cow_heights[j] += chunk_to_eat
                cane_heights[i] -= chunk_to_eat

            if cane_heights[i] == 0:
                break
        if not any_cow_ate:
            break
for cow in cow_heights:
   print(cow)