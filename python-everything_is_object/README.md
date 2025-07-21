# Python - Everything is Object

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

```python

## Introduction

In Python, everything is an object. This fundamental concept shapes how data and functions are handled within the language. Understanding objects, their types, and how they behave—especially in terms of mutability—is crucial for writing effective Python code. This post explores these concepts, providing insights into how Python treats different types of objects and how this affects function arguments.

## ID and Type

Every object in Python has an identity, a type, and a value. The identity of an object is unique and unchangeable, much like an object's address in memory. You can obtain an object's identity using the `id()` function, which returns the object's memory address. The type of an object defines the possible values and operations for that object, such as `int`, `str`, or `list`. You can check an object's type using the `type()` function.

x = 10
print(id(x))  # Output: Memory address of x
print(type(x))  # Output: <class 'int'>

Mutable Objects
Mutable objects can be changed after they are created. Think of them like a to-do list where you can add or remove tasks. Lists and dictionaries in Python are mutable.
my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the list
print(my_list)  # Output: [1, 2, 3, 4]

Immutable Objects
Immutable objects cannot be changed after they are created, like a photo that can't be altered once taken. Numbers, strings, and tuples in Python are immutable.
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This would cause an error
new_tuple = my_tuple + (4,)  # Creates a new tuple
print(new_tuple)  # Output: (1, 2, 3, 4)

Why It Matters
Knowing whether an object is mutable or immutable is important because it affects how you can modify it. Mutable objects can be changed directly, while immutable objects require creating a new object for any changes.
def change_list(lst):
    lst.append(4)  # Changes the original list

my_list = [1, 2, 3]
change_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

def change_tuple(tup):
    tup += (4,)  # Creates a new tuple

my_tuple = (1, 2, 3)
change_tuple(my_tuple)
print(my_tuple)  # Output: (1, 2, 3)
