# find the largest number in a given number
# example: 569 -> 9
number = 569

str_number = str(number)
number_list = []

for item in str_number:
    number_list.append(int(item))

print(max(number_list))
