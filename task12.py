import re
from collections import Counter

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase for case-insensitive counting
            
            # Use regex to find all words (sequence of alphanumeric characters)
            words = re.findall(r'\b\w+\b', text)
            
            # Count occurrences of each word
            word_counts = Counter(words)
            
            # Sort the dictionary by key (word) alphabetically
            sorted_word_counts = dict(sorted(word_counts.items()))
            
            # Display the results
            for word, count in sorted_word_counts.items():
                print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = input("Enter the path to the text file: ")
count_words_in_file(file_path)
