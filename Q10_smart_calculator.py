# Project : Smart Calculator & Data Manager
# Concepts: Functions, Dictionary, Exception Handling,
#           Math Module, Random Module, While Loop
import math
import random
from datetime import datetime

# Dictionary to store history
history = {}

# ---------------- Basic Arithmetic ----------------
def arithmetic():

    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose Operation : ")

        if choice == "1":
            result = num1 + num2
            operation = f"{num1} + {num2}"

        elif choice == "2":
            result = num1 - num2
            operation = f"{num1} - {num2}"

        elif choice == "3":
            result = num1 * num2
            operation = f"{num1} * {num2}"

        elif choice == "4":
            if num2 == 0:
                print("❌ Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = f"{num1} / {num2}"

        else:
            print("❌ Invalid Choice")
            return

        print("✅ Result :", result)

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        history[timestamp] = f"{operation} = {result}"

    except ValueError:
        print("❌ Please enter valid numbers.")

# ---------------- Scientific Calculator ----------------
def scientific():

    try:
        num = float(input("Enter Number : "))

        print("\n1. Square Root")
        print("2. Power")
        print("3. Factorial")

        choice = input("Choose Operation : ")

        if choice == "1":

            if num < 0:
                print("❌ Square root of negative number is not possible.")
                return

            result = math.sqrt(num)
            operation = f"√{num}"

        elif choice == "2":

            power = float(input("Enter Power : "))
            result = math.pow(num, power)
            operation = f"{num}^{power}"

        elif choice == "3":

            if num < 0 or num != int(num):
                print("❌ Factorial requires a positive integer.")
                return

            result = math.factorial(int(num))
            operation = f"{int(num)}!"

        else:
            print("❌ Invalid Choice")
            return

        print("✅ Result :", result)

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        history[timestamp] = f"{operation} = {result}"

    except ValueError:
        print("❌ Invalid Input")

# ---------------- Random Number ----------------
def random_numbers():

    try:
        start = int(input("Enter Start Number : "))
        end = int(input("Enter End Number : "))

        result = random.randint(start, end)

        print("🎲 Random Number :", result)

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        history[timestamp] = f"Random Number = {result}"

    except ValueError:
        print("❌ Please enter valid integers.")

# ---------------- View History ----------------
def view_history():

    if len(history) == 0:
        print("📂 No History Available.")

    else:
        print("\n========== History ==========")

        for time, data in history.items():
            print(time, "->", data)

# ---------------- Main Menu ----------------

while True:

    print("\n" + "=" * 50)
    print("🧮 Smart Calculator & Data Manager")
    print("=" * 50)

    print("1. Basic Arithmetic")
    print("2. Scientific Calculator")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        arithmetic()

    elif choice == "2":
        scientific()

    elif choice == "3":
        random_numbers()

    elif choice == "4":
        view_history()

    elif choice == "5":
        print("\n✅ Thank You! Program Closed.")
        break

    else:
        print("❌ Invalid Choice! Try Again.")