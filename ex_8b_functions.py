## 1
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# sayWelcome()
# sayWelcome()

## 2
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# sayWelcome()
# sayWelcome()
# sayWelcome()

## 3
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

## 4
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# def sayBye():
#     print("Goodbye, have a good day!")

# sayBye()
# sayWelcome()

## 5
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()
# def sayBye():
#     print("Goodbye, have a good day!")
# sayWelcome()
# sayBye()

## 6
# def saycoolstuff():
#     print("hakuna matata! ")
#     print()
#     print("It means no worries. ")
# saycoolstuff()

## 7
# def sayWelcome():
#     print("Welcome to the Python class")
#     print("We hope you enjoy it.")
#     print()

# print("This line of code is not well positioned -- it comes between two function definitions.")

# def sayBye():
#     print("Goodbye, have a good day!")

# print("This line of code is well positioned, because it comes after the function definitions.")
# sayWelcome()
# sayBye()

## 8
# def sayHiTo(name):
#     print(f"Hello {name}. Welcome to the Python course.")

# sayHiTo("Bob")
# sayHiTo("Sue")
# sayHiTo("Tom")

## 8b
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# tellAbout("Bob", "cat")
# tellAbout("Sue", "dog")
# tellAbout("camel", "Tom")

## 9
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# tellAbout("Bob", "cat")
# tellAbout("Sue", "dog")
# tellAbout("Tom", "camel")

## 10
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# tellAbout("Bob")

## 11
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# tellAbout("Bob", "monkey")

## 12
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# na = "Bob"
# ani = "cat"
# tellAbout(na, ani)

## 13
# def tellAbout(name, animal):
#     print(f"Hello {name}. I've heard you have a pet {animal}.")

# na = input("What is your name? ")
# ani = input("Name an animal: ")
# tellAbout(na, ani)

## 14
# def sayLengthOfEach(names):
#     for name in names:
#         print(f"The length of {name} is {len(name)}")

# sayLengthOfEach(["Bob", "Joseph", "Susan"])

## 15
# def convertHoursToMinutes(hours):
#     return hours * 60

# h = int(input("Give a number of hours, and I'll convert it to minutes."))
# m = convertHoursToMinutes(h)
# print(f"That would be {m} minutes.")