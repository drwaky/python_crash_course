# A tuple is a data structure similar to a list but it is immutable
# The values in a tuple can not be changed, but the tuple can be reasigned to a
# new tuple.
# 'tuple = (x, y, z)'
serie = (2, 4, 6, 8)

# Values in a Tuple can be access using indexes, the same way that in a list.
print(f"First value in the Tuple: {serie[0]}")
print(f"Last value in the Tuple: {serie[-1]}")
print(f"Slicing the tupla to get 2nd and 3rd items: {serie[1:3]}")

# print("\nTrying to modify a value in a Tuple throw an error:")
# serie[0] = 1

# To create a tuple with only one element you need to add the comma ','
# tuple = (x,)
single_value_tuple = (8,)
print(f"Single value Tuple: {single_value_tuple} 👉 {single_value_tuple[0]}")

# Looping through all values in a Tuple using a 'for' loop
print("\nLooping through all values in a Tuple:")
for number in serie:
    print(number)

# Reassigning the Tuple to a different value
serie = (1, 1, 2, 3, 5, 8)

print("\nNew values in the Tuple:")
for number in serie:
    print(number)
