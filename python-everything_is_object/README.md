# Python - Everything is Object

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

## Introduction

In Python, everything is an object. This fundamental concept shapes how data and functions are handled within the language. Understanding objects, their types, and how they behave—especially in terms of mutability—is crucial for writing effective Python code. This post explores these concepts, providing insights into how Python treats different types of objects and how this affects function arguments.

## ID and Type

Every object in Python has an identity, a type, and a value. The identity of an object is unique and unchangeable, much like an object's address in memory. You can obtain an object's identity using the `id()` function, which returns the object's memory address. The type of an object defines the possible values and operations for that object, such as `int`, `str`, or `list`. You can check an object's type using the `type()` function.

```python
x = 10
print(id(x))  # Output: Memory address of x
print(type(x))  # Output: <class 'int'>

Mutable Objects
Mutable objects can be changed after they are created. Think of them like a to-do list where you can add or remove tasks. Lists and dictionaries in Python are mutable.
