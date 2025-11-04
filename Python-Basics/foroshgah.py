
shopping = int(input())

if shopping > 50000 :
    discount = shopping * .2
    final_price = shopping - discount
    print(int(final_price))
elif 20000 < shopping < 500000 :
    discount = shopping * .1
    final_price = shopping - discount
    print(int(final_price))
elif shopping < 20000 :
    print(int(shopping))

