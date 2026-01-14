"""
Unit 01 - Functions - Block 01 - Introduction to Functions
Guided Note
Students: fill in the blanks by writing answers in COMMENTS and completing the TODO code.
Run this file often to see what happens.

When finished turn this in via Github and Canvas.

This portion is worth 5 points.
"""


# ============================================================
# 0–3 min — Warm-Up: “Code déjà vu”
# Notice the repeated parts. What’s annoying about this?
# Functions help because they let us:
# ✅ Eliminate repetition
# ✅ ________________________________________________
# ============================================================

print("Welcome!")
print("Here are the rules...")
print("Be kind.")

print("\n" + "-" * 60 + "\n")


# ============================================================
# 3–7 min — What is a function?
# A function is a block of code
# that runs when it is called.
#
# Why we use functions (2 big reasons):
# 1) Organization:
# 2) Reuse (DRY): DRY means “Don't Repeat Yourself”
# ============================================================


# ============================================================
# 7–12 min — Function vocabulary
# - Define a function = write it using the keyword def
# - Call a function with name my_func = my_func()
# - Parameter = a variable in the function definition / block
# - Argument = the actual value you pass in when calling the function
# ============================================================

def greet(name):  # name is a parameter
    print("Hello", name)

greet("Ada")      # "Ada" is an argument

print("\n" + "-" * 60 + "\n")


# ============================================================
# 12–18 min — Anatomy of a function (the “shape”)
#
# Template:
# def function_name(parameters):
#     # function body (indented!)
#     statements
#     return value
#
# Label the parts of this:
# def add(a, b):
#     total = a + b
#     return total
#
# - function name: add
# - parameters: a, b
# - function body:      total = a + b
# #   return total
# - return statement: return total
#
# Indentation rule:
# Everything inside the function must be indented at least once.
# ============================================================

def add(a, b):
    total = a + b
    print(total)


print("add(3, 4) =", add(3, 4))

print("\n" + "-" * 60 + "\n")


# ============================================================
# 18–22 min — `print` vs `return` (super important)
# `print` shows something to the Terminal/Console.
# `return` sends a value back to the function call.
#
# Predict what happens BEFORE running:
# What prints to the screen?
# 1) Value of X doubled is printed
# 2) Our case of X is 5, printing 10
#
# What is `result` equal to?
#
# Key idea: If a function has no `return`, it returns None
# ============================================================

def double_print(x):
    print(x * 2)

result = double_print(5)
print("result =", result)

print("\n" + "-" * 60 + "\n")


# ============================================================
# 22–26 min — Function Scope (Local vs Global)
# Scope means: where a variable lives
# (and can be used).
#
# Big rule:
# Variables created inside a function are local variables.
# - They exist only in the function
# - They cannot be used outside the function
#
# Variables created outside a function are global variables.
# - They can be used anywhere

# - But functions usually should not depend on globals too much.
# ============================================================

# --- Example: Local variables stay in the function ---
def demo():
    x = 10  # local variable
    print("inside:", x)

demo()

# Predict:
# If we try to use x out here (outside demo), what happens?
# Does it work? YES / NO
# If NO, what error do you expect? Unresolved reference
#
# IMPORTANT: We are NOT running the "outside x" line yet because it will stop the program.
# You'll test it later in the OPTIONAL section at the bottom.

print()

# --- Example: Using a global variable (reading is allowed) ---
score = 0

def show_score():
    print("score =", score)

show_score()

# This works because the function is only _____________________ the global variable.

print()

# --- Example: Changing a global variable (tricky!) ---
# Predict: Does this run? YES / NO
# If NO, why? ________________________________________________

# This code is shown for learning; DON'T run it unless your teacher tells you to.
# def add_point_broken():
#     score = score + 1   # <-- what happens?

# Fix option 1 (recommended): Use parameters + return instead of globals
def add_point(score):
    return score + 1

score = add_point(score)
print("score after add_point(score) =", score)

# Fix option 2 (use carefully): global keyword
score2 = 0

def add_point_global():
    global score2
    score2 = score2 + 1

add_point_global()
print("score2 after add_point_global() =", score2)

# When should you use `global`?
# ➡️ Almost never. Prefer ________________________________.

print()

# Quick check:
# In this code, identify the local variables and the global variab