print("=== NUMBER GUESSING GAME ===")

secret = 7

guess = int(input("Guess a number from 1 to 10: "))

if guess == secret:
    print("Congratulations! Correct guess!")
elif guess < secret:
    print("Too low! Try again next time.")
else:
    print("Too high! Try again next time.")