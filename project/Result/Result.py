class Student:
    def __init__(self):
        # Attribute
        self.name = input("Enter the student name: ")
        self.roll_num = int(input("Enter the roll number: "))
        self.marks1 = int(input("Enter marks1: "))
        self.marks2 = int(input("Enter marks2: "))
        self.marks3 = int(input("Enter marks3: "))

#method
class Child(Student):
    def calculate_total_marks(self):
        return self.marks1 + self.marks2 + self.marks3

    def calculate_per(self):
        total = self.calculate_total_marks()
        return (total / 300) * 100

# Create object
result = Child()

# Total marks
total_marks = result.calculate_total_marks()
print(f"The total marks is: {total_marks}")

# Percentage
per_obtain = result.calculate_per()
print(f"The total percentage is: {per_obtain:.2f}%")

# Pass / Fail
if per_obtain >= 80:
    print("Result: Distinction")
elif per_obtain >= 60:
    print("Result: First Division")
elif per_obtain >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
