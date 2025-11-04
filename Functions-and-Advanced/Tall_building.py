def skyline(*args) :
    a = 0
    for i in args :
        if i > a :
            a = i
    return a
nums = list(map(int , input().split() ))
print(skyline(*nums))
print(nums)