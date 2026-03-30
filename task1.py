"""
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.
"""

def A():
    print("Hello")

def B():
    print("How are you")

def C():
    print("Hi")

user_input = input("Please enter a letter from A to C")

if user_input == 'a':
    A()
elif user_input == 'b':
    B()
elif user_input == 'c':
    C()
    

