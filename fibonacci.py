#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
print('User input: ')
user_input = input()



# Validate that the input is a positive integer.

while not user_input.isdigit() or int(user_input) < 0:
  print('Expected output: Please enter a positive integer.')
  print('User input: ')
  user_input = input()

user_input = int(user_input)
# Use a for loop to print the Fibonacci sequence up to that many terms.

num_one = 0
num_two = 1



for i in range(user_input):
    print(num_one, end='')
    if i < user_input - 1:
        print(' ', end='')
    temp = num_one
    num_one = num_two
    num_two = temp + num_two
