import os
from os import path
import datetime
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


def getdate():
    return datetime.datetime.now()


def Create_file():
    if (path.exists(f'{desktop}\\My_Routine.txt')) == True:
        try:
            f = open(f"{desktop}\\My_Routine.txt", "a")
            f.write(f"""\n\n__________________ Today's date : {getdate()} __________________
Theory       = {Theory}
Cpp          = {Cpp}
Python       = {Python}
Korean       = {Korean}
Course       = {Courses}
Course name  = {Courses_name}\t\t\t\t\t\t\t\t\t\tStatus: {Status}
""")
            f.close()
        except:
            print("Error!!!")
    else:
        try:
            f = open(f"{desktop}\\My_Routine.txt", "a")
            f.write(f"""\t\t\t\t  ____________\n\t\t\t\t|| MY ROUTINE ||\n\n__________________ Today's date : {getdate()} __________________
Theory       = {Theory}
Cpp          = {Cpp}
Python       = {Python}
Korean       = {Korean}
Course       = {Courses}
Course name  = {Courses_name}\t\t\t\t\t\t\t\t\t\tStatus: {Status}
""")
            f.close()
        except:
            print("Error!!!")


print("\t\tYOUR ROUTINE\n(Please enter your answer in ' Yes ' or ' No ') .")
Theory = (input("\n\nDid you complete your Theory :")).upper()
Cpp = (input("\nDid you complete your Cpp :")).upper()
Python = (input("\nDid you complete your Python :")).upper()
Korean = (input("\nDid you complete your Korean :")).upper()
Courses = (input("\nAny extra courses :")).upper()
if Courses == "YES":
    Courses_name = input("\nEnter the course name :").upper()
else:
    Courses_name = "None"
Status_no = 0
if Theory == "YES":
    Status_no += 1
if Cpp == "YES":
    Status_no += 1
if Python == "YES":
    Status_no += 1
if Korean == "YES":
    Status_no += 1
if Courses == "YES":
    Status_no += 1
else:
    pass

if Status_no > 4:
    Status = "Very Good"
if Status_no < 2:
    Status = "Bad"
if Status_no > 2 and Status_no < 4:
    Status = "Good"
Create_file()

print("\n\tYour today's routine is complete..")
