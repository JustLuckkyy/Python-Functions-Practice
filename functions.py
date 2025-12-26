# """
# Python Logic & Algorithm Portfolio
# Candidate: Lucky
# Topics: functions
# """
# # ==========================================
# # PYTHON PRACTICE EXERCISES - DAY 1
# # ==========================================
#
# from selenium.webdriver.support.expected_conditions import none_of

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



# ==========================================
# 1. LAMBDA FUNCTIONS
# ==========================================
#A quick way to write a small function in one line
cube = lambda x: x ** 3
print(f"Cube of 5 is: {cube(5)}")


# ==========================================
# 2. VARIABLE ARGUMENTS (*args)
# ==========================================
#This function can take any number of integers and sum them up
def add_all_numbers(*args):
    return sum(args)


print(f"Sum of multiple numbers: {add_all_numbers(1, 2, 5, 10, 20)}")
#

# # ==========================================
# # 3. UNDERSTANDING DATA IN *args (The Bag)
# # ==========================================
# # This shows how Python 'packs' items into a tuple inside *args
def check_content(*args):
    print(f"Items received: {args}")
    print(f"Total count of items: {len(args)}")


check_content(10, 20, 30)

#
# # ==========================================
# # 4. GENERATORS (The 'yield' keyword)
# # ==========================================

def even_generator(num):
    for i in range(2, num + 1, 2):
        yield i


print("Testing Generator with a for-loop:")
for j in even_generator(10):
    print(j)


#
# # ==========================================
# # 5. RECURSION (Factorial)
# # ==========================================
## A function that calls itself to solve a math problem
def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n - 1)


print(f"Factorial of 5 is: {find_factorial(5)}")
#
#
# # ==========================================
# # 6. THE SMART MULTIPLIER (Handling User Input)
# # ==========================================
# This handles multiple inputs, splits them, and multiplies them
def multiply_all(*args):
    if not args:
        return 0
    total = 1
    for n in args:
        total = total * n
    return total


# Step-by-step input handling
raw_data = input("Enter numbers to multiply (separated by spaces): ")

if raw_data:
    # 1. Split the string by spaces
    # 2. Convert each string part into an actual integer
    clean_list = [int(x) for x in raw_data.split()]

    # 3. Pass the list into the function using '*' to unpack it
    final_result = multiply_all(*clean_list)
    print(f"The final product is: {final_result}")