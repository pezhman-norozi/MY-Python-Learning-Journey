donations = {
    "mobina" : 18 ,
    "ayoub" : 200 ,
    "pedram" : 900 ,
    "amir" : 1800  
}

def donation_Analisis (don):
    person = ""
    total = 0
    count = 0
    max_don = -1
    for name , value in don.items():
        total += value
        count += 1
        if value > max_don:
            person = name
            max_don = value
    
    avarage = int(total / count)
    return avarage , total , person
avg , total , max_person = donation_Analisis(donations)

print(total)
print(avg)
print(max_person)
        

