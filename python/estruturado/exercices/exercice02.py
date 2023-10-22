# If grade is bigger or equal 7, student approved
# If grade is lower than 7 and bigger or equal 5, student in recovery
# If grade is lower than 5, student reproved

grade = float(input('Type student grade: '))

if grade > 10 or grade < 0:
    print('Invalid grade')
elif grade >= 7:
    print('Student Approved')
elif grade >= 5:
    print('Student in recovery')
else:
    print('Student reproved')
