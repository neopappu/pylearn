#!/usr/bin/env python3


def h_many_add(*args_pappu: int) -> int:
    return sum(args_pappu)

def mult_3(a: int, b: int, c: int) -> int :
    return a * b * c

h_many_add(1,2,3,4,5,4)
h_many_add(12)
"""  

an_array = list(range(4))

print(an_array)

print(an_array)

str_item = [str(x) for x in an_array]
    
names = ["tom", "dick", "harry"]

print(names)
print("###".join(names))

"""

nums = [1,1,1,2,2,5,5,5,5,5,5]
outdict = {}
for item in nums:
    print(outdict)
    try:
        outdict[item] += 1
        print("repeat time")
    except:
        outdict[item] = 1
        print("first time")
print(outdict)

