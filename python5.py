# List Comprehension is a short and simple way to create a new list from an existing list using a single line of code.
# Instead of writing a long for loop, we can write it in one line

# SYNTAX
# new_list = [expression for item in iterable if condition]

# Normal for loop vs List Comprehension
# Normal for loop:
numbers = [1, 2, 3, 4, 5]

even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)

print(even)

# using List comprehension

numbers = [1, 2, 3, 4, 5]

even = [i for i in numbers if i % 2 == 0]

print(even)
# ==============================

numbers = [2, 3, 4, 5]

squares = [x*x for x in numbers]

print(squares)

# =============================
marks = [20, 45, 80, 30, 90]

passed = [m for m in marks if m >= 35]

print(passed)