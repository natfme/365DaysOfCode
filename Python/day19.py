# Day 19 -Let's Be a Bit Lazy!

# What if you do have an idea of how often you want something to repeat (or you just want to be a bit lazy)? Introducing...the `for` loop.

"""
For Loop
A while loop is perfect to use when we don't know how many times we want the loop to repeat.

If we have an idea of how many times we want the loop to repeat, we can use a for loop to loop code in exactly the same way the while loop did.

However, we can set up the variable, control condition, and increment all in ONE line of code.

Let's compare
Here is how we created a counter with a while loop:

counter = 0
while counter < 10:
  print(counter)
  counter += 1
And here is the same counter using a for loop:

for counter in range(10):
  print(counter)

Range ----------------------------------
The range function creates a list of numbers in the range you create. If you only give it one number, it will start at 0 and move to a state where the final number is one less than the number in the brackets. In this case, the final number would be 9.

range(10)
Note: The variable is only there during the loop, not after it is completed.

Fun fact ------------------------------------------
Commonly computer programmers use the variable names i, j, and k when using for loops for counter. There is no real reason. It's just how everyone has always done it. However, feel free to use a variable that has a bit more meaning if you like.

for days in range(7):
  print("Day", days)
"""
#👉 Day 19 Challenge

"""
A common thing people do is borrow money. When people repay money, they pay interest which is paid back annually and added to the original amount the person borrowed.

You are going to create a loan calculator that shows how much money you owe for a loan of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.

This means each year the amount of money you owe will increase 5%.

Figure out how much you owe altogether for 10 years?

Use a for loop and one or two lines of looped code to determine the answer. (Hint: Don't make this overcomplicated. It should only be a few lines of code altogether.)

Hints:
Make sure the for loop happens 10 times.
Start your value (amount you are borrowing) before the loop starts.
If you need to count on one more number, just write i+ in the print statement to tell the computer to add the next number.
"""
loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))