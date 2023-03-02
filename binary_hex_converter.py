# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:24:44 2023

@author: David
"""
import numpy as np



def deci_to_bi(num):
    binary_num = ""
    arr = []
    temp = int(num)
    while temp >= 2:
        arr.append(int(temp % 2))
        temp = int(temp/2)
    arr.append(temp)
    arr.reverse()
    for x in arr:
        binary_num += str(x)
    return(binary_num)

def bi_to_hex(num):
    dif = (4-int(len(num)%4))%4
    hex_num=""
    arr = []
    
    power = 3
    temp = 0
    while dif != 0:
        dif -=1
        power -=1
    
    for x in num:
        if x == '1':
            temp += pow(2,power)
             
        if power == 0:
            power = 4
            arr.append(temp)
            temp = 0
            
        power -=1    
            
    for x in arr:
        if x == 15:
            hex_num += 'F'
        elif x == 14:
            hex_num += 'E'
        elif x == 13:
            hex_num += 'D'
        elif x == 12:
            hex_num += 'C'
        elif x == 11:
            hex_num += 'B'
        elif x == 10:
            hex_num += 'A'
        else:
            hex_num += str(x)
           
    return(hex_num)
        
    
        
         

decimal_num = input("enter number: ")
decimal_num = int(decimal_num)


print (deci_to_bi(decimal_num))
print(bi_to_hex(deci_to_bi(decimal_num)))