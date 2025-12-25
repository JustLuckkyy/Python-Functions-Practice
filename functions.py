"""
Python Logic & Algorithm Portfolio
Candidate: Lucky
Topics: functions
"""
# ==========================================
# PYTHON PRACTICE EXERCISES - DAY 1
# ==========================================

from selenium.webdriver.support.expected_conditions import none_of

# ------------------------------------------
# 1. Number Existence Check in a List
# ------------------------------------------
def number_in_list(num):
    numbers = [1, 2, 3, 4, 5]

    for i in numbers:
        if num in numbers:
            return True
        else:
            return False


number = number_in_list(6)
print(number)


# ------------------------------------------
# 2. Even or Odd Number Finder
# ------------------------------------------

def to_find_square(num):
    if num % 2 == 0:
        return("number is even")
    else:
        return("number is odd")

number = int(input("Enter a number: "))
square = to_find_square(number)
print(square)



# ------------------------------------------
# 3. Square of a Number Calculation
# ------------------------------------------


def to_find_square(num):
    x = (num ** 2)
    if num:
        return x
    else:
        return 0

number = int(input("Enter a number: "))
square = to_find_square(number)
print(square)




# ------------------------------------------
# 4. Simple Addition Function
# ------------------------------------------
def func_to_get_sum(a,b):
    return a+b


sum = int(input("Enter the sum : "))
sum2 = int(input("Enter the sum : "))
print(func_to_get_sum(sum,sum2))


# ------------------------------------------
# 5. String and Number Multiplication
# ------------------------------------------

def multiplying(num1, num2):
    return num1 * num2

print(multiplying(3,"h"))




# ------------------------------------------
# 6. Circle Area and Circumference Calculator
# ------------------------------------------
## calculating area and circumference of a circle by its radius

def calc_area_and_circumference(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

answer = int(input())
area, circumference = calc_area_and_circumference(answer)
print(area, circumference)


# ------------------------------------------
# 7. Greeting Function with Default Parameters
# ------------------------------------------
## Topic: Functions with Default Parameters

def greeting(name="Guest"):
    return f"Hello {name}, Welcome to the team!"


print(greeting("Lucky"))
print(greeting())

















