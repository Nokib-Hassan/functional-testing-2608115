"
Practical Assignment: Functional Testing, CI/CD and Live Deployment

Students receive target.py (16 functions: 11 data-type, 5 mathematics). Test it, host it on GitHub, automate it with GitHub Actions, add a frontend, and deploy it so every push is tested and goes live. Individual work, 20 points + 2 bonus, due [date and time].

Do not modify target.py; the original is restored at grading. Report suspected bugs in your README.

Part 1: Functional tests (8 points)

Write tests/test_target.py that tests every corner case of all 16 functions.

• Cover valid inputs, boundary values, invalid values and wrong types for each function.

• Use parametrize, and pytest.raises with the exact exception class (plus match= where needed).

• Check result types where they matter; use pytest.approx only for inexact results.

• Reach 100% line and branch coverage: pytest --cov=target --cov-branch.

• No skip, xfail or other hidden failures.

Grading: corner cases 4 (0.25 per function), catching hidden faulty versions 2, precise assertions 1, coverage and quality 1.

Part 2: GitHub repository and sync (3 points + 2 bonus)

• Create functional-testing-<student-id> and give the instructor access.

• Make at least 10 focused commits with clear messages.

• Include .gitignore and a pinned requirements.txt; never commit secrets.

• Write a README with setup, test command, live URL, CI badge and suspected bugs.

Bonus: 3+ feature branches merged via pull requests (+1); branch protection on main requiring CI (+1).

Part 3: GitHub Actions workflow (3 points)

Create .github/workflows/ci.yml that:

• runs on every push and on pull requests to main, in a job named test;

• tests on Python 3.10, 3.11 and 3.12 with pip caching;

• lints, runs all tests and fails below 100% coverage of target.py;

• uploads the coverage report as an artifact, with a status badge in the README.

Include one red run from a failing test, then a green fix.

Part 4: Frontend interaction (3 points)

Build a web frontend that runs the target.py functions and shows each result or error. Design and technology are your choice; instructors evaluate it directly. Part 5: Deploy, integrate and test on push (3 points)

push-to-live pipeline · 3 jobs, 1 gate

• Deploy publicly (e.g. Render, Railway, PythonAnywhere) with direct auto-deploy off.

• Add a deploy job with needs: test that runs only on pushes to main and uses a GitHub secret.

• Make /health return the deployed commit SHA, and show it in the frontend.

• Add a smoke-test job that waits for the new SHA on the live site and checks three live requests.

• Record a 3–5 minute demo: a change going live with a matching SHA, and a failing push blocked from deploying.
"

""""target.py - simple functions for practising functional testing."""

import math


# 1. Integer: True if age is 18 or more. Negative age raises ValueError.
def is_adult(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18


# 2. Float: convert Celsius to Fahrenheit, rounded to 2 decimals.
def celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)


# 3. String: count vowels (a, e, i, o, u), ignoring case. Non-string raises TypeError.
def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return sum(1 for letter in text.lower() if letter in "aeiou")


# 4. Boolean: return the opposite of flag. Non-bool raises TypeError.
def invert(flag):
    if not isinstance(flag, bool):
        raise TypeError("flag must be True or False")
    return not flag


# 5. None: greet by name, or greet "Guest" if name is None, empty or only spaces.
def greet(name=None):
    if name is None or name.strip() == "":
        return "Hello, Guest!"
    return f"Hello, {name.strip()}!"


# 6. List: return the largest number. Empty list raises ValueError.
def find_max(numbers):
    if len(numbers) == 0:
        raise ValueError("list is empty")
    return max(numbers)


# 7. Dictionary: return the price of item. Missing item raises KeyError.
def get_price(prices, item):
    if item not in prices:
        raise KeyError(f"{item} not found")
    return prices[item]


# 8. Tuple: return the two values swapped. Not exactly 2 values raises ValueError.
def swap(pair):
    if len(pair) != 2:
        raise ValueError("pair must have exactly 2 values")
    return (pair[1], pair[0])


# 9. Set: return the items found in both sets.
def common_items(set_a, set_b):
    return set_a & set_b


# 10. Date: True if year is a leap year. Year below 1 raises ValueError.
def is_leap_year(year):
    if year < 1:
        raise ValueError("year must be 1 or more")
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# 11. Type conversion: convert value to int. A bool raises TypeError.
def to_int(value):
    if isinstance(value, bool):
        raise TypeError("bool is not allowed")
    return int(value)


# 12. Math: return a / b. Dividing by zero raises ZeroDivisionError.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


# 13. Math: return base raised to exponent.
def power(base, exponent):
    return base ** exponent


# 14. Math: return the square root of x. Negative x raises ValueError.
def square_root(x):
    if x < 0:
        raise ValueError("cannot take the square root of a negative number")
    return math.sqrt(x)


# 15. Math: return n factorial. Negative n raises ValueError.
def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    return math.prod(range(1, n + 1))


# 16. Math: return the average of a list. Empty list raises ValueError.
def average(numbers):
    if len(numbers) == 0:
        raise ValueError("list is empty")
    return sum(numbers) / len(numbers)
"