def calculate_percentage(marks):
    total_marks = sum(marks)
    total_subjects = len(marks)
    return total_marks / total_subjects

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 35:
        return "E"  # Pass grade
    else:
        return "F"  # Fail grade

def main():
    subjects = ["Physics", "Chemistry", "Maths", "Computer", "English", "Nepali"]
    
    name = input("Enter student's name: ")
    
    marks = []
    print("\nEnter marks for each subject (0-100):")
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a number between 0 and 100")
            except ValueError:
                print("Please enter a valid number!")
    
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    gpa = percentage / 25
    
    print("\nResults:")
    print(f"Name: {name}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"GPA: {gpa:.2f}")
    print("Status: " + ("Pass" if percentage >= 35 else "Fail"))

if __name__ == "__main__":
    main()
