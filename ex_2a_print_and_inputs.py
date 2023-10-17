## 1
# print ("Here we go!")

## 1b
# print("I can print")
# print("more than one line.")

## 2a
# print("If you want \n separate lines, you \n can also do it \n like this.")

## 2b
# print("This thing inside quotes is called a \"string\". If you want")
# print("to put quotes inside of quotes, you precede the quotes with a backslash.")
# print("Hello!")

## 2c
# print("""If you put three quote marks, 
# you can easily enter a
# multi-line
# string.""")

## 2d
# """If I wanted to write a long explanation,
# I could write it like this
# instead of using the '#' if I wanted to."""

## 2e
# print('In Python, the single quote can be used instead of the double quote.')
# print("You can put 'single quotes' inside of double quotes, or vice versa, without needing an escape sequence.")
# print('However, if you want single quotes inside of single quotes, you\'ll need to escape them.')

## 3a
# firstn = "Bob"
# lastn = "Smith"
# print(firstn)

## 3b
# firstn = "Bob"
# lastn = "Smith"
# print(lastn)

## 4e
# animal = input("what is a name an animal, then press enter:")
# print(f"the animal you named is {animal}. I think thet would make a nice pet.")

## 5
# firstn = input("Please enter a first name: ")
# lastn = "Smith"
# print(f"Maybe someone is named: {firstn} {lastn}.") 

## 6a
# firstn = input("Please enter a first name: ")
# lastn = input("Please enter your Last name: ")
# print(f"Your name is: {firstn} {lastn}.") 

## 6b
# name = input("what is your first, middle and last name?")
# print(f"your name is {name}")

## 7
# color = input("What is your favorite color? ")
# print(f"{color} is a pretty color")

## 8
# animal2 = input("name an animal, then press enter: ")
# plant = input("type a mane of a plant, then press enter: ")
# print(f"the {animal2} eats {plant} everyday.")

## 9a
# a = "hello"
# b = "goodbye"
# c = a + " " + b
# print(c)

## 9b
# mysentence = "Hello" + "everyone"
# print(mysentence)

## 9c
# mysentence = "hello" + " " +"everyone"
# print(mysentence)

## 10
# a = input("First word? ")
# b = input("second word? ")
# c = a + " " + b
# print(c)

## 11
# a = 5
# b = 3
# c = a + b
# print(c)

## 12
# a = "5"
# b = "3"
# c = a + b
# print(c)

## 13
# print("welcome to the number adder that works well!")
# a = input("What's a number you like?")
# b = input("Can you give me another number you like?")
# c = a + b
# print("I added them. Here's what I got...")
# print(c)

## 14
# print("welcome to the number adder that works well!")
# a = int(input("What's a number you like?"))
# b = int(input("Can you give me another number you like?"))
# c = a + b
# print(c)

## 15
# a = input("What is a number you like? ")
# b = int(input("Can you give me another number you like? "))
# c = a + b
# print(c)

## 16
# favnum = int(input("What is your favorite number? "))
# onemore = favnum + 1
# print(f"One more would be {onemore}")

## 17
# a = int(input("Choose a number: "))
# twomore = int(a + 2)
# print(f"that numbere plus 2 would be {twomore}")

## 18
# a = int(input("Type an integer: "))
# b = int(input("type another integer: "))
# c = int(a * b)
# print(f"The sum of your integers is {c}")

## 19
# a = int(input("What's a number you like?"))
# b = int(input("Can you give me another number you like?"))
# c = a - b
# print(f"the first number minus the second number is {c} ")

## 20
# a = int(input("Choose a number: "))
# halfof = int(a / 2 )
# print(f"half of that number is {halfof}")

## 21
# print("hello"*3)
# a = input("Please enter a string of numbers: ")
# b = (a*3)
# print(b)

## 22a
# print("hello" * "3")

## 22b
# a = input("Please give me a wored: ")
# b = int(input("Please give me a number to multiply it by: "))
# c = a * b
# print(c)

## 23
# num = input("Give me a number. ")
# print("I'm going to try to multiply that number by 5,")
# print("but something strange is going to happen:")
# # print(num*5)

## 24
# questions = float(input("How many questions are on the test? "))
# right = float(input("how many did you get right? "))
# percent = (100 / questions) * right
# print(f"You got {percent:.2f}% right! " )

## 25
# name = input("what is your name? ")
# age = int(input("what is your age? "))
# twomore = int(age + 2)
# print(f"Guess what, {name}, in two years you will be {twomore}")

# # 26
# x = 123
# y = "123"
# print(x*3)
# print(y*3)

## 27
# x = input("Enter a word: ")
# y = int(input("Enter a number: "))
# print(f"The type of x is {type(x)}, which is another way to say 'string'.")
# print(f"The type of y is {type(y)}, which is another way to say 'integer'.")
# print(x*y)

## 28
# mystery = 6
# another = "Hello"
# something = input("Enter a number.")
# whatIsThis = int(input("Enter a number."))
# thisIsSomething = 3.1
# print(f"The type of mystery is {type(mystery)}, which is another way to say 'integer'.")
# print(f"The type of another is {type(another)}, which is another way to say 'string'.")
# print(f"The type of something is {type(something)}, which is another way to say 'string'.")
# print(f"The type of whatIsThis is {type(whatIsThis)}, which is another way to say 'integer'.")
# print(f"The type of thisIsSomething is {type(thisIsSomething)}, which is another way to say 'floating point number'.")

## 28b
# somenum = int(input("Try typing a non-whole number, such as an approximate value for pi. You'll see that it doesn't work: "))
# print(f"you typed {somenum}")

## 28c
# somenum = float(input("Try typing another non-whole number: "))
# print(f"You typed {somenum}")

## 28d
# num = float(input("please enter a number: "))
# num2 = float(input("please enter another number: "))
# sum = (num * num2)
# print(f"The sum of those numbers is {sum}" )

## 28e
# num = float(input("What is pi? "))
# double = num * 2 
# print(f"Twice that munber is {double}")

## 28f
# name = input("what is your name? ")
# age = float(input("what is your age? "))
# twomore = float(age + 2)
# print(f"Guess what, {name}, in two years you will be {twomore}")

# a = float(input("Choose a number: "))
# halfof = float(a / 2 )
# print(f"half of that number is {halfof}")

## 29
# x = "hello"
# y = "goodbye"
# print(x*y)

## 30
# x = "3"
# y = "5"
# print(x*y)
# print("yes")