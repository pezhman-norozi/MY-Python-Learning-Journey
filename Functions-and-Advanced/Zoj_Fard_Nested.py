numbers = []

for i in range(5):
    num = int ( input( ))
    numbers.append(num)
print(numbers)

def shomarsh (numbers):
    def even_p (n):
       return n % 2 == 0
    
    even = []
    odd = []
    
    for n in numbers:
        if even_p(n):
            even.append(n)
        else:
            odd.append(n)
    
    return even, odd, len(even), len(odd)

even, odd, even_count, odd_count = shomarsh(numbers)
print("اعداد زوج:", even, "تعداد:", even_count)
print("اعداد فرد:", odd, "تعداد:", odd_count)
