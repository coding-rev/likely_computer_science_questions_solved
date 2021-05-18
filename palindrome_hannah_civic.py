while True:
    user_input = input("Type a word: ")
    palindrome_value = (user_input[::-1])

    if palindrome_value == user_input:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
