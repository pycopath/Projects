# Jonathan Morales
# Comp163 -007
# 9/40/2023
# This program will tell take the user's input of 3 of each category's grade in the grade book and average them out based on their weight. 
# It will then print a final grade based on the averages of each assignment in each category.


# Create the dictionary that holds the type of assignment and corresponding weight
comp163Cat = {
    "Homework": 0.1,
    "Program Assignments": 0.3,
    "Quiz": 0.15,
    "Test": 0.2,
    "Final Exam": 0.25
}

# Create the dictionary of averaged category grades to later update with real values
comp163CatGrades = {
    "Homework": 0,
    "Program Assignments": 0,
    "Quiz": 0,
    "Test": 0,
    "Final Exam": 0
}

catGrade = []

#Prompt the user to enter 3 grades for each category, 
# then append them to the catgrade list to average them out and set correct value for comp163catgrades.
#  Then clear list and repeat process for all categories
for type in comp163Cat:
    numgrade = 0
    print(f"{type} Category")
    while numgrade != -1:
        numgrade = float(input(f"Enter grade for Category {type} : "))
        catGrade.append(numgrade)
        #Since final exam is only one grade, only allow it to loop once
        if type == 'Final Exam':
            break
        else:
            pass
    # Try to remove the negative 1 from the list if it exists so it doesn't mess with the averages.
    try:
        catGrade.remove(float("-1.0"))
    except:
        pass
    #average out grades and add to corresponding category
    comp163CatGrades[type] = sum(catGrade)/(len(catGrade))
    catGrade.clear()
        
#Multiply each category's average by the weight in order to get correct value for the total grade.
totalGradeList = []
for type in comp163Cat:
    comp163CatGrades[type] = comp163Cat[type] * comp163CatGrades[type]
for grade in comp163CatGrades:
    totalGradeList.append(comp163CatGrades[grade])
total_grade = sum(totalGradeList)

# Test to see what letter grade range the number grade falls into.
if total_grade < 55:
    letter_grade = 'F'
elif total_grade < 60 and total_grade >= 55:
    letter_grade = "D"
elif total_grade < 65 and total_grade >= 60:
    letter_grade = "D+"
elif total_grade < 68 and total_grade >= 65:
    letter_grade = "C-"
elif total_grade < 72 and total_grade >= 68:
    letter_grade = "C"
elif total_grade < 75 and total_grade >= 72:
    letter_grade = "C+"
elif total_grade < 78 and total_grade >= 75:
    letter_grade = "B-"
elif total_grade < 82 and total_grade >= 78:
    letter_grade = "B"
elif total_grade < 85 and total_grade >= 82:
    letter_grade = "B+"
elif total_grade < 90 and total_grade >= 85:
    letter_grade = "A-"
elif total_grade >= 90:
    letter_grade = "A"

#Print the output
for type in comp163CatGrades:
    print(f"{type} weighted total is {comp163CatGrades[type]:.2f}")
print(f"Your weighted total in the class is : {total_grade:.2f}")
print(f"Your letter grade in the class is : {letter_grade}")