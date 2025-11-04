count = 0
count_1 = 0
my_list = [1 ,2 ,7 ,9 ,123 ,234 ,565 ,568 ,987 , 8765]

even_numbers =[]
odd_numbers =[]

for a in my_list:
    if a % 2 == 0:
        count += 1
        even_numbers.append(a)
    else:
        count_1 += 1
        odd_numbers.append(a)
        
print("even_numbers:")   
for num in even_numbers:
    print(num)   
print("odd_numbers:")
for num in odd_numbers:
    print(num)  
    
print(f"we had {count} even numbers")
print(f"we had {count_1} odd numbers")

