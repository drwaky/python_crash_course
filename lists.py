# Creating an empty list
# 'list = []'
empty_list = []
print(f"Empty list: {empty_list}")


# Creating a list with elements
# 'list = [X, Y, Z]'
star_wars_characters = ['luke skywalker', 'darth vader', 'princess leia',
    'han solo', 'obi-wan kenobi']


# Print the list
print(f"The whole list: {star_wars_characters}")


# Access the first element, the index of a list starts at 0
# 'list[i]'

# It is an immutable operation, the original list is not modified.

# If the index is out of range, an 'IndexError' is raised
print(f"First element 'list[0]': {star_wars_characters[0].title()}")


# Negative indexes start from the end of the list
# 'list[-1]' is the last element
# 'list[-2]' is the second to last element

# It is an immutable operation, the original list is not modified.

# If the index is out of range, an 'IndexError' is raised
print(f"Last element 'list[-1]': {star_wars_characters[-1].title()}")
print(f"Second to last element 'list[-2]': {star_wars_characters[-2].title()}")


# Modifying an element of the list by it's index
# 'list[i] = X'

# It is a mutable operation, the original list is modified.

# If the index is out of range, an 'IndexError' is raised
print("\nModifying the first element"
    f" 'list[0] = X':\n\t {star_wars_characters}")

star_wars_characters[0] = 'yoda'

print(f"At 0\t {star_wars_characters}")


# Adding elements at the end of the list
# 'list.append(X)'

# It is a mutable operation, the original list is modified.
print("\nAdding elements at the end of the list"
    f" 'list.append(X)':\n\t {star_wars_characters}")

star_wars_characters.append('luke skywalker')

print(f"Last\t {star_wars_characters}")


# Inserting elements in the list at a specific index
# 'list.insert(i, X)'

# It is a mutable operation, the original list is modified.

# If the index is out of range, is inserted at the end of the list for a
# positive index and at the beginning of the list for a negative one

# If the index is negative, the element is inserted before the element at the
# negative index
print("\nInserting elements in the list at a specific index"
    f" 'list.insert(i, X)':\n\t {star_wars_characters}")

star_wars_characters.insert(0, 'anakin skywalker')

print(f"At 0\t {star_wars_characters}")

star_wars_characters.insert(1, 'padme amidala')

print(f"At 1\t {star_wars_characters}")

star_wars_characters.insert(-2, 'chewbacca')
print(f"Fore -2\t {star_wars_characters}")


# Removing elements from the list, knowwing it's index, without using it
# 'del list[i]'

# It is a mutable operation, the original list is modified.

# If the index is out of range, an 'IndexError' is raised
print("\nRemoving elements from the list, knowwing it's index, without using it"
    f" 'del list[i]':\n\t {star_wars_characters}")

del star_wars_characters[0]

print(f"At 0\t {star_wars_characters}")


# Removing the last element from the list and using it.
# 'pop' method with no parameter 'list.pop()'

# It is a mutable operation, the original list is modified.

# If the list is empty, an 'IndexError' is raised
print("\nRemoving the last element from the list and using it"
    f" 'list.pop()':\n\t {star_wars_characters}")

last_character = star_wars_characters.pop()

print(f"Last\t {star_wars_characters}")
print(f"Removed element: {last_character.title()}")


# Removing an element from the list, knowing it's index and using it.
# 'pop' method with parameter. 'list.pop(i)'

# It is a mutable operation, the original list is modified.

# If the index is negative, the element is removed from the end of the list

# If the index is out of range, or the list is empty, an 'IndexError' is raised
print("\nRemoving an element from the list, knowing it's index and using it"
    f" 'list.pop(i)':\n\t {star_wars_characters}")

fourth_character = star_wars_characters.pop(-1)

print(f"At 3\t {star_wars_characters}")
print(f"Removed element: {fourth_character.title()}")


# Removing an element from the list by value
# 'remove' method. 'list.remove(X)'

# It is a mutable operation, the original list is modified.

# If the value appears more than once, only the first occurrence is removed

# If the value is not in the list, a 'ValueError' is raised
print("\nRemoving an element from the list by value"
    f" 'list.remove(X)':\n\t {star_wars_characters}")
value_to_remove = 'padme amidala'
star_wars_characters.remove(value_to_remove)

print(f"\t {star_wars_characters}")
print(f"Removed element: {value_to_remove}")


# Reversing the order of the list
# 'reverse' method. 'list.reverse()'

# This method doesn't return a new list, it modifies the original list. It is
# a mutable operation

# The changes are permanent but you can recover the original order by using
# the 'reverse' method again

# The 'reverse' method do not sort the list, it just reverse the order
print("\nReversing the order of the list"
    f" 'list.reverse()':\n\t {star_wars_characters}")

star_wars_characters.reverse()

print(f"\t {star_wars_characters}")

star_wars_characters.reverse()

print(f"\t {star_wars_characters}")


# Sorting the list
# 'sort' method. 'list.sort()'

# This method doesn't return a new list, it modifies the original list. It is
# a mutable operation

# The changes are permanent, you can NOT recover the original order if you do
# not have a copy of the original list before sorting

# The 'sort' method is case sensitive, uppercase letters are sorted before
# lowercase letters
print("\nSorting the list"
    f" 'list.sort()':\n\t {star_wars_characters}")

# Making a copy of the original list
original_order = star_wars_characters.copy()

star_wars_characters.sort()

print(f"\t {star_wars_characters}")

# Recovering the original order
star_wars_characters = original_order.copy()


# Sorting the list in reverse order
# 'sort' method with parameter 'reverse=True'. 'list.sort(reverse=True)'

# This method doesn't return a new list, it modifies the original list. It is
# a mutable operation

# The changes are permanent, you can NOT recover the original order if you do
# not have a copy of the original list before sorting

# The 'sort' method is case sensitive, uppercase letters are sorted before
# (after in reverse) lowercase letters
print("\nSorting the list in reverse order"
    f" 'list.sort(reverse=True)':\n\t {star_wars_characters}")

star_wars_characters.sort(reverse = True)

print(f"\t {star_wars_characters}")

# Recovering the original order
star_wars_characters = original_order.copy()


# Sorting the list temporarily
# 'sorted' function. 'sorted(list)'

# This function returns a NEW list, the original list is NOT modified. It is
# an immutable operation

# The 'sorted' function is case sensitive, uppercase letters are sorted before
# (after in reverse) lowercase letters

# The 'sorted' function can be used too with the 'reverse' parameter
print("\nSorting the list temporarily"
    f" 'sorted(list)':\n\t {star_wars_characters}")

sorted_characters = sorted(star_wars_characters)

print(f"\t {sorted_characters}")

print("\nSorting the list temporarily in reverse order"
    " 'sorted(list, reverse=True)':"
    f" \n\t {star_wars_characters}"
    f" \n\t {sorted(star_wars_characters, reverse = True)}")


# Getting the length of the list
# 'len' function. 'len(list)'
print("\nGetting the length of the list"
    f" 'len(list)':\n\t {star_wars_characters}")

length = len(star_wars_characters)

print(f"Length: {length}")
