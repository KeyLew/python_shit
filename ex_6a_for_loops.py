## 1
# colors = ["red", "orange", "yellow"]
# for color in colors:
#     print("Here is a color that I know:")
#     print(color)
#     print()

## 2
# colors = ["red", "orange", "yellow"]
# color = colors[0]
# print("Here is a color that I know:")
# print(color)
# print()
# color = colors[1]
# print("Here is a color that I know:")
# print(color)
# print()
# color = colors[2]
# print("Here is a color that I know:")
# print(color)
# print()

## 3
# names = ["Sam", "Lisa", "Micah", "Dave"]
# for name in names:
#     print(f"Hello {name}. Welcome to the Python course.")

## 4
# names = ["Sam", "Lisa", "Micah", "Dave"]
# for name in names:
#     print(f"Have a good day,{name}. I hope you enjoyed experimenting with python.")

## 5
# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"In two years, that person will be {age + 2} years old.")
#     print()

## 6
# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"5 years ago, that person was {age - 5} years old.")
#     print()

## 7
# ages = [21, 40, 32, 10, 8, 3]
# for age in ages:
#     print(f"Half of {age} is {age / 2}.")
#     print()

## 8
# for num in range(1,5):
#     print(num)

## 9
# for num in range(1,7):
#     print(num)

## 10
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")

## 11
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")
#     if temp > 90:
#         print("That's hot.")

## 12
# temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
# for temp in temps_in_F:
#     print("The temperature was {temp}")
#     if temp > 32:
#         print("That's not freezing.")
#     else:
#         print("Now that's freezing")

## 13
# x = input("Say a word: ")
# if x.endswith("s"):
#     print("That ends with an 's', so it might be plural.")
# print("That's all I have to say.")

## 14
# x = input("Say a word: ")
# if x.endswith("day"):
#     print("I think that's a day of the week.")
# print("That's all I have to say.")

## 15
# fruits = ["strawberry", "mango", "raspberry", "blueberry", "grape", "melon"]
# berryCount = 0
# for fr in fruits:
#     if fr.endswith("berry"):
#         berryCount += 1
# print("I've finished counting the fruits.")
# print(f"There were {berryCount} that ended with berry.")

## 16
# fruits = ["strawberry", "mango", "raspberry", "blueberry", "grape", "melon"]
# mCount = 0
# for fr in fruits:
#     if fr.startswith("m"):
#         mCount += 1
# print("I've finished counting the fruits.")
# print(f"There were {mCount} that started with m.")

## 17
# temps_in_F = [90, 30, 47, 82, 68, 100, 25, 40]
# meltcount = 0
# for temp in temps_in_F:
#     if temp > 32:
#         meltcount += 1
# print("I have calculated the temperatures.")
# print(f"there were {meltcount} temperatures above freezing.")

## 18
# temps_in_F = [90, 30, 47, 82, 68, 100, 25, 40]
# meltcount = 0
# freezecount = 0
# for temp in temps_in_F:
#     if temp > 32:
#         meltcount += 1
# for temp in temps_in_F:
#     if temp < 33:
#         freezecount += 1
# print("I have calculated the temperatures.")
# print(f"there were {meltcount} temperatures above freezing and {freezecount} below.")
## 19
# instructors = [
#     ["Maria", 38, 7],
#     ["Walton", 47, 22],
#     ["Martin", 52, 18],
#     ["Joel", 28, 3],
#     ["Tate", 67, 5]
# ]

## 20
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for instructor in instructors:
#     name, age, yearsExp = instructor
#     print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

## 21
# name, color = ["Bob", "Green"]
# print(f"{name} likes the color {color}")

## 22
# personinfo = ["Bob", "Green"]
# name, color = personinfo
# print(f"{name} likes the color {color}")

## 23
# personinfo = ["Bob", "Green", 20]
# name, color, age = personinfo   #   <-- Only change this line.
# print(f"{name} is {age} years old, and likes the color {color}")

## 24
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")

# instructor = instructors[0]
# name, age, yearsExp = instructor
# print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

# instructor = instructors[1]
# name, age, yearsExp = instructor
# print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

# instructor = instructors[2]
# name, age, yearsExp = instructor
# print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

# instructor = instructors[3]
# name, age, yearsExp = instructor
# print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

# instructor = instructors[4]
# name, age, yearsExp = instructor
# print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

## 25
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for instructor in instructors:
#     name, age, yearsExp = instructor
#     print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

## 26
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

## 27
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} is {age} years old and started working here at the age of {age - yearsExp}.")

