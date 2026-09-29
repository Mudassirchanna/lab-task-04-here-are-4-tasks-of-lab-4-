# lab_task 04
"""Q:no:3,create a list of student names:
students=["Ali","Ahmed","Sara","Ayesha","Bilal"]
 ask the user to enter a student name .
if the name exists,display:
student found
otherwise
student not found"""

students_list=["Ali","Ahmed","Sara","Ayesha","Bilal"]
name=input("enter a student name : ")
if name in students_list:
    print("student found")
else:
    print("student not found")