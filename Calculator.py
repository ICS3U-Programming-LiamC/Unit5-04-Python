#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 4, 2021
# This program gets an operator, and two numbers from the user, then combines
# then depending on the input


def calculate(oper, num1, num2):
    determiner = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
        '%': num1 % num2,
    }
    # this is from
    # https://www.geeksforgeeks.org/switch-case-in-python-replacement/
    # it returns the result, and if none of the conditions are met
    # it will return -1
    return determiner.get(oper, "ERROR")


def factorial(num1):
    # set counters and result to 1 so that facotrial works
    counter = 1
    result = 1
    while counter < num1 + 1:
        # do the factorial
        result = counter * result
        counter = counter + 1
    # return the result to the user
    return result


# welcome the user to the program
def greet():
    print("This program takes an operator, and two numbers then\
combines them depending on the your inputs")


# the main function where all the first steps happen
def main():
    # get operator and num1
    operator = input("What is your operator (+, -, *, /, %, !): ")
    user_num1 = input("What is your first number: ")
    # make sure the users num can be an integer
    try:
        # make sure the num is a num, and check if the user did
        # factorial, because facotrial only needs 1 num
        user_num1 = float(user_num1)
        if (operator == "!"):
            # call the function with the parameter
            result = factorial(user_num1)
            # print the result to the user
            print(result)
        else:
            # get the second num and check for errors
            user_num2 = input("What is your second number: ")
            try:
                user_num2 = float(user_num2)
                # call the calculator function, which handles some operators
                # with 2 inputs
                result = calculate(operator, user_num1, user_num2)

                if (result == "ERROR"):
                    print("{} is not a valid operator".format(operator))
                    main()
                else:
                    # print the result to the user
                    print(result)
            # if there is an error
            except ValueError:
                # print the error
                print("Not a valid number")

    # if there was an error in the first num
    except ValueError:
        print("Not a valid number")


# get the program started
if __name__ == "__main__":
    greet()
    main()
