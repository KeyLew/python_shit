## 1
# f = open("something_very_unique_file.txt", "w")
# f.write("Here are some words.\n")
# f.write("More words.\n")
# f.close()

## 2
# f = open("my_thoughts.txt", "w")
# f.write("why\n am\n i\n going\n to\n do\n this\n today\n it\n sucks\n hard.\n")
# f.close()

## 3
# name = input("What is your name? ")
# age = int(input("How old are you? "))
# f = open("person_info.txt", "w")
# f.write(f"{name} is {age} years old.\n")
# f.close()

## 4 
# f = open("something_very_unique_file.txt", "r")
# contents = f.read()
# print(contents)
# f.close()

## 5 
# f = open("something_very_unique_file.txt")
# contents = f.read()
# print(contents)
# f.close()

## 6 
# f = open("yay_new_file.txt", "w")
# f.write("Here are some words for you.\n")
# f.close()
# f = open("yay_new_file.txt")
# contents = f.read()
# print(contents)
# f.close()
# f = open("yay_new_file.txt", "w")
# f.write("I overwrote those words.\n")
# f.close()
# f = open("yay_new_file.txt")
# contents = f.read()
# print(contents)
# f.close()

## 7
# f = open("yay_new_file.txt", "x")
# f.write("Words to put in the file\n")
# f.close()

## 8
# f = open("yay_new_file.txt", "a")
# f.write("This will write at the end of an existing file.\n")
# f.close()

## 9a
# import random

# f = open("your_filename_here.txt", "w")
# for unusedCounter in range(10000000):
#     rnum = random.random() * 10
#     f.write(f"{rnum}\n")
# f.close()

## 9b
# f = open("your_filename_here.txt", "r")
# for line in f:
#     if line.startswith("3.14"):
#         print(line)
# f.close()

## 9c
# f = open("your_filename_here.txt", "r")
# contents = f.read()
# lines = contents.splitlines()
# for line in lines:
#     if line.startswith("3.14"):
#         print(line)
# f.close()

## 10
# import os
# from pathlib import Path

# rootdir = Path("many_files_are_in_here")
# os.mkdir(rootdir)
# filehandlelist = []
# for count in range(0, 500000):
#     filename = rootdir / f"file_num_{count}.txt"
#     f = open(filename, "w")
#     filehandlelist.append(f)