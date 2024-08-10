def fibonacci_sequence(n):
    # Initialize the first two terms of the Fibonacci sequence
    sequence = [0, 1]

    # Generate the sequence up to n terms
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    # If n is 1, return only the first term
    if n == 1:
        return [sequence[0]]
    
    return sequence

# Example usage:
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_seq = fibonacci_sequence(num_terms)
        print(f"The first {num_terms} terms of the Fibonacci sequence are: {fibonacci_seq}")
except ValueError:
    print("Please enter a valid integer.")
