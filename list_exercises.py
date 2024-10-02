# Count to 20 using a 'for' loop
print("Counting to 20 using a 'for' loop:")

for number in range(1, 21):
    print(number)

# Make a list with the numbers from 1 to 1.000.000 and use a 'for' loop to print
# them

print("Printing one million numbers in a list using 'for' loop:")
numbers = list(range(1, 1_000_001))
## Uncomment next two lines it you want to see the numbers being printing
## be aware that it takes some time to execute
# for number in numbers:
#     print(number)


# Make a list with the numbers from 1 to 1.000.000 and use 'min' and 'max' to
# check if the list has all the numbers and then 'sum' to calculate the
# summation value of the list of the first 1M numbers.

print(f"\nCreating a list of 1M numbers, and printing the minimum, maximum, and"
      "the summation of all the numbers in the list:")

one_million_numbers = list(range(1, 1_000_001))
min = min(one_million_numbers)
max = max(one_million_numbers)
sum = sum(one_million_numbers)

print(f"\nThe minimum value is: {min}")
print(f"The maximum value is: {max}")
print(f"The summation is: {sum}")


# Using range and a for loop print the odd numbers from 1 to 20
print("\nPrinting the odd numbers from 1 to 20")
odd_numbers = list(range(1, 20, 2))
for odd_number in odd_numbers:
    print(odd_number)

# Using range and a for loop print multiples of 3 from 3 to 30
print("\nPrinting the multiples of 3 from 3 to 30")
multiples_numbers = list(range(3, 31, 3))
for multiples_number in multiples_numbers:
    print(multiples_number)

# An alternative way using list comprehension expression
print("\nPrinting the multiples of 3 from 3 to 30 using list comprehension")
multiples_numbers2 = [value * 3 for value in range(1, 11)]
for multiples_number in multiples_numbers2:
    print(multiples_number)

# Make a list with the ten first cubes and print them with a for loop
print("\nPrinting the ten first cubes")
cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)

for cube in cubes:
    print(cube)

# Make a list with the ten first cubes and print them with a for loop using
# list comprehension expression
cubes2 = [number ** 3 for number in range(1, 11)]

for cube in cubes:
    print(cube)
