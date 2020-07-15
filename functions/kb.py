def myFirstFunction():
    print("Something")

def addTwoNumbers():
    num1 = int(input("select first number: "))
    num2 = int(input("select second number: "))
    total = num1 + num2
    return total

# This is a way to add parameters to the function and if not provided, it will ask for input
def addTwoNumbers2(num1 = "", num2 = ""):
    if num1 == "":
        num1 = int(input("select first bb number: "))
    if num2 == "":
        num2 = int(input("select second bb number: "))
    total = num1 + num2
    return total

def multiplyTwoNumbers():
    num1 = int(input("select first number: "))
    num2 = int(input("select second number: "))
    total = num1 * num2
    # print(total)
    return total

# myTotal = addTwoNumbers()
# print(myTotal)
#
# myMultiplyTotal = multiplyTwoNumbers()
# print(myMultiplyTotal)
#
# print(addTwoNumbers2(myTotal, myMultiplyTotal))
