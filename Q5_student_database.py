# Program : Student Database Management System
# Concepts: Dictionary, Functions, While Loop, Exception Handling
def student_database():

    students = {}  # Dictionary to store student records

    while True:

        print("\n" + "=" * 50)
        print("📚 Student Database Management")
        print("=" * 50)
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ")

        #  Add Student 
        if choice == "1":
            try:
                roll = int(input("Enter Roll Number : "))
                name = input("Enter Name        : ")
                age = int(input("Enter Age         : "))
                city = input("Enter City        : ")

                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("✅ Student added successfully.")

            except ValueError:
                print("❌ Invalid input! Roll Number and Age must be numeric.")

        #  Search Student 
        elif choice == "2":
            try:
                roll = int(input("Enter Roll Number to Search: "))

                student = students.get(roll)

                if student:
                    print("\nStudent Found")
                    print("-" * 30)
                    print("Roll Number :", roll)
                    print("Name        :", student["Name"])
                    print("Age         :", student["Age"])
                    print("City        :", student["City"])
                else:
                    print("❌ Student not found.")

            except ValueError:
                print("❌ Please enter a valid Roll Number.")

        #Display All Students
        elif choice == "3":

            if len(students) == 0:
                print("⚠️ No student records available.")

            else:
                print("\n========== Student Records ==========")

                for roll, details in students.items():
                    print(f"\nRoll Number : {roll}")
                    print(f"Name        : {details['Name']}")
                    print(f"Age         : {details['Age']}")
                    print(f"City        : {details['City']}")
                    print("-" * 35)

        #  Exit
        elif choice == "4":
            print("✅ Thank you! Program Closed.")
            break

        #  Invalid Choice 
        else:
            print("❌ Invalid choice! Please select between 1 and 4.")


# Function Call
student_database()