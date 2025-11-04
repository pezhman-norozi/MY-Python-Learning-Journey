def is_it_zoj(f):
    def wrapper():
        
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 != 0:
            f()
        else:
            print("hisssss")
    return wrapper


@is_it_zoj
def say_heloo():
    print("salaaammmm")

@is_it_zoj    
def say_bye():
    print("byeeeeee")
    
    
#is_it_zoj(say_heloo)
#is_it_zoj(say_bye)

say_heloo()
say_bye()


    