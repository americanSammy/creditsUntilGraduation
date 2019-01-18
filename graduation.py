totalCreditHours = input("Please enter how many credits you have: ")
toGraduate = 120

if toGraduate >= int(totalCreditHours):
    int(totalCreditHours) >= 119;
    print("You may not graduate.");
    creditsRemaining = int(toGraduate) - int(totalCreditHours);
    print("You still need " + str(creditsRemaining) + " credits.");
    coursesPerSemester = input("How many credits do you take a semester? ");
else:
    print("You may graduate! Congratulations!")

semestersRemaining = int(creditsRemaining) / int(coursesPerSemester)
print("You have " + str(semestersRemaining) + " semesters left before graduation.");
print("Keep up the good work.");
