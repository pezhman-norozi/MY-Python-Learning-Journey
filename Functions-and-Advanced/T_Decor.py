import time

def Zaman(func):
    def wrapper(*args , **kwargs):
        start = time.perf_counter()
        result = func(*args , **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@Zaman
def listak(n):
    return list(range(1 , n+1))
       
        
n = int ( input ("Enter your Number:" ))
Numbers = listak(n)
print(Numbers)
           
    
