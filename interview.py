#Author: Alejandro Veloz
#Date: 3/13/2024
#Description:
#   - This program will show several functions that solve a specific problem.
#     In this case, these are good exercises to prepare for an interview in Python. 
#   - I have found these questions using the following link: https://medium.com/@nikitasilaparasetty/python-interview-coding-questions-with-solutions-for-beginners-7f6d782defac
#   - I will use my own solutions, but in the link above the user also solves the problems using a different algorithm.

# First Exercise:Write a Python program to check if a string is a palindrome.
def Palindrome(word):
    if (Check_Palindrome(word)):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a Palindrome")

def Check_Palindrome(word):
    #Return true if the word is equal, 
    #if it isn't then returns false. 
    return word == word[::-1]  

# 2nd Exercise: Find the factorial of a number
def Factorial(number):
    #I am not a huge fan of recursive functions... Therefore, I will use a while loop instead. 
    factorial = 1
    assistant = number
    while(assistant > 0):
        if (assistant -1 == 0):
            factorial = factorial * 1    
        else:
            factorial = factorial * assistant
        assistant = assistant -1
    
    print(f"The factorial of {number} is {factorial} ")

#3rd Exercise: Find the largest number inside of a list. 
def Find_Largest(numbers):
    largest_number = numbers[0]
    for number in numbers:
        if (number > largest_number):
            largest_number = number
        
    print (f"the largest number in this array is: {largest_number}")

#4th exercise: create a program that reverse a string
def Reverse_String(word):
    return word[::-1]

#5th exercise: Count frequency of a specific element of a list. 
def Check_Frequency (elements, check_var):
    point = 0
    for element in elements:
        if (check_var == element):
            point += 1

    print(f"the frequency of this element is {point} time(s)")

#Exercise #6: check if a number is primer:
def Check_Prime_Number(number):
    if (number <= 1): print(f"{number} is not prime")
    else:
        if (number % 2 == 1): 
            print (f"{number} is prime")
        else:
            print(f"{number} is a composite number")
        

#Test Function:
def Test():
    #test for Palindrome:
    test_word_t = "oso"
    test_word_f = "Alejandro"
    Palindrome(test_word_t)
    Palindrome(test_word_f)

    #Test for Factorial:
    Factorial(4)
    Factorial(6)

    #test for largest number:
    my_list = [10, 1000, 20, 2, 3, 0]
    Find_Largest(my_list)

    #test reverse string 
    word = "Hello"
    print (f"{Reverse_String(word)} is your word reversed")

    #test frequency in a list
    elements = [10, 4, "hello" , 5, 4, 30, "hello"]
    Check_Frequency(elements, 10)

    #Test prime number functions:
    Check_Prime_Number(3)
    Check_Prime_Number(4)
    Check_Prime_Number(1)
    Check_Prime_Number(0)

start = Test()