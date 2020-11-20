# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:47:22 2020

@author: rrajkumar1990
"""



# sorting 

# often we get big lists or and we get questions what the port of sorting something

#sorting is a way of arranging things ascending or decending

#very useful for searching and finding anything when we have lists sorted


#lets start with a  basic Bubble sort:


###what is bubble sort?
#simplest and easiet sort is the bubble sort

#how do we do:
#for eg: lets consider number  5,4,7,2

#step 1: start  with first two elements , compare which is small move to left - 5 and 4 => now sorted array becomes 4,5
#step2: move one postion now and compare postion two and three => 5,7 => its already sorted  so lets conitue 
#step 3: move subsequently and come bac iteratively until everything is sorted

def bubbleSort(n):
    l = len(n)

    for i in range(l-1):  #here l-1 because we are comparing next elemnet 
        
        for j in range(l-i-1): #each element traverses one whole time
            
            if n[j] > n[j+1] :
            
                val    =  n[j+1]
            
                n[j+1] =  n[j]
            
                n[j]   =  val
                
    return n


# here  each element of outer loop will go will run for all but one element in inner loop
    
# for value of i =0 , j takes values =0,1,2,3
# for i =1 , j takes 0,1,2 , for i=2 , j is 0,1...


bubbleSort([5,4,6,8,2])


#[2, 4, 5, 6, 8]
    