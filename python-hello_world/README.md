1. How to use the Python interpreter
You can open the interpreter by running python3 in your terminal.

2. How to print text and variables using print()
Use print() to display information:

3. How to use strings
Strings are sequences of characters, enclosed in quotes:

python
Copier
Modifier
text = "Python is fun"
print(text.lower())    # "python is fun"
print(text.upper())    # "PYTHON IS FUN"
print(len(text))       # 13 (number of characters)


4. What are indexing and slicing in Python
Indexing accesses a single character:

python
Copier
Modifier
word = "Python"
print(word[0])    # P (first character)
print(word[-1])   # n (last character)
Slicing accesses a range of characters:

python
Copier
Modifier
print(word[0:2])   # Py (from index 0 to 1)
print(word[2:])    # thon (from index 2 to end)
print(word[:4])    # Pyth (start to index 3)


5. What is the official Python coding style and how to check your code with pycodestyle
Python follows PEP 8, the official style guide:
➤ 4 spaces per indent, clear names, blank lines between functions, etc.

To check your code:

bash
Copier
Modifier
$ pip install pycodestyle
$ pycodestyle your_script.py
It will show style issues like missing spaces, long lines, or indentation problems.
