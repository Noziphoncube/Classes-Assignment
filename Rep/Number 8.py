import random

# Function to generate a list of random integers
def generate_random_numbers(n, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Main program
def main():
    # Generate 10 random integers between 1 and 100
    random_numbers = generate_random_numbers(10, 1, 100)
    
    # Calculate the average
    average = calculate_average(random_numbers)
    
    # Print the results
    print("Generated random numbers:", random_numbers)
    print("Average of the numbers:", average)

# Run the main function
if __name__ == "__main__":
    main()
