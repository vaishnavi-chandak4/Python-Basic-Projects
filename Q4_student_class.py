# Program : Student Management System
# Concepts: OOP, Lists, Exception Handling

class Student:

    # Constructor to initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Method to add marks
    def add_mark(self, mark):
        try:
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")

            self.marks_list.append(mark)

        except ValueError as e:
            print("❌", e)

    # Method to calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Method to display student details
    def display_info(self):
        print("\n" + "=" * 50)
        print("🎓 Student Information")
        print("=" * 50)
        print(f"Name          : {self.name}")
        print(f"Roll Number   : {self.roll_no}")
        print(f"Marks         : {self.marks_list}")
        print(f"Average Marks : {self.get_average():.2f}")
        print("=" * 50)


# Main Program 
try:
    name = input("Enter Student Name : ")
    roll = int(input("Enter Roll Number  : "))
    student = Student(name, roll)

    print("\nEnter marks for 5 subjects")

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Subject {i} Marks : "))

                student.add_mark(mark)

                if 0 <= mark <= 100:
                    break

            except ValueError:
                print("❌ Please enter numeric marks.")
    student.display_info()

except ValueError:
    print("❌ Roll Number must be numeric.")