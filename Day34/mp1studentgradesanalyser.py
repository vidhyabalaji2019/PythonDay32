# Mini Project 1: Student Grades Analyzer

# Dictionary storing student names and marks
students = {
    "Anu": 85,
    "Kamal": 92,
    "Madhu": 78,
    "Oviya": -1,  # Absent
    "Sundar": 90,
    "Johny": 65
}

total_marks = 0
count = 0

print("Student Rankings:")
rank = 1

# Loop through students and display marks
for name, marks in students.items():
    if marks == -1:
        continue  # Skip absent students
    total_marks += marks
    count += 1
    print(f"{rank}. {name} - {marks} marks")
    rank += 1

# Calculate class average
avg_marks = total_marks / count if count > 0 else 0
print(f"\nClass Average Marks: {avg_marks:.1f}")

# Identify top performers
print("\nTop Performers:")
for name, marks in students.items():
    if marks >= 80:
        print(f"🏆 {name} - {marks} marks")
