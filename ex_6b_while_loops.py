## 1
# count = 10
# print(f"count is {count}.")
# count += 1
# print(f"I changed count. Now, it's {count}.")
# count -= 2
# print(f"I changed it again. Now, it's {count}.")

## 2
# count = int(input("Please select a number: "))
# print(f"count is {count}.")
# count += 1
# print(f"I changed count. Now, it's {count}.")
# count -= 2
# print(f"I changed it again. Now, it's {count}.")

## 3
# count = 3
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)
# count -= 1
# print("Reached zero. Proof:")
# print(count)

## 4
# count = 3
# while count > 0:
#     print(count)
#     count -= 1
# print("Reached zero. Proof:")
# print(count)

## 5
# count = int(input("Please select a number: "))
# while count > 0:
#     print(count)
#     count -= 1
# print("Reached zero. Proof:")
# print(count)

## 6
# count = 3
# while count > 0:
#     print(f"Launch in {count}")
#     count -= 1
# print("Liftoff!")

## 7
# import time
# print("Start...")
# time.sleep(1)
# print("Done.")

## 8
# delay = int(input("select a time of delay: "))
# import time
# print("Start...")
# time.sleep(delay)
# print("Done.")

## 9
# count = 3
# import time
# print("Start...")
# time.sleep(1)
# while count > 0:    
#     print(f"Launch in {count}")
#     time.sleep(1)
#     count -= 1
# print("Liftoff!")

## 10
# keepGoing = "yes"
# while keepGoing == "yes":
#     print("Since the variable keepGoing is still 'yes', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")

## 11
# keepGoing = "yes"
# while keepGoing == "yes" or keepGoing == "y":
#     print("Since the variable keepGoing is still 'yes', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")

## 12
# keepGoing = "yes"
# while keepGoing == "yes" or keepGoing == "y":
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

## 13
# keepGoing = "yes"
# while keepGoing in ["yes", "y"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

## 14
# keepGoing = "yes"
# while keepGoing not in ["no", "no thanks"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")   

## 15
# keepGoing = "yes"
# while keepGoing in ["yes", "y", "hey", "woo", ]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")   

## 16
# keepGoing = "yes"
# while keepGoing not in ["no"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")   

## 17
# keepGoing = "yes"
# while keepGoing.lower() not in ["done", "quit", "exit"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.") 

## 18
# count = 0
# print("welcome to my counter")
# math = (input("Would you like to add one, subtract one, or quit?"))
# while math in ["add"]:
#     count += 1
#     print(f"the counter is currently at {count}")
#     math = (input("Would you like to add one, subtract one, or quit?"))
# while math in ["subtract"]:
#         count-= 1
#         print(f" the counter is currently at {count}")
#         math = (input("Would you like to add one, subtract one, or quit?"))
# print("Thanks for using my counter program!")

## 19
# print("Welcome to the word guesser!")
# secretWord = "water"
# guess = ""
# while guess != secretWord:
#     guess = input("What is your guess? ")
# print("You got it!")

## 20
# print("Welcome to the word guesser!")
# secretWord = "water"
# guess = ""
# while guess != secretWord:
#     guess = input("What is your guess? ")
#     print("let me check")
# print("You got it!")

## 21
# print ("welcome to the word guesser!")
# secretWord = "water"
# guess = input("What is your guess? ")
# while guess != secretWord:
#     print("No, try again.")
#     guess = input("What is your guess? ")
# print("You got it!")

## 22
# print("Welcome to the number doubler.")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     print(f"Double your num is {num * 2}.")
# print("Exiting.")

## 23
# print("Welcome to the number squarer.")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     print(f"Double your num is {num ** 2}.")
# print("Exiting.")

## 24
# print("Welcome to the number doubler.")
# num = float(input("select a number: "))
# while num != -1:
#     print(f"Double your num is {num * 2}.")
#     num = int(input("Type a number, or type -1 to quit: "))    
# print("Exiting.")

