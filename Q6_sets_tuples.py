# Program : Set, Tuple and Module Operations
# Concepts: Sets, Tuples, Random Module, Math Module,
#           Exception Handling

import random
import math


def set_tuple_operations():

    numbers = set()  # Set to store unique numbers

    print("=" * 50)
    print("🔢 Set and Tuple Operations")
    print("=" * 50)

    # Take 10 numbers from the user
    while len(numbers) < 10:
        try:
            num = int(input(f"Enter Number {len(numbers)+1}: "))
            numbers.add(num)

        except ValueError:
            print("❌ Please enter a valid integer.")

    # Convert set into tuple
    number_tuple = tuple(numbers)

    print("\nUnique Numbers (Set) :", numbers)
    print("Tuple :", number_tuple)

    try:
        # Pick 3 random unique numbers
        random_numbers = random.sample(number_tuple, 3)
        print("\n🎲 Random Numbers :", random_numbers)

        # Calculate square root of sum
        total = sum(number_tuple)

        if total < 0:
            print("❌ Square root cannot be calculated for a negative sum.")
        else:
            print("√ Sum of Tuple :", round(math.sqrt(total), 2))

    except ValueError as e:
        print("❌", e)


# Function Call
set_tuple_operations()