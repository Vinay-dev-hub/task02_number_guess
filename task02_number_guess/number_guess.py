import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("📉 Too low. Try again.")
        elif guess > secret_number:
            print("📈 Too high. Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} correctly.")
            break
    except ValueError:
        print("❌ Please enter a valid number.")
attempts = 0
...
attempts += 1
...
print(f"You guessed it in {attempts} tries!")
88