import random

while True:   # game loop

    number = random.randint(1, 500)
    attempt = 0

    print("Choose difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty = int(input("Enter Choice: "))

    if difficulty == 1:
        attempts = 10
    elif difficulty == 2:
        attempts = 7
    elif difficulty == 3:
        attempts = 5
    else:
        print("Invalid choice")
        continue

    guess = int(input("Enter your guess: "))

    while guess != number and attempt < attempts:

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")

        attempt += 1

        if attempt == attempts:
            break

        guess = int(input("Enter your guess: "))

    if guess == number:
        print("You got it in", attempt + 1, "attempts")
    else:
        print("Game over! The number was", number)

    play = input("Play again? (y/n): ").lower()

    if play == "n":
        print("Thanks for playing")
        break