# A simple grade checker program in Python that calculates the percentage, grade, and GPA based on marks entered by the user.

#Function to calculate the percentage from marks
def calculate_percentage(marks):
    total_marks = sum(marks)
    total_subjects = len(marks)
    return total_marks / total_subjects

# Function to calculate the grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C+"
    elif percentage >= 40:
        return "C"
        
    elif percentage >= 35:
        return "D"  # Pass grade
    else:
        return "F"  # Fail grade

# Main function to run the grade checker program
def main():
    subjects = ["Physics", "Chemistry", "Maths", "Computer", "English", "Nepali"]
    
    name = input("Enter your name: ")
    
    marks = []
    print("\nEnter marks for each subject (0-100):")
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter your marks in {subject}: "))
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
    

    # Displaying the results
    print("\n" + "="*30)
    print("\nResults:")
    print("-"* 30)
    print(f"Student's Name: {name}")
    print(f"Percentage Obtained: {percentage:.2f}%")
    print(f"Grade Obtained: {grade}")
    print(f"GPA Obtained: {gpa:.2f}")
    print("Status: " + ("Pass" if percentage >= 35 else "Fail"))
    print("\n" + "="*30)
main()
