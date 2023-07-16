prelimGrade = float(input("Enter Prelim Grade: "))
midtermGrade = float(input("Enter Midterm: "))
preFinalGrade = float(input("Enter Pre Final: "))
finalsGrade = float(input("Enter Finals: "))
totalScore = prelimGrade + midtermGrade + preFinalGrade + finalsGrade
averageGrade = totalScore / 4

dict = {
    1: 'You Passed!',
    2: 'You Failed!'
}

if averageGrade >= 75:
    print("\nCongratulations your grade is:",averageGrade)
    print(dict.get(1))
else:
    print("\nBetter luck next time your grade is:",averageGrade)
    print(dict.get(2))
