n = 0

while n < 20 :
 
        n += 1
        if n % 3 == 0 and n % 5 == 0 :
            print("hihoop")
            continue
        if n % 3 == 0 :
            print("hop")
            continue
        if n % 5 == 0 :
            print("hoop")
            continue
        if n == 17 :
            break    
        print(n)
       
       
#new = ["hop" if n%3 == 0 else n for n in range(1 , 16) ]
#print(new)
#هوپ به روش لیست کامپریهنشن