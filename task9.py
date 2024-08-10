import re

def password_strength_checker(password):
    # Initial strength score
    strength_score = 0
    
    # Check for minimum length of 8 characters
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password should be at least 8 characters long.")
    
    # Check for presence of lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one lowercase letter.")
    
    # Check for presence of uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one uppercase letter.")
    
    # Check for presence of digits
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        print("Password should contain at least one digit.")
    
    # Check for presence of special characters
    if re.search(r'[\W_]', password):  # \W matches any non-word character, including special characters
        strength_score += 1
    else:
        print("Password should contain at least one special character.")
    
    # Determine the overall strength
    if strength_score == 5:
        return "Strong Password"
    elif 3 <= strength_score < 5:
        return "Moderate Password"
    else:
        return "Weak Password"

# Example usage:
password = input("Enter your password: ")
strength = password_strength_checker(password)
print(f"Password strength: {strength}")