## 25
# animal = input("Name an animal, or say 'moose' to exit: ")
# while animal != "moose":
#     print(f"The {animal} says 'meow'.")
#     animal = input("Name an animal, or say 'moose' to exit: ")
# print("Moose out.")

## 26
# animal = input("Name an animal, or say 'moose' to exit: ")
# noise = input("What sound does that animal make? ")
# while animal != "moose":
#     print(f"The {animal} says '{noise}'.")
#     animal = input("Name an animal, or say 'moose' to exit: ")
# print("Moose out.")

## 27
# animal = input("Name an animal, or say 'moose' to exit: ")
# noise = input("What sound does that animal make? ")
# while animal != "moose" and noise != "meow":
#     print(f"The {animal} says '{noise}'.")
#     animal = input("Name an animal, or say 'moose' to exit: ")
#     noise = input("What sound does that animal make? ")
# print("Moose out.")

## 28
# import random
# import time

# print("This is a Duck, Duck, Goose Simulator. Have fun!!!!!")
# choices = ["Goose",
#               "Duck",
#               "Duck",
#               "Duck"]
# one_choice = random.choice(choices)
# while one_choice != "Goose":
#     print(f"{one_choice}...")
#     time.sleep(1)
#     one_choice = random.choice(choices)
# print("Goose!")  

## 29
# import random
# import time
# replies = ["Not yet, try again.", "I bet you'll get it, keep trying!", "That's not it.", "I appreciate your patience, but you haven't guessed it yet."]
# print("Welcome to the word guesser!")
# secretWord = "keys"
# guess = input("guess the secret word: ")
# while guess.lower() != secretWord:
#     one_choice = random.choice(replies)
#     print(one_choice)
#     guess = input("guess the secret word: ")
#     print("let me check...")
#     time.sleep(2)
# print("You got it!")

## 29b
# names_starting_with_c = []
# name = input("Enter a name, or q to quit: ")
# while name != "q":
#       if name.lower().startswith("c") :
#           names_starting_with_c.append(name)
#       name = input("Enter a name, or q to quit: ")
# print(f"These names start with the letter c: {names_starting_with_c}")

## 30
# import random
# somenum = random.randint(20, 101)
# guess = float(input(f"If you divided {somenum} by 12, what would be the remainder? "))
# answer = somenum % 12
# while guess != answer:
#     guess = float(input("guess:"))
# print("You got it!")

## 31
# print("This is a grade tracking helper.")
# f = open("physics_grades.csv", "w")
# f.write("Student_Name,Student_Grade\n")
# f.close()
# name = input("What is the student name? (Press enter with no name to exit.) ")
# questions = int(input("What is the total number of questions for this assignment? "))
# while name != "":
#     right = int(input("How many questions did that student answer correctly? "))
#     percent = 100 / questions * right
#     print(f"{percent:.2f}%")
#     f = open("physics_grades.csv", "a")
#     f.write(f"{name}, {percent:.2f}%\n")
#     f.close()
#     name = input("What is the student name? (Press enter with no name to exit.) ") 
# print("Exiting... ")

## 32
# x = 0
# while 2 + 2 == 4:
#     print(x)
#     x += 1
# print("Done")

## 33
# while 2 + 2 == 5:
#     print("Hi")
# print("Done")

## 34
# while 3 > 2:
#     print("Hi")
# print("Done")

## 35
# while 2 == 2:
#     print("Hi")
# print("Done")

## 36
# while True == True:
#     print("Hi")
# print("Done")

## 37
# while True:
#     print("Hi")
# print("Done")

## 38
# while 1 == 1:
#     color = input("What is your favorite color? ")
#     print(f"Ok, {color} is a nice color.")

## 39
# print("Welcome to yet another version of the number doubler.")
# while True:
#     num = int(input("Type a number, or type -1 to quit: "))
#     if num == -1:
#         break
#     print(f"Double your num is {num * 2}.")