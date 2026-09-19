# Python Learning Roadmap

This guide covers the core Python concepts you listed and helps you move from beginner to professional Python development.

---

## 1) Fundamentals

### Variables

Variables store data in memory so you can reuse it later.

```python
name = "Alice"
age = 25
is_student = True
```

Key ideas:
- Python is dynamically typed, so you do not need to declare the type explicitly.
- Variable names should be descriptive and follow snake_case.
- Python uses references to objects, not fixed memory locations like some low-level languages.

Example:

```python
x = 10
x = x + 5
print(x)  # 15
```

---

### Functions

Functions let you group reusable logic.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Sam"))
```

Important concepts:
- Parameters: values passed into a function
- Return value: value sent back from a function
- Default arguments

```python
def welcome(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(welcome("Aisha"))
print(welcome("Aisha", "Hi"))
```

---

### Classes

Classes define blueprints for objects.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Bruno", 3)
print(my_dog.bark())
```

Learn:
- `__init__` is the constructor
- `self` refers to the current instance
- objects encapsulate state and behavior

---

### Modules

A module is a Python file containing code you can reuse.

Example:

```python
# math_tools.py

def add(a, b):
    return a + b
```

Then import it:

```python
import math_tools

print(math_tools.add(3, 4))
```

Modules help organize code into smaller, maintainable files.

---

### Packages

A package is a folder containing modules and usually an `__init__.py` file (in older Python) or a namespace package in modern Python.

Example structure:

```text
project/
    app/
        __init__.py
        utils.py
        math_tools.py
```

Importing:

```python
from app.math_tools import add
print(add(2, 5))
```

Packages are used to structure large applications.

---

### Exceptions

Exceptions are errors that occur during runtime.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("This always runs.")
```

Common exception types:
- `ValueError`
- `TypeError`
- `FileNotFoundError`
- `IndexError`
- `KeyError`

Best practice:
- Catch specific exceptions rather than broad `except Exception` when possible.

---

### Decorators

Decorators modify or enhance functions without changing their code directly.

```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello world"

print(greet())
```

Use cases:
- logging
- authentication checks
- caching
- timing functions

---

### Generators

Generators produce values one at a time instead of storing everything in memory.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(3):
    print(value)
```

Key points:
- `yield` pauses and resumes iteration.
- Great for large datasets and streaming data.

---

### Comprehensions

Comprehensions provide a compact way to create lists, sets, and dictionaries.

List comprehension:

```python
squares = [x * x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

Dictionary comprehension:

```python
square_map = {x: x * x for x in range(1, 4)}
print(square_map)
```

Set comprehension:

```python
even_numbers = {x for x in range(10) if x % 2 == 0}
```

---

### Context Managers

Context managers handle setup and cleanup automatically.

```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
```

This ensures the file is closed after the block ends.

You can also create custom context managers using `contextlib`:

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Opening resource")
    yield
    print("Closing resource")

with managed_resource():
    print("Using resource")
```

---

## 2) Professional Python

### Virtual Environments

A virtual environment isolates project dependencies.

Why use them?
- avoid package conflicts
- keep project dependencies controlled
- make projects reproducible

Create one:

```bash
python -m venv .venv
```

Activate it:

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

---

### pip

`pip` installs Python packages.

```bash
pip install requests
pip install --upgrade pip
```

Install from requirements:

```bash
pip install -r requirements.txt
```

List installed packages:

```bash
pip list
```

---

### pyproject.toml

`pyproject.toml` is the modern Python project configuration file.

It is used for:
- project metadata
- dependencies
- build tools
- packaging
- test configuration

Example:

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "A sample Python project"
requires-python = ">=3.10"

dependencies = [
  "requests>=2.0.0"
]
```

Modern tools like `pip`, `poetry`, and `setuptools` often use this file.

---

### Type Hints

Type hints help make code clearer and safer.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
```

You can also type variables:

```python
name: str = "Alice"
count: int = 5
```

Benefits:
- better editor support
- easier debugging
- clearer APIs
- better collaboration

---

### Dataclasses

Dataclasses reduce boilerplate when creating classes that mainly store data.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Alice", 30)
print(p1)
print(p1.name)
```

This automatically creates methods like `__init__` and `__repr__`.

---

### Logging

Logging is used for tracking application events and debugging.

```python
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Something went wrong")
```

Common log levels:
- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

---

### Configuration

Configuration keeps values like URLs, file paths, and feature flags out of hardcoded logic.

Example:

```python
DB_HOST = "localhost"
DB_PORT = 5432
```

Better approach for larger apps:
- use config files
- use environment variables
- use `.env` files in local development

---

### Environment Variables

Environment variables are key-value settings stored outside the codebase.

```python
import os

api_key = os.getenv("API_KEY")
print(api_key)
```

Set a variable in terminal:

On Windows:

```bash
set API_KEY=abc123
```

On macOS/Linux:

```bash
export API_KEY=abc123
```

Use packages like `python-dotenv` to load values from a `.env` file:

```python
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("API_KEY"))
```

Why this matters:
- secrets stay out of source code
- easier deployment across environments
- safer for production systems

---

## 3) Suggested Learning Order

1. Variables and basic data types
2. Functions and control flow
3. Lists, dictionaries, tuples, sets
4. Classes and objects
5. Modules and packages
6. Exceptions and error handling
7. File handling and context managers
8. Decorators and generators
9. Virtual environments and `pip`
10. Type hints and dataclasses
11. Logging and configuration
12. Environment variables and deployment-ready patterns

---

## 4) Practice Exercises

### Exercise 1: Function and return value

```python
def multiply(a, b):
    return a * b

print(multiply(4, 5))
```

### Exercise 2: Class with method

```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))
```

### Exercise 3: Exception handling

```python
try:
    number = int("abc")
except ValueError:
    print("This is not a valid integer.")
```

### Exercise 4: List comprehension

```python
nums = [1, 2, 3, 4, 5]
print([n * 2 for n in nums])
```

---

## 5) Beginner Tips

- Write simple code before complex code.
- Practice reading errors carefully.
- Use descriptive names for variables and functions.
- Break problems into small steps.
- Learn by building small projects such as:
  - calculator
  - todo app
  - file organizer
  - web scraper
  - API client

---

## 6) Final Advice

Python is best learned by building. Start with small programs, then gradually add structure, testing, packaging, and professional practices. Once you understand variables, functions, classes, and modules, you can move confidently into virtual environments, package management, and production-style code.

If you want, the next step can be:
- a full Python beginner roadmap with daily practice tasks
- a project-based learning plan
- a list of interview questions for Python fundamentals
- a set of beginner exercises with solutions
