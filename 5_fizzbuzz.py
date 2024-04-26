# fizzbuzz
# Write a program that prints the numbers from 1 to 25. For number that divisible by three print “Fizz” instead of the number and if it is divisible by of five print “Buzz”. For numbers that is disible by both three and five print “FizzBuzz”.

for number in range(1, 26):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
