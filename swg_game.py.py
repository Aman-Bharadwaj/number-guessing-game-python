import random

names =  ["snake", "water", "gun"]

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:

    user = input("Enter 0=(snake) 1=(water) 2=(gun) or q=quit: ")

    if user == "q":
        print("You left the game")
        break
 
    if user not in ["0", "1", "2"]:
        print("Invalid input")
        continue

    user = int(user)
    computer = random.randint(0,2)

    print("You chose:", names[user])
    print("Computer chose:", names[computer])

    result = (user - computer) % 3

    if result == 0:
        print("Draw")

    elif result == 1:
        print("computer wins")
        computer_score += 1

    else:
        print("You win")
        user_score += 1

    print("Score → You:", user_score, "| computer:", computer_score)
    
print("\nFinal Score")
print("You:", user_score)
print("computer:", computer_score)

if user_score > computer_score:
   print("You won the match!")