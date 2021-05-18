#Program to ask a user a number

# Algorithm
#1. Ask the users number
#2. get all the even numbers
#3. Compare the user number to the even numbers
#4. Print GOOD if the user's number is even

#CODE:
while True:

    user_num = int(input("Enter your number: "))

    mod = user_num % 2

    
    if mod != 0:
        print("You entered an odd number")
        print("")
    else:
        print("Good. You entered an even number")
        print(" ")

