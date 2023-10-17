print("Hello")
name = input("What is your name? ")
print(f"Greetings, {name}")
print("This is a basic calculator that adds, subtracts, multiplies, and divides.")
num = float(input("Please select a number: "))
num2 = float(input("Please select another number: "))
sum = num + num2
diff = num - num2
product = num * num2
quotient = num / num2
print(f"The sum is {sum}")  
print(f"The difference is {diff} ")   
print(f"The product is {product}.")   
print(f"The quotient is {quotient:.4f}.") 
print("Now, we are going to convert distance from km to m.")
kilo = float(input("what is a distance in kilometers? "))
meters = kilo * 1000
print(f"In meters, that would be {meters}m.")
print("Have a good day!")