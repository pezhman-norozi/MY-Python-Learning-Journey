names = [ "pezhman" , "ali" , "mobina"]
data = {
    "ali" : { "sen" : 15 , "ghad" : 189}
    ,
    "mobina" : {"sen" : 24 , "ghad" : 175}
    
}

for name in names :
    if name in data:
        print(f"i have {name} and sen {data[name]["sen"]} and my hieght is {data[name]["ghad"]} cm")
    else :
        print(f"i have no data for {name}")