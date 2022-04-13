"""logical_operators

if condition & condition2 & condition3:
    do this 
else:
    do this

Logical operators:

A and B | True (both True) or False (one this are false or both are False)
C or D  | True (one this condition is True) or False (both False)
not E   | Reverse condition (if True is False ,  if False is True)

"""
print("Welcome to the rollercoaster!")
height = int(input("What is yout height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    
    age = int(input("What is your age?"))
    
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
         
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:   
        bill = 12
        print("Adults tickets are $12.")
    
           
    wants_photo = input("Do you want to a photo taken? Y or N.")
    if wants_photo == 'Y':
    #Add $3 to their bill
        #bill = bill + 3
        bill += 3
        print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")