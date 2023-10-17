# thelist = ["water", "chair", "mug", "mouse"]
# #             0        1       2       3 
# print(thelist[0])
# print(thelist[2])

## 1
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[1])

## 2
# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[3])

## 3
# thelist = ["water", "chair", "mug", "mouse"]
#            -4       -3      -2      -1
# print(thelist[-1])
# print(thelist[-2])

## 4
# foods = ["Potatoes", "Beef", "Broccoli", "Lemons", "Grapes"]
# print(foods[1])
# print(foods[-1])

## 5
# foods = ["Potatoes", "Beef", "Broccoli", "Lemons", "Grapes"]
# print(foods[3])

## 6
# print(thelist[0:3])

## 7
# print(thelist[1:3])

## 8
# print(thelist[0:4])

## 9 
# print(thelist[1:])

## 10 
# print(thelist[2:])

## 11
# letters = ["a", "b", "c", "d", "e"]
# letters[0] = "ROCKET"
# print(letters[0])

## 12
# letters = ["a", "b", "c", "d", "e"]
# letters[3] = "WAVE"
# print(letters[3])

## 13
# letters = ["a", "b", "c", "d", "e"]
# letters[-2] = "WAVE"
# print(letters[-2])

## 14
# name = "Becky"
# print(name[0])

## 15
# name = "Becky"
# print(name[2])

## 16
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names[4][3])

## 17
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names[0][4])

## 18
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names[-1][-1])

## 19
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# sentence = "Hello to " + names[1] + " and everyone else."
# print(sentence)

## 20 
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(f"Hello to {names[1]} and everyone else.")

## 21
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# id_num = 4
# print(f"ID: {id_num} Name: {names[id_num]}")

## 22
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# id_num = int(input("select an ID 0-4 : "))
# print(f"ID: {id_num} Name: {names[id_num]}")

## 23
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# names.append("Bob")
# print(names)

## 24
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# new = input("Please add a name to the list. ")
# names.append(f"{new}")
# print(names)

## 25
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# del names[0]
# print(names)

## 26
# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# fired = int(input("Please select a number 0-4 to depart. "))
# del names[fired]
# print(names)

## 27
# start = 1
# stop = 10+1
# step = 2
# num_list = list(range(start, stop, step))
# print(num_list)

## 28
# start = 3
# stop = 30+1
# step = 3
# num_list = list(range(start, stop, step))
# print(num_list)

## 29
# Here are some other list-related functions:
# mynums = [23, 7, 8, 10]
# print(min(mynums))  # The minimum (smallest) value
# print(max(mynums))  # The maximum (largest) value
# print(len(mynums))  # The length (how many elements are in the list)