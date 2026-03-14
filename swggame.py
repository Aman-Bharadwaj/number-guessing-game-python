import random
choices = ["s", "w", "g"]

user_score = 0
computer_score = 0

for i in range(5):

    computer = random.choice(choices)

    user = input("Enter s, w or g: ").lower()
    if user == "q":
        print("You left the game")
        break

    if user == computer:
        print("Draw")

    elif (user == "s" and computer == "w") or \
        (user == "w" and computer == "g") or \
        (user == "g" and computer == "s"):
        print("You win")
        user_score += 1

    elif user in choices:
        print("Computer wins")


    else:
        print("Invalid Input")

print("Final Score")
print("You", user_score)
print("Computer:", computer_score)

