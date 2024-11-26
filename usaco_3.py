# -*- coding: utf-8 -*-
"""Usaco#3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Sp6WqXIT-dVNubB6p-yYrEDYS1I9oCEh
"""

# with open("beads.in","r") as f:
#   length=f.readline().strip()
#   necklace=f.readline().strip()

# beads=[]
# length=int(length)

# for bead in necklace:
#   beads.append(bead)

# max_index_left=0
# max_index_right=0
# max_counter=0
# for i in range(0,length):
#   b1=i%length
#   starting_left=b1
#   b2=(b1+1)%length
#   starting_right=b2
#   still_going_left=True
#   still_going_right=True
#   left_counter=0
#   right_counter=0
#   j=0
#   found_non_white=False
#   color=''
#   while found_non_white==False:
#     check_index=starting_left-j
#     if check_index==-1:
#       check_index=length-1
#     if(beads[check_index]=='r' or beads[check_index]=='b'):
#       color=beads[check_index]
#       found_non_white=True
#       left_counter+=1
#     else:
#       j+=1
#       left_counter+=1
#   while still_going_left==True:
#     if(b1<0):
#       b1=28
#     if(beads[b1]==color or beads[b1]=='w'):
#       left_counter+=1
#       b1-=1
#     else:
#       still_going_left=False
#   j=0
#   found_non_white==False
#   color=''
#   while found_non_white==False:
#     check_index=starting_right+j
#     if check_index>28:
#       check_index=0
#     if(beads[check_index]=='r' or beads[check_index]=='b'):
#       color=beads[check_index]
#       found_non_white=True
#       right_counter+=1
#     else:
#       j+=1
#       right_counter+=1
#   while still_going_right==True:
#     if(b2>28):
#       b2=0
#     if(beads[b2]==color or beads[b2]=='w'):
#       right_counter+=1
#       b2+=1
#     else:
#       still_going_right=False
#   counter=left_counter+right_counter
#   if counter>max_counter:
#     max_counter=counter
# print(max_counter)

with open("beads.in","r") as f:
   length=int(f.readline().strip())
   necklace=f.readline().strip()
   beads=[]
for bead in necklace:
  beads.append(bead)
max_counter=0
for i in range(0,length):
  starting_left=i%29
  starting_right=(i+1)%29
  bead_counter=0
  curr_left=starting_left
  curr_right=starting_right
  still_going_left=True
  still_going_right=True
  color=''
  while still_going_left==True:
    if(beads[curr_left]=='w'):
      bead_counter+=1
      curr_left=(curr_left+1)%29
    elif((beads[curr_left]=='r' or beads[curr_left]=='b') and color==''):
      color=beads[curr_left]
      bead_counter+=1
      curr_left=(curr_left+1)%29
    elif(beads[curr_left]==color):
      bead_counter+=1
      curr_left=(curr_left+1)%29
    else:
      still_going_left==False