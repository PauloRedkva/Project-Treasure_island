# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
price = 0

if size == "S":
    price = price + 15
elif size == "M":
    price = price + 20
else:
    price = price + 25

if add_pepperoni == "Y":
    if size == "S":
        price = price + 2
    else:
        price = price + 3

if extra_cheese == "Y":
    price = price + 1
    
print(f"Your final bill is: ${price}")


"""

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

"""
"""
## Pizza Order

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

# Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

# Example Output

```
Your final bill is: $28.
```

e.g. When you hit **run**, this is what should happen:  

 
![](https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4)
  

# Hint

1. Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-4-test-your-code](https://repl.it/@appbrewery/day-3-4-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 



# Solution

[https://repl.it/@appbrewery/day-3-4-solution](https://repl.it/@appbrewery/day-3-4-solution)
"""