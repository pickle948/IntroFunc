"""
Unit 01 - Functions - Block 01 - Introduction to Functions
Pair Programming Lab: Functions Boot Camp
Names: ______________________  ______________________  (______________________)

Instructions:
- Complete each TODO.
- Run after each function to test.
- Use parameters + return whenever possible.

Roles (switch halfway)

Driver: types, runs the code, shares screen/keyboard

Navigator: reads instructions, watches for mistakes, explains “why”

(Optional 3rd) Coach: checks requirements, tests edge cases, keeps time

0–3 min: Assign roles, create file, run it once (expect failures).
3–15 min: Complete Parts A–C + run tests after each function.
15 min: Switch Driver/Navigator.
15–25 min: Complete Parts D–E.
25–30 min: Clean up: confirm all tests run, add names, push to GitHub

Each person will turn in a complete copy.  So make sure all of the work is present for both students.

When finished turn this in on Github and Canvas.

This portion is worth 15 points.
"""

print("\n=== PART A: Warm-up Functions ===\n")

# ------------------------------------------------------------
# 1) say_hello(name)
# Prints: Hello, <name>!
# ------------------------------------------------------------
def say_hello(name):
    print('Hello', name)


# ------------------------------------------------------------
# 2) add_numbers(a, b)
# Returns the sum of a and b
# ------------------------------------------------------------
def add_numbers(a, b):
    return a + b


# ------------------------------------------------------------
# 3) multiply(a, b)
# Returns the product of a and b
# ------------------------------------------------------------
def multiply(a, b):
    return a * b


print("\n=== PART B: Return vs Print ===\n")

# ------------------------------------------------------------
# 4) double_value(x)
# Returns x * 2 (DO NOT print inside this function)
# ------------------------------------------------------------
def double_value(x):
    return x * 2


# ------------------------------------------------------------
# 5) report_double(x)
# Prints a message like: Double of 7 is 14
# Uses double_value(x) inside it
# ------------------------------------------------------------
def report_double(x):
    print('Double of 5 is 10')
    double_value(x)


print("\n=== PART C: Mini Challenge (Make it Useful) ===\n")

# ------------------------------------------------------------
# 6) fahrenheit_to_celsius(f)
# Returns Celsius using: (f - 32) * 5/9
# ------------------------------------------------------------
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# ------------------------------------------------------------
# 7) is_even(n)
# Returns True if n is even, otherwise False
# ------------------------------------------------------------
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print("\n=== PART D: Scope Puzzle (No try/except) ===\n")

# Read carefully. Do NOT use try/except.
# ------------------------------------------------------------
# 8) make_username(first, last)
# Returns a username like: first initial + last name, all lowercase.
# Example: make_username("Ada", "Lovelace") -> "alovelace"
#
# NOTE: Do NOT use global variables.
# ------------------------------------------------------------
def make_username(first, last):
    return first.lower() + " " + last.lower()


# ------------------------------------------------------------
# 9) add_tax(price, tax_rate)
# Returns total price after tax.
# Example: add_tax(10.00, 0.07) -> 10.7
#
# NOTE: tax_rate must be a parameter (not global).
# ------------------------------------------------------------
def add_tax(price, tax_rate):
    return price + tax_rate




print("\n=== PART E: Final Team Challenge (1 function, 3 tests) ===\n")

# ------------------------------------------------------------
# 10) describe_number(n)
# Returns a STRING description:
# - "even" or "odd"
# - and "positive", "negative", or "zero"
#
# Examples:
# describe_number(6)   -> "even positive"
# describe_number(-3)  -> "odd negative"
# describe_number(0)   -> "even zero"   (0 is even)
#
# Requirements:
# - Must use is_even(n) inside this function
# - Must return a string (do not print inside)
# ------------------------------------------------------------
def describe_number(n):
    even_or_odd = ''
    if is_even(n):
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    sign = ''
    if n > 0:
        sign = 'positive'
    elif n < 0:
        sign = 'negative'
    else:
        sign = 'zero'

    return f'{even_or_odd} {sign}'


# ============================
# TEST ZONE (Do not delete)
# ============================

# Part A tests
say_hello("Nick")
say_hello("Ada")

print("add_numbers(3, 4) =", add_numbers(3, 4))
print("add_numbers(-2, 10) =", add_numbers(-2, 10))

print("multiply(3, 5) =", multiply(3, 5))
print("multiply(-2, 8) =", multiply(-2, 8))

# Part B tests
print("double_value(7) =", double_value(7))
print("double_value(0) =", double_value(0))
report_double(7)
report_double(12)

# Part C tests
print("fahrenheit_to_celsius(68) =", fahrenheit_to_celsius(68))
print("fahrenheit_to_celsius(32) =", fahrenheit_to_celsius(32))

print("is_even(10) =", is_even(10))
print("is_even(7) =", is_even(7))

# Part D tests
print("make_username('Ada', 'Lovelace') =", make_username("Ada", "Lovelace"))
print("make_username('Grace', 'Hopper') =", make_username("Grace", "Hopper"))

print("add_tax(10.00, 0.07) =", add_tax(10.00, 0.07))
print("add_tax(50.00, 0.05) =", add_tax(50.00, 0.05))

# Part E tests (3 required)
print("describe_number(6) =", describe_number(6))
print("describe_number(-3) =", describe_number(-3))
print("describe_number(0) =", describe_number(0))