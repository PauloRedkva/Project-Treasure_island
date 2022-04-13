# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)

if bmi_as_int < 18.5:
    print(f"Your BMI is {bmi_as_int}, you are overweight.")
elif bmi_as_int < 25:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int < 30:
    print(f"Your BMI is {bmi_as_int}, you slightly overweight.")
elif bmi_as_int < 35:
    print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_as_int}, you are clinically obese")


"""

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

"""









"""
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""





"""
BMI Calculator 2.0
UPDATE
We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

Click here

Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

Example Input
weight = 85
weight = 85
height = 1.75
height = 1.75
Example Output
85 ÷ (1.75 x 1.75) = 27.755102040816325

Your BMI is 28, you are slightly overweight.
Your BMI is 28, you are slightly overweight.
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/mGRynIETXuVqoDk8unci

The testing code will check for print output that is formatted like one of the lines below:

"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
Hint

Try to use the exponent operator in your code.
Remember to round your result to the nearest whole number.
Make sure you include the words in bold from the interpretations.
Test Your Code
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-2-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

Solution
https://repl.it/@appbrewery/day-3-2-solution
"""