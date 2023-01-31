#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
for i in range(1,10+1):
    print(i**3)



# Question 2: Get first prime numbers up to 100
# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

def first_odd():
    for i in range(100):
        if i % 2  !=0:
            print(i)
first_odd()

#question 3 Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = input("How Old are you?: ")
age = int(age)

if age <= 18:
    print("Kid's menu.")
elif age <= 65:
    print("Adult's menu.")
else:
    print("The early bird senior special.")