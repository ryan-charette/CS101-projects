#You are a student and you are trying to organize your subjects and grades using Python. 
#Let’s explore what we’ve learned about lists to organize your subjects and scores.
#Use lists and 2D-lists, .append(), .remove(), list addition, and be able to modify list items

import ast

gradebook = []

subject_input = input("Enter the name of each class you are taking separated by commas: ")
subjects = subject_input.split(",")
grades_input = input("Enter your current grades separated by commas: ")
grades = grades_input.split(",")

for item in range(len(subjects)):
    gradebook.append([subjects[item], grades[item]])

while True:
    selection = input("""Update gradebook using the following options:
    [1] Change grade
    [2] Add new subject
    [3] Change to Pass/Fail
    [4] Export gradebook
    [5] Append previously exported gradebook
    [6] Exit
    """)

    if selection == "1":
        subject_to_update = input("Which subject's grade would you like to update? ")
        for subject in range(len(gradebook)):
            if gradebook[subject][0] == subject_to_update or gradebook[subject][0] == " " + subject_to_update:
                new_grade = input("Enter updated grade: ")
                gradebook[subject][1] = new_grade
            elif subject == len(gradebook):
                print("Subject not found.")
    elif selection == "2":
        new_subject = input("Enter new subject: ")
        new_subject_grade = input("Enter new subject grade: ")
        gradebook.append([new_subject, new_subject_grade])
    elif selection == "3":
        pf_class = input("Which subject would you like to change to pass/fail? ")
        for subject in range(len(gradebook)):
            if gradebook[subject][0] == pf_class or gradebook[subject][0] == " " + pf_class:
                pf = input('Enter "Pass" or "Fail": ')
                gradebook[subject][1] = pf
            elif subject == len(gradebook):
                print("Subject not found.")
    elif selection == "4":
        print(gradebook)
    elif selection == "5": 
        old_gradebook = ast.literal_eval(input("Enter previously exported gradebook: "))
        gradebook = old_gradebook + gradebook
    elif selection == "6":
        break
    else:
        print("Invalid selection.")
    
