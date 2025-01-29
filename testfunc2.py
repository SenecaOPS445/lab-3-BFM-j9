#!/usr/bin/env python3
#Function that does not take argument or return value p2

def hello():
    print('Hello World')
    print('Inside a function')
    return

my_stuff = hello()
print('Stuff return from hello():',my_stuff)
print('the object my_stuff is of type:',type(my_stuff))