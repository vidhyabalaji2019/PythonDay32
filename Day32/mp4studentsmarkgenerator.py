# Mini Project 1: Simple Student Report Card
# AI POWERED PYTHON DJANGO MYSQL LEARNING MATERIAL

# Taking student details as input
student_name = input("Enter student name: ")
student_class = input("Enter class: ")

# Taking marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculating total and percentage
total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

# Displaying data types (for learning purpose)
print(f"\nType of student_name: {type(student_name)}")
print(f"Type of student_class: {type(student_class)}")
print(f"Type of subject1: {type(subject1)}")
print(f"Type of total_marks: {type(total_marks)}")
print(f"Type of percentage: {type(percentage)}")

# Displaying formatted report card
print("\n========== STUDENT REPORT CARD ==========")
print(f"Student Name : {student_name}")
print(f"Class        : {student_class}")
print("------------------------------------------")
print(f"Subject 1    : {subject1}")
print(f"Subject 2    : {subject2}")
print(f"Subject 3    : {subject3}")
print("------------------------------------------")
print(f"Total Marks  : {total_marks}")
print(f"Percentage   : {percentage:.2f}%")
print("==========================================")

# Grade display (optional enhancement)
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 45:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade        : {grade}")
print("==========================================")
print("Thank you for using the Student Report System!")
