# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:23:54 2020

@author: rrajkumar1990
"""



# Lets  continue on our sorting , we will go to the next  sorting algorithm

#insertion sort


#step1: lets consider a list of elements 7,4,3,5
#step2 : take the first element , keep it aside in this case its 7
#step 3: take the next element from the list which is 4 , and insert it before 7
#step4 : continue with the next element and insert it accordingly untilall the elements are traversed




def ins_Sort(n):
    l= len(n)
    
    for i in range(1,l):
        val = n[i]
       
        idx = i
       
        while idx > 0 and val < n[idx -1]:     # check  if the present val is less the the previous element in the sequence
            
            n[idx] = n[idx-1]      # as its less assign previous to present
            
            idx -= 1   
        
        n[idx] = val     #
        
    return n



ins_Sort([5,4,3,2])


#2,3,4,5
