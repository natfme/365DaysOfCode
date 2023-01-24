#Day 10 - A little bit of math
#So far we have introduced the computer to two types of numbers:

#float: numbers with a decimal
#int: whole numbers

adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

""" #👉  Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
3.4 * 6.8

# division
2467 / 4673

#raise 10 to the power of 2

# print the remainder when 343 is divided by 4
print("343 // 100") """


#Fix My Code------------------
print(3.4 * 6.8)

# division
print(2467 / 4673)

#raise 10 to the power of 2
print(10**2)

# print the remainder when 343 is divided by 4
print(343 % 4)

"""Let's split the bill
Did you have fun messing with those mathematical symbols? Now let's put them to good use.

You and your friends went to dinner and need to split the bill. Being the clever friend you are, you can use your code to discover how much each person owes. (Remember, myBill is a float because the total bill will probably have a decimal point and numberOfPeople is an int because you did not go to dinner with .7 of a person.)"""

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)

"""Did you get a really funky number with sooo many decimal points?

 

You can take your answer and use round. Round has two components: "What am I rounding?" and "How many decimal places am I rounding to?"

Add this portion of code after answer and before print. This shows you are rounding answer to 2 decimal points."""

answer = round(answer, 2)
print(answer)

"""Day 10 Challenge
Extend your bill calculator
Add a tip function that adds the total tip to the bill before splitting it equally between the people.

Ask the user for the total bill amount.
Ask what % of tip they will leave to be added to the bill total.

Figure out how to get the total bill with tip then add that to original amount.

Ask the user how many people are splitting the bill and divide by the total.
You can use the same code to get started:

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
"""

myBill = float(input("What was the bill?: "))
tip = myBill * 0.15
totalBill = myBill + tip
numberOfPeople = int(input("How many people?: "))
answer = totalBill / numberOfPeople
print("You all owe", answer)


myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))


bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount)
