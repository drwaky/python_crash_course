characters = ['luke', 'darth vader', 'leia',
    'han solo', 'obi-wan kenobi', 'r2d2', 'yoda']

# Double equal sign '==' is the 'equality operator' that returns 'True' or
# 'False' if the values on the left and right side of the operator match or not.

for character in characters:
    if character == 'r2d2':
        print(character.upper())
    else:
        print(character.title())

# The 'equality operator' in Python is case sensitive. If case doesn't matter,
# you can use 'lower' for compare, what do not modify the original value.

print(f"\n{characters[0].lower() == 'luke'}")  # True


# To determine whether two values are not equal, you can use the 'inequality
# operator' 👉 '!=' that returns 'True' if the values on the left and right of
# operator do not match and 'False' if they do.

print(f"\n{characters[0].lower() != 'yoda'}")  # True


# Comparing Numbers.

CELL = 2187

print(f"\nCELL: {CELL}")
print(f"Less than '<': CELL < 2200: {CELL < 2200}")  # True
print(f"Less than or equal to '<=': CELL <= 2188: {CELL <= 2188}")  # True
print(f"Equal to '==': CELL == 2187: {CELL == 2187}")  # True
print(f"Greater than '>': CELL > 2180: {CELL > 2180}")  # True
print(f"Greater than or equal to '>=': CELL >= 2186: {CELL >= 2186}")  # True


# Checking multiple conditions with 'and' and 'or'.

BLOCK = 1138

print(f"\nCELL: {CELL}")
print(f"BLOCK: {BLOCK}")
print(f"'and': CELL < 2200 and BLOCK > 1100: "
      f"{CELL < 2200 and BLOCK > 1100}")  # True and True 👉 True
print(f"'or': CELL < 2100 or BLOCK > 1100: "
      f"{CELL < 2100 or BLOCK > 1100}")  # False or True 👉 True


# Checking if a Item IS 'in' a list

VIP = 'yoda'
print(f"\nIs our VIP (Yoda) in the character list?: {VIP in characters}")

# Another way with an if:
if VIP in characters:
    print(f"{VIP.title()} is in da house!")


# Checking if a Item is NOT 'in' a list

VIP2 = 'c3po'
print(f"\nIs not our VIP2 (C3PO) in the character list?: {VIP2 not in characters}")

# Another way with an if:
if VIP2 not in characters:
    print(f"{VIP2.upper()} is not in the list!")


# Boolean Expressions

# A 'boolean expression' is just another name for a conditional test.
# When a 'boolean expression' is evaluated, the result is a 'boolean value',
# witch is either 'True' or 'False'.

movie_is_good = True
empire_wins = False

print(f"\nIs the movie good?: {movie_is_good}")


# if Statements

# An 'if' statement tests for a condition and then responds to that condition.
# If the condition is 'True', the following code statement will be executed.
# If the condition is 'False', the following code statement will be skipped.

# Syntax:
# if conditional_test:
#     do something

if movie_is_good:
    print("\nThis movie is awesome!") # This will be printed.

if empire_wins:
    print("\nEmpire wins!") # This will not be printed.


# if-else Statements

# An 'if-else' is similar, but the 'else' statement allows you to define an
# action or set of actions that are executed when the condition is 'False'.

# Syntax:
# if conditional_test:
#     do something
# else:
#     do something else

if movie_is_good:
    print("\nThis movie is awesome!") # This will be printed.
else:
    print("\nThis movie is not so good!") # This will not be printed.

if empire_wins:
    print("\nEmpire wins!") # This will not be printed.
else:
    print("\nRebels wins!") # This will be printed.

# Having several actions indentend at the same level after the 'if' or 'else'
# statement is called a 'block of code', and it will be executed together.

if movie_is_good:
    print("\nThis movie is awesome!") # This will be printed.
    print("I love it!") # This will be printed.
else:
    print("\nThis movie is not so good!") # This will not be printed.
    print("I don't like it!") # This will not be printed.


# if-elif-else Chain

# If we need to check more than two conditions, we can use an 'if-elif-else'
# chain. Python executes each 'if' and 'elif' statement in order, and stops at
# the first 'if' or 'elif' that evaluates to 'True'. The block of code just
# after that 'if' or 'elif' is executed and the rest of the tests are skipped.
# If none of the conditions are 'True', the code block under 'else' is executed.

# Syntax:
# if conditional_test_1:
#     do something
# elif conditional_test_2:
#     do something else
# else:
#     do something else

movie_is_action = False
movie_is_fantasy = False
movie_is_scifi = True

if movie_is_fantasy:
    print("\nThis movie is a Fantasy movie!") # This will not be printed.
elif movie_is_scifi:
    print("\nThis movie is a Sci-Fi! movie!") # This will be printed.
else:
    print("\nThis movie is from a different genere") # This will not be printed.

# You can use if to set the correct value of a variable based on a condition.
if movie_is_fantasy:
    genere = "Fantasy" # This will not be printed.
elif movie_is_scifi:
    genere = "Sci-Fi" # This will be printed.
else:
    genere = "Unknown" # This will not be printed.

print(f"\nThe genere of the movie is {genere}") # Sci-Fi

# You can use as many elsif blocks as you need in your code. Python will
# execute each one of them in order, and stops at the first one that evaluates
# to 'True'. If none of the conditions are 'True', the code block under 'else'
# is executed.

if movie_is_fantasy:
    genere = "Fantasy" # This will not be printed.
elif movie_is_action:
    genere = "Action" # This will not be printed.
elif movie_is_scifi:
    genere = "Sci-Fi" # This will be printed.
else:
    genere = "Unknown" # This will not be printed.

print(f"\nThe genere of the movie is {genere}") # Sci-Fi


# The 'else' block is optional. If you don't want to do anything when none of
# the conditions are 'True', you can omit it.

if movie_is_fantasy:
    genere = "Fantasy" # This will not be printed.
elif movie_is_action:
    genere = "Action" # This will not be printed.
elif movie_is_scifi:
    genere = "Sci-Fi" # This will be printed.

print(f"\nThe genere of the movie is {genere}") # Sci-Fi
