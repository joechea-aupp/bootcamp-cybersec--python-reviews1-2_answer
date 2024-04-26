
greet = "Hello, World!"

reversed_greet = []
for char in greet:
    reversed_greet.append(char)

reversed_greet.reverse()
print(''.join(reversed_greet))  # !dlroW ,olleH
# or
print(greet[::-1])  # !dlroW ,olleH
