# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:25:04 2024

@author: SATHIYAPRIYAN
"""
import random

Upper_letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Lower_letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=["!","@","#","$","%","&","*",".","?"]
numbers=["1","2","3","4","5","6","7","8","9","0"]

n_Upper_letters=int(input("Enter how Upper letter you want:"))
n_Lower_letters=int(input("Enter how Lower letter you want:"))
n_symbols=int(input("Enter how many symbols you want:"))
n_numbers=int(input("Enter how many numbers you want:"))

password=" "

for i in range(1,n_Upper_letters+1):
    char=random.choice(Upper_letters)
    password+=char
    
for i in range(1,n_Lower_letters+1):
    char=random.choice(Lower_letter)
    password+=char
    
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
    
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char

print(password)