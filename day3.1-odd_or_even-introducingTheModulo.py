# Modulo Operation
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
      print("This is an even number.")
else:
  print("This is an odd number.")


"""

if number % 2 == 0:
  print("This is an even number.")
#Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")

"""


"""
Odd or Even
UPDATE
We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

Click here

Instructions
Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

6 % 2 = 0
6 % 2 = 0
5 ÷ 2 = 2 x 2 + 1, remainder is 1.

5 % 2 = 1
5 % 2 = 1
14 ÷ 4 = 3 x 4 + 2, remainder is 2.

14 % 4 = 2
14 % 4 = 2
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input 1
43
43
Example Output 1
This is an odd number.
This is an odd number.
Example Input 2
94
94
Example Output 2
This is an even number.
This is an even number.
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/bkF9TKJSTGksvxNzOtba

Hint
All even numbers can be divided by 2 with 0 remainder.
Try some using the modulo with some odd numbers e.g.
3 % 2
3 % 2
5 % 2
5 % 2
7 % 2
7 % 2
Then try using the modulo with some even numbers e.g.

4 % 2
4 % 2
6 % 2
6 % 2
8 % 2
8 % 2
See what's in common each time.

Test Your Code
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-1-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

Solution
https://repl.it/@appbrewery/day-3-1-solution

"""