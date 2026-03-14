name = ["snake", "water", "gun"]

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:

    user = get_user_choice()
    
def get_user_choice():
    get
    user = input("Enter 0=snake, 1=water, 2=gun, q=quit: ")

    if user == "q":
        return "q"
    
    if user not in ["0", "1", "2"]:
        print("Invalid input")
        return None
    
    return int(user)

def get_computer_choice():
    import random
    return random.randint(0,2)

def decide_winner(user, computer):
    result = (user-computer) % 3

    if result == 0:
        return "draw"

    elif result == 1:
        return "computer"
    
    else:
        return "user"
    
def print_score(user_score, computer_score):
    print("score → You:", user_score,"| computer:", computer_score)    