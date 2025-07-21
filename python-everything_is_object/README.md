Python - Everything is Object
Introduction
In Python, everything is an object. This fundamental concept shapes how data and functions are handled within the language. Understanding objects, their types, and how they behave—especially in terms of mutability—is crucial for writing effective Python code. This post explores these concepts, providing insights into how Python treats different types of objects and how this affects function arguments.

ID and Type
Every object in Python has an identity, a type, and a value. The identity of an object is unique and unchangeable, much like an object's address in memory. You can obtain an object's identity using the id() function, which returns the object's memory address. The type of an object defines the possible values and operations for that object, such as int, str, or list. You can check an object's type using the type() function.

Copier
x = 10
print(id(x))  # Output: Memory address of x
print(type(x))  # Output: <class 'int'>
Mutable Objects
Mutable objects are those that can be changed after they are created. Lists, dictionaries, and sets are common examples of mutable objects in Python. When you modify a mutable object, you are changing the object itself, not creating a new one.

Copier
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
Immutable Objects
Immutable objects, on the other hand, cannot be changed after they are created. Integers, floats, strings, and tuples are examples of immutable objects. Any modification to an immutable object results in the creation of a new object.

Copier
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This would raise an error
new_tuple = my_tuple + (4,)
print(new_tuple)  # Output: (1, 2, 3, 4)
Why Does It Matter and How Differently Does Python Treat Mutable and Immutable Objects
The distinction between mutable and immutable objects is crucial because it affects how objects are passed and modified within functions. Mutable objects can be modified in place, which means changes made to them inside a function will be reflected outside the function. Immutable objects, however, cannot be changed in place, so any modifications inside a function result in a new object, leaving the original unchanged.

Copier
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

def modify_tuple(tup):
    tup += (4,)

my_tuple = (1, 2, 3)
modify_tuple(my_tuple)
print(my_tuple)  # Output: (1, 2, 3)
How Arguments Are Passed to Functions and What Does That Imply for Mutable and Immutable Objects
In Python, arguments are passed by assignment. This means that the reference to the object is passed to the function. For mutable objects, this allows the function to modify the original object. For immutable objects, since they cannot be modified, any changes result in a new object being created, and the original object remains unchanged.

Copier
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # Output: 1

def append_to_list(lst):
    lst.append(4)

b = [1, 2, 3]
append_to_list(b)
print(b)  # Output: [1, 2, 3, 4]
