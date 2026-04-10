import os
import sys
import subprocess
import argparse
def startup():
    print("Welcome to PYOS!"
          "\nType 'help' for a list of commands.")
def help():
    print("Avaliable commands:" \
    "\nhelp - shows this message"
    "\nadd - adds two numbers together"
    "\nprint - prints a message to the console"
    "\nsub - subtracts two numbers"
    "\nmul - multiplies two numbers"
    "\nshutdown - shuts down PYOS")
def add(a, b):
    return a + b
def print(message):
    sys.stdout.write(message + "\n")
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def shutdown():
    print("Shutting down PYOS...")
    sys.exit()
startup()
while True:
    command = input(">>> ")
    if command == "help":
        help()
    elif command == "add":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        add(num1, num2)
        print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
    elif command == "print":
        message = input("Enter the message to print: ")
        print(message)
    elif command == "sub":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        sub(num1, num2)
        print(f"The difference of {num1} and {num2} is {sub(num1, num2)}")
    elif command == "mul":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        mul(num1, num2)
        print(f"The product of {num1} and {num2} is {mul(num1, num2)}")
    elif command == "shutdown":
        shutdown()