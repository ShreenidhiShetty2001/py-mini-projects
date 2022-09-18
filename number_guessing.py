#generate a random number and ask the user to guess it
# every time they guess a number we tell them if it above or below the number to be guessed
# we ask them the range

import random

print("Enter the range")
start = int(input("Enter start vale:\n"))
stop = int(input("Enter stop value:\n"))

num = random.randint(start,stop)
val = 0
while(val != num):
    val = int(input("Guess a number\n"))
    if (val == num):
        print("you have guessed the number correctly")
    elif(val > num):
        print("this is higher than the number")
    else:
        print("this is lower than the number")
