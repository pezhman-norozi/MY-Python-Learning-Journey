def pick_evens(*args) :
    evens =[ ]
    for a in args :
        if  a % 2 == 0 :
            evens.append(a)
    return evens       

nums = list(map(int , input().split() ))
print(pick_evens(*nums))
print(nums)