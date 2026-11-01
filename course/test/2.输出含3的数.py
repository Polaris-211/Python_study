# -*- coding: utf-8 -*-
"""
Spyder Editor
打印出 打印出 1~ 1000之间 包含 3的数字 ；


如果 3是连在一起的（如果3是连在一起的如 233）则在数字前加上&；


如果这个数字是质则在后加上*, 例:（3,13*,23*,&33,43*...&233*...)
This is a temporary script file.
"""
def is_3 (a):
    s = str(a)
    return '3' in s
      
    
def is_connecting (a):
    s = str(a)
    return '33' in s

def is_prime (a):
    if a <= 1 :
        return False
        
    flag = 0
    for n in range (2, a):
        if a%n == 0 :
            flag+=1
    if flag == 0 :
        return True
    else :
        return False
            
m = int (input())
if m == 1 :
    for a in range (1, 1001):
        if is_3 (a):
            print(a)

if m == 2 :
    for a in range (1, 1001):
        if is_3 (a):
            if is_connecting(a):
                print(f"&{a}") 
            else :
                print(a)
                
if m == 3 :
    for a in range (1, 1001):
        if is_3 (a):
            if is_connecting(a):
                if is_prime(a):
                    print(f"&{a}*")
                else :
                    print(f"&{a}")
            elif is_prime(a):
                print (f"{a}*")
            else :
                print(a)
               
            
        
   
    
        

    
    
