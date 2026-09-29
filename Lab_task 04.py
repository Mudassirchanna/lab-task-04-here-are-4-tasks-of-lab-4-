# lab_task 04
"""Q :no:1, write a python program to find the smallest number in the following
list using for loop.
my_list=[3,1,0,9,5,2,6,4,9,8,7]
print the smalleat number as the output"""

my_list=[3,33,10,11,56,5,44,6,9,78,20,]
smalest = my_list [10]
for  num in my_list:
    if num < smalest :
        smalest = num
        print(num)        