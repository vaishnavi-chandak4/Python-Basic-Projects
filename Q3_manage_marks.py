# Program : Student Marks Management System
# Concepts: Lists, Functions, Exception Handling

def manage_marks():
    marks = []  # List to store marks

    print("=" * 50)
    print("📚 Student Marks Management System")
    print("=" * 50)

    # Take marks for 5 subjects
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i}: "))

                # Validate marks
                if mark < 0 or mark > 100:
                    print("❌ Marks should be between 0 and 100.")
                    continue

                marks.append(mark)
                break

            except ValueError:
                print("❌ Invalid input! Please enter numeric marks.")

    # Calculate result
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Sort marks in descending order
    sorted_marks = sorted(marks, reverse=True)

    # Display Result
    print("\n" + "=" * 50)
    print("📊 Student Result")
    print("=" * 50)
    print(f"📝 Marks Entered      : {marks}")
    print(f"🏆 Highest Marks      : {highest}")
    print(f"📉 Lowest Marks       : {lowest}")
    print(f"📈 Average Marks      : {average:.2f}")
    print(f"🔽 Descending Order   : {sorted_marks}")
    print("=" * 50)


# Function Call
manage_marks()