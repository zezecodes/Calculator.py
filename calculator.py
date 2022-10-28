def addition():
    sumVal1 = int(input("Please input the first value you want to sum up: "))
    sumVal2 = int(input("Now input the second: "))
    addNumber1 = sumVal1
    addNumber2 = sumVal2

    return print("The sum is: "+str(sumVal1 + sumVal2))
    
def subtraction():
    diffVal1 = int(input("Please input the first value you want to sum up: "))
    diffVal2 = int(input("Now input the second: "))
    subtractNumber1 = diffVal1
    subtractNumber2 = diffVal2

    return print("The difference is: "+str(diffVal1 - diffVal2))

def division():
    diffVal1 = int(input("Please input the first value you want to sum up: "))
    diffVal2 = int(input("Now input the second: "))
    subtractNumber1 = diffVal1
    subtractNumber2 = diffVal2

    return print("The quotient is: "+(x/y))

def multiplication():
    return print("The product is: "+(x*y))

operationInput = input("Please input the operation you want to use on your values(+ _ * /): ")
if operationInput == "+":    
    print(addition())
elif operationInput == "-":
    print(subtraction())
elif operationInput == "*":
    print(multiplication())
elif operationInput == "/":
    print(division())
