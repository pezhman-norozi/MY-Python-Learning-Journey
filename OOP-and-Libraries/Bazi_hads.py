import random

def welcome():
    print("Welcome to your funny Game")
    print("Guess your number")
    print("Do you think will win")
    print("Starttttttt")
    print()

def finish(number , count):
    print("Good Game")
    print(f"my number was {number} and you found it in {count} va {record} record ine ")
    print()
    answer = input ("Do you play a again (Y/N)")
    if answer.upper() in ["Y" , "ARE" , "BALE"] :
        return True
    else:
        return False
    
    

def win(computer_number , guess):
    return computer_number == guess

def answer(computer , user):
    if computer > user :
        return "My Number is larger"
    if computer < user :
        return "My number is smaller"
    
    return "wowww your so good in guess number"

def get_guess():
    ans = int (input ("Guess your number: "))
    return ans


record = None
welcome()
continueplaying = True
while (continueplaying) :
    computer_number = random.randint(1 , 20)
    guess = 0
    count = 0
    

    while (not win (computer_number , guess)):
        guess = get_guess()
        count += 1
        print(answer(computer_number , guess))
    if record is None or count<record :
        record = count 
           
    continueplaying = finish(computer_number , count)


