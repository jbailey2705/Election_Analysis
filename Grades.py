    #What is the score?
from tkinter import E


Score = int(input('What is your test score? '))
    #Determine the grade.
if Score >= 90:
    print('Your grade is an A.')
elif Score >= 80:
    print('Your grade is a B.')
elif Score >= 70:
    print('Your grade is a C.')
elif Score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is a F.')