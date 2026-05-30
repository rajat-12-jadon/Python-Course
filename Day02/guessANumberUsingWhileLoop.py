import random

num = random.randint(1, 10)
# print(num)

tries = 0

while True:

    guess = int(input("Please guess you number: "))

    if num == guess:
        tries += 1
        print(f"You are right and you guessed the number in {tries} tries.")
        break
    elif num < guess:
        print("Choose smaller number.")
        tries += 1
    elif num > guess:
        print("Choose larger number.")
        tries += 1
    else:
        tries += 1
        print("Sorry! You are wrong")

# for n chances

tries = 5

while tries > 0:

    guess = int(input("Please guess your number: "))

    if num == guess:
        print("You guessed correctly!")
        break

    elif num < guess:
        print("Choose a smaller number.")

    else:
        print("Choose a larger number.")

    tries -= 1
    print(f"Remaining tries: {tries}")

if tries == 0:
    print(f"You failed! The number was {num}.")