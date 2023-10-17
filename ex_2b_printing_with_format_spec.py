## Example group 1
# item_number = 27.283
# print()
# print(f"My item num is {item_number}.")
# print()
# print(f"My item num is {item_number:10}. Notice that it is padded with spaces on the left.")
# print()
# print(f"My item num is {item_number:.2f}, rounded to two decimal places.")
# print()
# print(f"My item num is both rounded and has extra space: {item_number:9.2f}. Do you see?")
# print()
# print("You can also center the value within the available space.")
# print("I'll add some letters before and after to make it clear:")
# print(f"letters{item_number:^11.2f}letters")
# print()
# print(f"Here's how to left-align with some letters after for visual context: {item_number:<11.2f}letters")

## Example group 2
# another_num = 17
# print("Here's how to display in binary, octal, hexadecimal:")
# print(f"The number {another_num}, expressed in binary, is {another_num:b}.")
# print(f"The number {another_num}, expressed in octal, is {another_num:o}.")
# print(f"The number {another_num}, expressed in hexadecimal, is {another_num:x}.")

## Incidentally, the format code "d" means decimal, which is the default:
# print(f"The number {another_num}, expressed in decimal, is {another_num:d}.")

## You can also display the number with a prefix that indicates the number system:
# print(f"The number {another_num}, expressed in binary with a prefix, is {another_num:#b}.")
# print(f"The number {another_num}, expressed in octal with a prefix, is {another_num:#o}.")
# print(f"The number {another_num}, expressed in hexadecimal with a prefix, is {another_num:#x}.")

## Note that the format specifiers for other number systems don't work for floats:
# item_number = 27.283
# print(f"This will give an error, because item_number is a float: {item_number:b}.")

## 1
# num = float(input("Type a number: "))
# print(f"The numnumber is {num:.3f}, rounded to three decimal places.")

## 2
# gal = float(input("What is the price of a gallon of gas? "))
# print(f"A gallon is about {gal:.1f}")