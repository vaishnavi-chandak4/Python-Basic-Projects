# Program : Square Numbers using Lambda Function
# Concepts: Lambda, Range, Lists, Exception Handling

def square_numbers():

    try:
        # Lambda function to calculate square
        square = lambda x: x ** 2

        # Generate numbers from 1 to 20
        numbers = range(1, 21)

        # Store squares in a list
        square_list = list(map(square, numbers))

        # Display all squares
        print("=" * 50)
        print("📌 Squares of Numbers (1 to 20)")
        print("=" * 50)
        print(square_list)

        # Print only even squares
        even_squares = list(filter(lambda x: x % 2 == 0, square_list))

        print("\n📌 Even Squares")
        print("=" * 50)
        print(even_squares)

    except Exception as e:
        print("❌ Error:", e)


# Function Call
square_numbers()