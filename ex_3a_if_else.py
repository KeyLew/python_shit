## 1
# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")

## 1b
# import random
# randomNumber = random.randint(1, 4)
# print(f"Here's a random integer: {randomNumber}")

## 1c
# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 7:
#     print("I think some people say that number is lucky.")

## 1d
# import random
# randomNumber = random.randint(7, 10)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 7:
#     print("I think some people say that number is lucky.")

## 1e
# import random
# randomNumber = random.randint(7, 10)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 7:
#     print("I think some people say that number is lucky.")
# if randomNumber == 10:
#     print("Wow, a two digit number! ")

## 2
# i"mport random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.")

## 3
# import random
# name = random.choice(["bob", "susan", "joe", "anna", "dell"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.")

## 3b
# import random
# name = random.choice(["bob", "susan", "joe", "anna", "dell"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.")
# if name == "dell":
#     print("That's a computer brand. ")

## 3c
# import random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Hello Joe!")
#     print("Your name rhymes with low.")
# print("Have a good day.")

## 4
# import random
# age = random.randint(18, 24)
# print(f"Pretend that you are {age} years old.")
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ")

## 5
# import random
# age = random.randint(18, 24)
# print(f"Pretend that you are {age} years old.")
# if age < 40: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ")

## 6
# thename = input("What is your name? ")
# if thename == "george":
#     print("Are you named after the first US President?")
# else:
#     print("Hello.")

## 7
# name = input("What is your name? ") 
# if name == "joe": 
#     print("Your name rhymes with low.") 
# else: 
#     print(f"Hey {name}.") 
# if name == "Pluto":
#     print("Is it a planet or not?")

## 7b
# name = input("What is your name? ")
# print(f"The lowercase version of that is {name.lower()}.")
# if name.lower() == "joe": 
#     print("Your name rhymes with low.") 
# else: 
#     print(f"Hey {name}.")

## 7bb
# name = input("What is your name? ")
# print(f"The lowercase version of that is {name.lower()}.")
# if name.lower() == "joe": 
#     print("Your name rhymes with low.") 
# else: 
#     print(f"Hey {name}.")
# if name.lower() == "ruby":
#     print("That name is also the name of a gem.")

## 7c
# name = input("What is your name? ")
# if name.lower() != "jay": 
#     print("Your name is not Jay.") 
# print("Greetings.")

## 7d
# name = input("What is your name? ")
# if name.lower() != "bob":
#     print("I don't think I know you. I only know Bob. ")

## 7dd
# num = int(input("select a number: "))
# if num != 5:
#     print("you should have picked 5. ")

## 7e
# name = input("What is your name? ")
# if name == "":
#     print("You didnt type anything")
# else:
#     print(f"Hi {name}")

## 8
# age = 10
# ageNextYear = age + 1
# print(ageNextYear)

## 9
# age = input("How old are you?") 
# ageNextYear = age + 1 
# print(ageNextYear) 

## 10
# age = int(input("How old are you?"))
# ageNextYear = age + 1 
# print(ageNextYear) 

## 11
# age = int(input("How old are you?"))
# agein20 = 20
# if age == 45:
#     print(f"I see you are {age} years old. You will be 65 in {agein20} years")

## 12
# age = input("How old are you?") 
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ")

## 13
# age = int(input("How old are you?") )
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ")

## 14
# age = int(input("How old are you?") )
# if age < 21: 
#     legal = 21 - age
#     print(f"You can't drink alcohol in the US for {legal} years.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ")

## 15
# name = input("What is your name? ")
# if name == "A":
#     print("Your name is just the letter A? That's kinda cool")
# else:
#     print(f"Ok, your name is {name}")

## 16
# birthyear = int(input("Type a year: ")) 
# if birthyear < 2000: 
#     print("You were born before 2000.") 
# elif birthyear == 2000: 
#     print("You were born in 2000.") 
# else: 
#     print("You were born after 2000.") 

## 16b
# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name == "bob":
#     print("That name used to be common, I think.")
# elif name == "sue":
#     print("Your name also refers to a legal action.")
# elif name == "rob":
#     print("Another abbreviation for robert, correct?")
# elif name == "lacy":
#     print("Does the origin of your name relate to clothing with lace?")
# else:
#     print("I don't know you.")
# print("Done.")

## 16c
# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name == "bob":
#     print("That name used to be common, I think.")
# if name == "sue":
#     print("Your name also refers to a legal action.")
# if name == "rob":
#     print("Another abbreviation for robert, correct?")
# if name == "lacy":
#     print("Does the origin of your name relate to clothing with lace?")
# else:
#     print("I don't know you.")
# print("Done.")

## 17
# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name.startswith("z"):
#     print("Your name starts with a Z. That is somewhat uncommon in English.")
# if len(name) < 3:
#     print("Your name is less than 3 characters long.")
# if len(name) > 9:
#     print("Your name is more than 9 characters long.")
# if name == "":
#     print("Your name is empty!")

