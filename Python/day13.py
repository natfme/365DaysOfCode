# Day13 - What grade did I get?

""" 👉 Day 13 Challenge - Grade Generator

This project is going to take some time (and some hard thinking) but will be brilliant once you have it working!

1. You are going to ask the user to type in the name of a test, maximum score they could receive, and how many points they received. For example, your test could be called "Python Skills" and the maximum score is 50 points and the user receives 30 points out of 50 possible points.

2. Figure out the percentage the user received and round to 2 decimal places.

3. Use if/elif statements to show users the letter grade they received.

4. At the end, the user should see the letter grade they received and the percentage correct.

5. Add in emojis to celebrate their good grade or different colors depending on what you think is a good or bad final grade.

----
Here is a grading scale to help you decide the letter grade the user received (feel free to use a different grading scale if you like.)

Letter Grade	Percentage
A+      90-100      90%
A-      80-89       80%
B       70-79       70%
C       60-69       60%
D       50-59       50%
Under   50          40%



"""

print("------- Examen grade calculator 🤓📝 -------")
print()
nameTest = input("Name of test: ")
nameStudent = input("What's your name: ")
maxGrade = int(input("what\'s the max possible grade: "))
grade = int(input("What's your grade in whole numbers: "))

percent = round(grade/maxGrade*100,2)


if percent in range(90,101):
    letterGrade = 'A+ 🥳'
elif percent in range(80,90):
    letterGrade = 'A 😁'
elif percent in range(70,80):
    letterGrade = 'B 😊'
elif percent in range(60,70):
    letterGrade = 'C 😐'
elif percent in range(50,60):
    letterGrade = 'D ☹️'
elif percent in range(0,50):
    letterGrade = 'U 😭'
else:
    print("it's not possible 👀")

print(f"{nameStudent}, you got {percent}% which is a {letterGrade} in your test of {nameTest}")

print("Exam Grade Calculator")
print()
name_of_exam = input("Name of exam: ")
print()
total_score = int(input("Max. Possible Score:"))
your_score = int(input("Your score: "))
print()



number_score = float(your_score / total_score)
final_number = round(number_score, 2)
final_perc = round(float(your_score / total_score)*100, 2)

print("You got",final_perc,"%")

if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")
