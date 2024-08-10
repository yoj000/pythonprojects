import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")
    
    # Getting the range from the user
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Ensure that the lower bound is less than the upper bound
    if lower_bound >= upper_bound:
        print("Invalid range. The lower bound should be less than the upper bound.")
        return
    
    # Generate the random number within the specified range
    number_to_guess = random.randint(lower_bound, upper_bound)
    guessed = False
    
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess it?")
    
    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            
            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Your guess must be between {lower_bound} and {upper_bound}. Try again.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number: {number_to_guess}")
                guessed = True
        except ValueError:
            print("That's not a valid number. Please enter a valid integer.")

if __name__ == "__main__":
    number_guesser()

