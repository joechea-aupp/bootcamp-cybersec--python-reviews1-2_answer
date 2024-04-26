# Write a program that prints out all the numbers from 0 to 9 and whether they are even or odd.
# use a for loop to iterate over the numbers from 0 to 9
# hint: 
# 1. use the range() function to generate a sequence of numbers from 0 to 9
# 2. use the modulo operator % to determine if a number is even or odd
for number in range(10):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
