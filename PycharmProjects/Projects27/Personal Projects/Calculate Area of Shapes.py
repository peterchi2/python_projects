'''
This program will calculate the area of a shape.
I have included a triangle, circle, square, and rectangle.
'''

from math import pi
from datetime import datetime
dfdf

#Variables used globally
now = datetime.now()
hint = "Don't forget to include the correct units! \nExiting..."

#define area functions here
def circle():
    radius = float(raw_input("Enter radius: "))
    area = pi * radius ** 2
    print("Area: %s \n%s" % (round(area, 2), hint))

def triangle():
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = 0.5 * base * height
    print("Area: %s \n%s" % (area, hint))

def square():
    side = float(raw_input("Enter one side: "))
    area = side ** 2
    print("Area: %s \n%s" % (area, hint))

def rectangle():
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = base * height
    print("Area: %s \n%s" % (area, hint))

print("The calculator is starting now!")
print("The current time is: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)

option = raw_input("Enter C for circle, T for triangle, R for rectangle, S for square: ")
option = option.upper()

if option == "C":
    circle()
elif option == "T":
    triangle()
elif option == "R":
    rectangle()
elif option == "S":
    square()
else:
    print("You entered garbage, GTFO!")
