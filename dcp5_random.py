# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:50:15 2018

@author: Mahe
"""

def cons(a,b):
   return lambda f:f(a,b)

def car(f):
    return f(lambda a,b:a)

def cdr(f):
    return f(lambda a, b:b)

if __name__=='__main__':
    print("Enter two numbers separated by a comma\n")
    a,b=(int(n) for n in input().split(','))
    print(car(cons(a,b)))
    print(cdr(cons(a,b)))