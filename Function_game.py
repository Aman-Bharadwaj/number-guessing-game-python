import random

def choose_difficulty():
    print("Choose difficulty: ")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")

    difficulty = int(input("Enter Choice: "))

    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 7
    elif difficulty == 3:
        return 5
    else:
        print("You Idiot, Play on Easy mode")
        return 10

def generate_number():
    return random.randint(1,500)

def play_game():
    number = generate_number()
    attempts = choose_difficulty()
    attempt = 0 

    while attempt < attempts:
        guess = int(input("Enter your guess: "))
        attempt += 1

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("You got it in", attempt, "attempts" )
            return
        
    print("Game over! The number was", number)

while True: 

    play_game()

    again = input("Play again? (y/n): ")

    if again != "y":
        break