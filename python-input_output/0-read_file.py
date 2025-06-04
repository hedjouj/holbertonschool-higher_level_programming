#!/usr/bin/python3
"""a fonction that read a file using with"""

def read_file(filename=""):
    """read a file"""

    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu)
