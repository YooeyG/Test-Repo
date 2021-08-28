#Prints out location and whihc python interpreter currently using

import sys
import os


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('Ryan'))

print('Version of Python')
print(sys.version)

print('Virtual Environment')
print(sys.executable)

print("current directory")
print(os.getcwd())

print('git status')