## 17b
# heightInInches = int(input("Give me a number: "))
# if heightInInches < 0:
#     print("You can't have a negative height!")
# elif heightInInches <= 55:
#     print("That's relatively short.")
# elif heightInInches <= 72:
#     print("That's around average.")
# else:
#     print("That's pretty tall.")

## 17c
# heightInInches = int(input("Give me a number: "))
# if heightInInches < 0:
#     print("You can't have a negative height!")
# if heightInInches <= 55:
#     print("That's relatively short.")
# if heightInInches <= 72:
#     print("That's around average.")
# else:
#     print("That's pretty tall.")

## 18
# fries = int(input("how many french fries do you want? "))
# if fries <= 10:
#     print("you need to eat more")
# elif fries < 25:
#     print("that sounds great! ")
# else:
#     print ("you eat too much. 😊")

## 19
# x = int(input("Enter a number: ")) 
# if x < 20: 
#     print("A") 
#     print("B") 
# print("C") 

## 20
# x = int(input("Enter a number: ")) 
# if x < 20: 
#     print("A") 
#     print("B") 
# else:
#     print("C") 

## 20b
# x = int(input("Enter a number: ")) 
# if x < 20: 
#     print("A") 
# else: 
#     print("C") 
# print("goodbye")

## 20c
# x = int(input("Type a number: "))
# if x > 3 and x < 10:
#     print("x is more than 3 and less than 10.")

## 20d
# x = int(input("Type a number: "))
# if 3 < x < 10:
#     print("x is more than 3 and less than 10.")

## 21
# num = int(input("type a number: "))
# if num > 50:
#     name = input("what is your name? ")
#     print(f"hello {name}")
# else:
#     input("how did you pick that number?")
#     print("I see")
# print("Have a good day")

## 22
# num = int(input("type a number: "))
# x2 = num * 2
# print(f"that number doubled is {x2}")
# if num > 25:
#     print("thats a juicy number")
# else:
#     print("those are rookie numbers")

## 22b
# firstcost = float(input("How much is the first thing you bought? "))
# secondcost = float(input("How much is the second thing you bought? "))
# total = firstcost + secondcost
# discounted = total * 0.9
# print(f"The total cost would be {total}.")
# print("However, we're doing a special sale today, so you get a 10% discount.")
# print(f"That means you actually pay {discounted}")

## 23
# x = float(input("Type a number between 0 and 1, for example, 0.3, 0.25, etc... "))
# print(f"One more would be {x + 1}.")

## 23b
# cost = float(input("How much does that single item cost? "))
# howmany = float(input("how many did you buy?"))
# total = cost * howmany
# print(f" the total price woul be {total}. ")

## 24
# cost = float(input("How much does that single item cost? "))
# howmany = float(input("how many did you buy?"))
# total = cost * howmany
# discounted = cost * 20 * 0.9
# print(f"The price woul be {total}. ")
# print(f"But if you buy 20 with the discount you would pay {discounted}")

## 25
# num = float(input("Type a non whole number: "))
# print(num)

## 26
# tempC = float(input("what is the temperature in celsius? "))
# tempF = tempC * (9/5) + 32
# print(f"that temperature is {tempF:.0f} in Fahrenheit")

## 27
# tempF = float(input("what is the temperature in Fahrenheit? "))
# tempC = float((tempF - 32) * (5/9))
# print(f"that temp in celsius is {tempC:.0f}")

## 28
# temp_and_unit = input("give me a degree to convert. Examples: 35 F, 82 C... ")
# temp_str, unit = temp_and_unit.split(" ")
# temp = float(temp_str)
# if unit == "F":
#     tempC = float((temp - 32) * (5/9))
#     print(f"in celsius that would be {tempC:.0f} C")
# elif unit == "C":
#     tempF = temp * (9/5) + 32
#     print (f"in fahrenheit that would be {tempF:.0f} F")
# elif unit != "F" and unit != "C":
#     print("I dont understand.")

## 29
# num = float(input("Type a number:"))
# rem = num % 5 
# print(f"the remainder of your number divided by 5 is {rem}.")
# if rem == 0:
#     div = num / 5
#     print(f"your number divided by 5 is {div}")

## 30
# color = input("What color is water? ")
# if color == "blue" or color == "transparent":
#     print("Yes, I agree.")
# else:
#     print("I'm not sure about that.")

## 31
# color = input("What color is water? ")
# if color in ["blue", "transparent"]:
#     print("Yes, I agree.")
# else:
#     print("I'm not sure about that.")

## 32
# color = input("What color is water? ")
# if color != "blue" and color != "transparent":
#     print("I'm not sure about that.")
# else:
#     print("Yes, I agree.")

## 33
# color = input("What color is water? ")
# if color not in ["blue", "transparent"]:
#     print("I'm not sure about that.")
# else:
#     print("Yes, I agree.")

## 34
# sound = input("what sound does a dog make? ")
# if sound.lower() in ["woof", "bark", "ruff"]:
#     print("thats correct")
# else:
#     print("not quite")