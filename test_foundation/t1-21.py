# Write a program that accepts a list of numbers as command line arguments and prints the count of
# numbers that are above the average.
# Example:
# Input: python3 program.py 3 7 2 9 4
# Output: 2
import sys

# step 1: calculate the average of the numbers
# for x in sys.argv[1:n] --> assing to numbers (list of integers)
numbers = [int(x) for x in sys.argv[1:3]]
print(f"Numbers: {numbers}")

#average = sum(numbers) / len(numbers) if numbers else 0
average = 0
if numbers:
    total = sum(numbers)
    count = len(numbers)
    average = total / count

print(f"Average: {average}")

# step 2: count how many numbers are above the average
count_above_average = 0
# ---2.1 loop through the list of numbers and compare each number to the average
for num in numbers:
    if num > average:
        # ---2.2 if the number is greater than the average, increment the count
        print(f"{num} is above average")
        count_above_average += 1

print(f"Count above average: {count_above_average}")