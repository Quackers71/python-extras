#3 map function

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

#2 print(list(map(func, li))) # using the map function this outputs the same as below

#3 print([func(x) for x in li]) # using list comprehension

print([func(x) for x in li if x %2==0]) #4 using list comprehension and only if x is divisible by 2

''' 
#1 The original way to create a new list using the Function
newList = []
for x in li:
    newList.append(func(x))

print(newList)

Output 1: 
[1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]

Output 2: 
[1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]

Output 3: 
[1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]

Output 4: 
[4, 256, 46656, 16777216, 10000000000]
'''