## 28
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} has been working for {yearsExp} years, and will recieve a ${yearsExp * 10} bonus this year.")

## 29
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# bonus = float(input("What is the bonus per year of experience? "))
# print("Here is my instructor data:")
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} has been working for {yearsExp} years, and will receive a ${yearsExp * bonus:.2f} bonus this year.")

## 30
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# totalYearsExp = 0
# print("Here is my instructor data:")
# for name, age, yearsExp in instructors:
#       totalYearsExp += yearsExp
# print(f"The total amount of work experience for this team is {totalYearsExp}")

## 31
# runners = [
#     ["James", 5, 60],
#     ["Tom", 1, 7],
#     ["Steve", 2, 22],
#     ["Carson", 2, 12]]
# for name, miles, minutes in runners:
#     print(f"{name} ran {miles} miles in {minutes} minutes. ")
#     print(f"That means {name} took an average of {minutes / miles} minutes to run each mile")

## 32
# phrase = "Hello world"
# for letter in phrase:
#     print(f"The letter is {letter}")

## 33
# phrase = input("What is your favorite phrase? ")
# for letter in phrase:
#     print(f"The letter is {letter}")

## 34
# phrase = input("What is your favorite phrase? ")
# for letter in phrase:
#     print(f"The letter is {letter}!")

## 35
# for num in range(1,6):
#     print(num ** 2)

## 36
# highnum = int(input("Please choose the highest number you want squared: "))
# for num in range(1, highnum + 1):
#     print(num ** 2)

## 37
# for num in range(1, 13):
#     print(f"{num} divided by 4 would have a remainder of {num % 4}")

## 38
# print("Hello"*3)

## 39
# howmany = int(input("How many times should the word 'Hello ' print? "))
# print("Hello "*howmany)

## 40
# howmany = int(input("How many rows would you like? "))
# for i in range(0, howmany):
#                print("AAAAA")

## 41
# howmany = int(input("How many rows would you like? "))
# for num in range(1, howmany):
#                print(f"{num} A")

## 42
# howmany = int(input("How many rows would you like? "))
# for num in range(1, howmany):
#                print(f"{num} times A is {'A'*num} ")

## 43
# howmany = int(input("How many rows would you like? "))
# for num in range(1, howmany):
#                print(f"{'A'*num} ")

## 44
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# base_pay = 35000
# pay_adjustment = 1000
# for  name, age, yearsExp in instructors:
#     pay_level = yearsExp // 5
#     salary = base_pay + (pay_adjustment * pay_level)
#     print(f"{name}: {yearsExp} years of experience, ${salary} per year.")

## 45
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# # print("Here is my instructor data:")
# base_pay = float(input("What should the base pay for instuctors be? "))
# pay_adjustment = float(input("And what should their pay adjustment be per 5 years experience? " ))
# for  name, age, yearsExp in instructors:
#     pay_level = yearsExp // 5
#     salary = base_pay + (pay_adjustment * pay_level)
#     print(f"{name}: {yearsExp} years of experience, ${salary} per year.")

## 46
# names = ["Sam", "Lisa", "Micah", "Dave"]
# for indx, elem in enumerate(names):
#     print(f"The index is {indx} and the element is {elem}")

## 47
# names = ["H", "e", "l", "l", "o",  " ", "w", "o", "r", "l", "d"]
# for indx, elem in enumerate(names):
#     print(f"{indx}: {elem}!")

##48
# freqs = [2403.6, 101.3, 90.1, 5.2, 2410.2, 3.7]
# for num in freqs:
#     if num >2.3 and num < 6:
#         print(f"{num} is within the wifi frequency range.")
#     elif num > 87 and num < 108.1:
#         print(f"{num} is within the FM frequency range.")
#     else:
#         print(f"{num} is not in either wifi or FM frequency ranges")

## 49
freqs = [2403.6, 101.3, 90.1, 5.2, 2410.2, 3.7]
wificount = 0
FMcount = 0
neithercount = 0
for num in freqs:
    if num >2.3 and num < 6:
        wificount += 1
        print(f"{num} is within the wifi frequency range.")        
    elif num > 87 and num < 108.1:
        FMcount += 1
        print(f"{num} is within the FM frequency range.")        
    else:
        neithercount += 1
        print(f"{num} is not in either wifi or FM frequency ranges.")        
print(f"There are {wificount} frequencies in the wifi range.")
print(f"There are {FMcount} frequencies in the FM range.")
print(f"There {neithercount} frequencies out of range.")