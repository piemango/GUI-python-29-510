import random
target = 72
count = 0
while True:
    n = int(input("Enter your number : "))
    count += 1 
    if n == target:
        print("Congratulations, your guess is correct. \nTotal number of guess is %d" %count)
    elif n>100:
        print("Sorry your guess is out of range")
    elif n<0:
        print("Sorry your guess is out of range")
    elif n> target:
        print("Sorry your guess is too high")
    elif n< target:
        print("Sorry your guess is too low")