# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 23:34:25 2020

@author: rajkumar.rajasekaran
"""

## hope you guys have seen my Bubble sort  way

# As i had mentioned bubble sort is the harder way ,  there are other ways of sorting 

#the other common way of sorting is the selection sort

#how does it work?

#same way as how we all humans think. lol !! 

#lets take a list , 8,6,3,4

#step1: we find the smallest in the list 3, we keep it aside
#step2 : scan through the remainin list 8,6,4 and find smallest which is 4 and add to our list  so now its 3,4
#step3 : continue the same process and sort the full list



def selectionSort(n):
    l= len(n)
    
    for  i in range(l-1):  
        index= i   # fix a index value initially
        
        for j in range(i+1,l):
            
            if n[j] < n[index]:  # check if the intial index value is smaller than other
                
                index = j    
            
        if index != i :     # if the initila index is not smaller , as it will be changed.now update the postion
            temp = n[i]
            
            n[i] = n[index]
            
            n[index] = temp
            
    return n 
            
            
   
    
selectionSort([6,7,8,3,4,6,8,0,5,2])