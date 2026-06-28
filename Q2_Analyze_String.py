# Function to analyze a string
def analyze_string(s):

    # Handle empty string case
    if len(s) == 0:
        print("String is empty!")
        return

    # Print length
    print("Length of String:", len(s))

    # Print reverse string
    print("Reversed String:", s[::-1])

    # Count vowels (case insensitive)
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Number of Vowels:", count)

    # Print each character with positive and negative index
    print("\nCharacter Indexes:")
    for i in range(len(s)):
        print(f"Positive Index: {i} | Negative Index: {i-len(s)} | Character: {s[i]}")


# User input
text = input("Enter a String: ")

# Function call
analyze_string(text)