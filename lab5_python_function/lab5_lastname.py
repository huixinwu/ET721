"""
Student's full name
Sep 16, Python functions
"""
import math
import random

# example 1: define a function to print a message. This a function that doesn't return nor pass a value 
def hellofunction():
    print("Welcome to function!")

# example 2: function that passes a username as argument, but it doesn't return any value
def greeting(username):
    print(f"Good afternoon {username}")

# example 3: function with default parameter, but it doesn't return any value
def usercountry(countryname="USA"):
    print(f"I am from {countryname}")

# example 4: function that passes and returns value
def triplenumber(num=0):
    return 3*num

#example 5: function that passes two numbers and check if the two numbers are divisible by each other. The function returns True if they are divisible and False if they are not divisible
def isdivisible(n1,n2):
    if(n1%n2 == 0 or n2%n1 == 0):
        return True
    else:
        return False

# example 6: function that passes a radius and returns the circumference
def circumference(radius=0):
    return 2*math.pi*radius

# example 8: function that returns a random number between 1 and 6
def rolldice():
    return random.randint(1,6) 

# call a function that doesn't return nor pass a value 
print("\n ---- Example 1 ----- ")
hellofunction()
hellofunction()

print("\n ---- Example 2 ----- ")
username = "peterpan123"
greeting(username)

print("\n ---- Example 3: function with default parameter ----- ")
usercountry("China")
usercountry()

print("\n ---- Example 4: function that passes a number and returns the triple of that number ----- ")
n = 9
print(f"The triple  of number {n} is {triplenumber(n)}")

print("\n ---- Example 5: function that passes two numbers and returns True or False ----- ")
n1 = 10
n2 = 50
check1 = isdivisible(n1,n2)
print(f"Is {n1} and {n2} divisibled? {check1}")

print("\n ---- Example 6: function that passes a radius and returns the circumference ----- ")
r = 5
c = circumference(r)
print(f"A circle with radius {r} has a circumference of {c:.2f}")

print("\n ---- Example 7: random numbers ----- ")
print(f"random number {random.random()}")
print(f"random uniform {random.uniform(-5,5)}")
print(f"random randint {random.randint(-10,10)}")

print("\n ---- Example 8: roll a dice ----- ")
print(f"dice number = {rolldice()}")