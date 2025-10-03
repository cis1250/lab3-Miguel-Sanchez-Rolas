#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.

user_input = input('User input: ')



# Validate that the input is a positive integer.

while user_input < 0:
  print('Expected output: Please enter a positive integer.')
  user_input = input('User input: ')


# Use a for loop to print the Fibonacci sequence up to that many terms.

num = 0
num_one = 1
num_two = 0
temp


for num in range(user_input):
  print(num)
  num = num_one + num_two
  temp = num_one
  num_one = num
  num_two = num_one
