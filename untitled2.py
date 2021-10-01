#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:42:31 2021

@author: zhaomingli
"""


def fibonacci_recursive(n):
    
    if n<0:
        print("error input")
    # Check if input is 0 then it will print incorrect input
        
    elif n==0:
        return 0
    # Check if n is 0 then it will return 0
    
    elif n==1 or n==2:
        return 1
    # Check if n is 1 or 2 it will return 1
    
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)


for i in range(30):
    print('The '+str(i+1)+" fibonacci number is: ")
    print(fibonacci_recursive(i+1))







def fibonacci_ite(n):
    
    a=0
    b=1
    
    for i in range(n-1):
        a,b=b,a+b
    return b
            


