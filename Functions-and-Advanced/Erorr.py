def divide():
    while True:    
    
        try :
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = a / b
            print("Result:" , result)
            break
        except ZeroDivisionError :
            print(f"had erorr 0")
            
        except ValueError :
            print("Error: Please enter numeric values only.")
            
        finally :
            print("program is succsesfull")
    
     
    
divide()

