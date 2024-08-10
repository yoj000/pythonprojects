import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guessed = False
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            user_guess = int(input("Please enter your guess: "))
            
            if user_guess < 1 or user_guess > 100:
                print("Your guess must be between 1 and 100. Try again.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number: {number_to_guess}")
                guessed = True
        except ValueError:
            print("That's not a valid number. Please enter a number between 1 and 100.")

if __name__ == "__main__":
    guessing_game()
