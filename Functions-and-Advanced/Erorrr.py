def divide(a, b):
    try :
        result = a / b
        return result
    except ZeroDivisionError :
        print("b had a Zeroooo!")
        return None
 
            
while True:            
    try :
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = divide(num1, num2)
        if result is not None:
            print("Result:" , result )
            break
        break
    except ValueError :
        print("Error: Please enter numeric values only.")
    finally :
        print("program has succsesfull")          
            