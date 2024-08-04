import re

def is_valid_email(email):
    # Regular expression for validating an email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the regex pattern
    if re.match(regex, email):
        return True
    else:
        return False

# Example usage
emails = ["test@example.com", "invalid-email@", "test@.com", "valid.email@domain.com"]

for email in emails:
    if is_valid_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is not a valid email address.")