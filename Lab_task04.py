# lab_task 04
# lab_task 04
"""Q:no:2, write a python program to find the average of all the numbers in the following list.
my_list=[3,1,0,9,5,2,6,9,8,7]
use a for loop to calculate the sum of the numbers and  then find and print their average."""

my_list=[3,1,0,14,5,2,16,19,28,77]
total = 0
for num in my_list:
    total = total + num
average=total/len(my_list)
print("average:",average)