# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:21:15 2020

@author: rrajkumar1990
"""

#Recursion

#lets start a basic factorial


import datetime

def factorial(n):
    if n <= 1 :
        return 1
    else :
        return n*factorial(n-1)


print(factorial(3))

#answer is 6 

#pretty simple huh. lets see for a higher number along with time  for n =1000

#lets see how much 
start = datetime.datetime.now()
factorial(1000)
end = datetime.datetime.now()
print(end-start)
 
#0:00:00.000996

#the problem is not only the time but lets increase the number to 2000 and 3000
factorial(2000)
factorial(3000)

#RecursionError: maximum recursion depth exceeded in comparison


#ideally this is the reality guys, there is a maximum limit to that and we should be fast. what shall we do


#Simple ways to solve both the problems =Caching 

cache={}

def factorial_new(n):
    if n < 2 :
        return 1
    else :
        if n in cache :  #adding a small check to our cache
            return cache[n]
        else:
            val = n*factorial_new(n-1)  # if not in cache repeat but add in the cache once done
            cache[n] = val
            return val


#lets see how our cache workis for n =1000 first
start = datetime.datetime.now()
factorial_new(1000)
end = datetime.datetime.now()
print(end-start)
 
#0:00:00.000951  why is this still lets run again now
start = datetime.datetime.now()
factorial_new(1000)
end = datetime.datetime.now()
print(end-start)

#0:00:00 - not a miracle just a simple cache :)

#final thing lets see the recursion limit with our new cache implementation

start = datetime.datetime.now()
factorial_new(2000)
factorial_new(3000)
end = datetime.datetime.now()
print(end-start)



### we very well get result and a faster result

## you guys could think why we are timing functions with date time , in our further process, i'll explain a better and efficient pythonic way for timing the functions



