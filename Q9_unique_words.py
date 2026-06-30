# Program : Unique Words Finder
# Concepts: Strings, Sets, Modules, Exception Handling
import math

def unique_words():

    try:
        # Take sentence input
        sentence = input("Enter a sentence: ")

        # Check if sentence is empty
        if sentence.strip() == "":
            raise ValueError("Sentence cannot be empty.")

        # Convert sentence into words
        words = sentence.split()

        # Store unique words in a set
        unique_set = set(words)

        # Sort unique words
        sorted_words = sorted(unique_set)

        # Display unique words
        print("\n" + "=" * 50)
        print("📝 Unique Words")
        print("=" * 50)

        for word in sorted_words:
            print(word)

        # Calculate square of total unique words
        total = len(unique_set)
        result = math.pow(total, 2)

        print("\n" + "=" * 50)
        print(f"Total Unique Words : {total}")
        print(f"Square of Total    : {int(result)}")
        print("=" * 50)

    except ValueError as e:
        print("❌", e)

    except Exception as e:
        print("❌ Error:", e)

# Function Call
unique_words()