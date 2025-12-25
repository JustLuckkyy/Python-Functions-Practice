"""
Python Logic & Algorithm Portfolio
Candidate: Lucky Choudhary
Topics: While Loops, For Loops, String Manipulation, Nested Loops
"""


# ==============================================================================
# SECTION 1: BASIC WHILE LOOPS (Iteration & Math)
# ==============================================================================

#1. Range Printing: 10 to 15
num = 10

while num <=15:
    print(num, end=" ")
    num += 1




#2. Mathematical Powers: Cubes of 1 to 5

num = 1
root = 0
while num <=5:
    print(num ** 3, end=" ")
    num += 1




#3. Filtering: Odd Numbers 1 to 10
num = 1
while num <=10:
    if num % 2 != 0:
        print(num,end=" ")
    else:
        pass
    num += 1




# 4. Logic: Calculating Cumulative Product (Factorial Pattern) from 1 to 5
num = 1
m = 1
while num <=5:
    m = (m * num)
    print(m)
    num += 1




# 5. Algorithm: Reversing a String using Negative Step Slicing in a For Loop
wrd = "helloworld"
r_wrd =[]
for i in range(9,-1,-1):

    r_wrd.append(wrd[i])
print(r_wrd)




# 6. Logic: Generating the First Five Multiples of 3 (Multiplication Table)
num = 3
numm = 1
product =1
while numm <=5:
    product =num*numm
    print(product)
    numm += 1



# 7. Logic: Calculating the 4th Power of a Constant using While Loop
num = 3
mlt=1
while mlt <2:
    print(num**4)
    mlt+=1




# 8. Algorithm: Counting Specific Character Occurrences via Manual Indexing
strng = "success"
target = "s"
count = 0
index = 0

while index < len(strng):
    if strng[index] == target:
        count += 1
    index += 1

print(f"Count: {count}")




########################################################################################################################
##################################################### NESTED LOOPS #####################################################
########################################################################################################################


# 9. Pattern: 2D Rectangular Grid Generation (5x11) using Nested Loops
for i in range(5):
    for j in range(10):
        print("#", end="")
    print("#")


# 10. Pattern: Half-Pyramid / Right-Angled Triangle (Inner Loop Dependent on Outer Loop)
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 11. Logic: Generating a 10x10 Multiplication Table (Mathematical Matrix)
for i in range(1,11):
    for j in range(1, 11):
        j = j * i
        print(j,end=" ")
    print()


# Algorithm: Prime Number Discovery (2 to 50) using Nested Divisibility Checks

for i in range(2,51):
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)













