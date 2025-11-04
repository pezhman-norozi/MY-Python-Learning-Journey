def chandta_harf(s , c):
    '''
    shomaresh horoff
    '''
    counter = 0
    for this_characters in s:
        if this_characters == c:
            counter += 1
    return(counter)

name = input()
show = chandta_harf(name , "a")
print(f'{name} has {show}  a')