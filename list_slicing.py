# Let's work with part of a list
star_wars_characters = ['luke skywalker', 'darth vader', 'princess leia',
    'han solo', 'obi-wan kenobi', 'yoda', 'palme', 'r2-d2', 'c3po']

# Slicing is similar to the 'range' function. It uses three indexes starting in 0
# 'list[start:end:step]'
# First index to the starting point, second index to the end, and the third one.
# to set the step sice, 1 = every item, 2 = each 2 items, and so on As 'range'
# function, it will end in 'end' -1. So [1:4] Will return a sub-list with the
# second item to the forth, idexes 1 to 3.
print(f"The whole list: {star_wars_characters}")
print(f"\n'star_wars_characters[0:3]' 👉 {star_wars_characters[0:3]}")

# You can generate a subset of a list, like 2nd, 3rd, 4th, and 5th items
print(f"'star_wars_characters[1:4]' 👉 {star_wars_characters[1:5]}")

# Omiting the first index in a slice, starts the slice at the beginning of the
# list, position, index 0
print(f"'star_wars_characters[:2]' 👉 {star_wars_characters[:2]}")

# The same works for the second index in the slice, if you omit it, the slice
# will include the items from the first index through the last item.
print(f"'star_wars_characters[3:]' 👉 {star_wars_characters[3:]}")

# A third index included in the slice will define the step sice in the slicing
# meaning add the item every 1, 2, 3 or "n" items.
# list[1:7:2] 👉 From the second item to the sixth every 2 items.
print(f"'star_wars_characters[1:7:2]' 👉 {star_wars_characters[1:7:2]}")

# A negative index means counting from the end of the list. So 'list[-3:]' will
# return the last 3 items in the list
print(f"'star_wars_characters[-3:]' 👉 {star_wars_characters[-3:]}")

# A negative 'step' means retreaving the items in reverse with that step size
print(f"'star_wars_characters[-3:1:-2]' 👉 {star_wars_characters[-3:1:-2]}")

# When we are slicing in reverse the 'end' idex' item must be to the left of the
# 'start' index item, meaning the index of a previous item than 'start' index.
# So omiting the second index means till the begining of the list.
print(f"'star_wars_characters[4::-2]' 👉 {star_wars_characters[4::-2]}")
# 👆 From the 5th element to the begining of the list in reverse, every 2 items

print(f"\nLet's print the three first characters:")
# We can loop through a slice using 'for' loop.
for character in star_wars_characters[:3]:
    print(character.title())

# Copying a list
# If we use equal "=" with one list into another, we are NOT creating a copy,
# but another reference to the same list of items. We can make a copy by slicing
# the whole list ([:])
print("\nLet's demostrate how copy with '=' is not copying at all, but "
    "another reference to the same list, and how slicing the whole list"
    " '[:]' will create a totally separated copy.\n")

rebels = ['luke skywalker', 'obi-wan kenobi', 'yoda']
jedis = rebels

jedis.append('asoka')
rebels.append('chewbacca')

print(f"Revels: {rebels}")
print(f"Jedis: {jedis}")
print("👆The same lists after appending diferent characters to each one\n")

rebels = ['luke skywalker', 'obi-wan kenobi', 'yoda']
jedis = rebels[:]

jedis.append('asoka')
rebels.append('chewbacca')

print(f"Revels: {rebels}")
print(f"Jedis: {jedis}")
print("👆Diferent lists after appending diferent characters to each one\n")
