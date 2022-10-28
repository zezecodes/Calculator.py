def addition():
    sumVal1 = int(input("Please input the first value you want to sum up: "))
    sumVal2 = int(input("Now input the second: "))
    addNumber1 = sumVal1
    addNumber2 = sumVal2

    return print("The sum is: "+str(sumVal1 + sumVal2))
    
def subtraction():
    diffVal1 = int(input("Please input the value you want to subtract: "))
    diffVal2 = int(input("Now input the value you want to subtract from: "))
    subtractNumber1 = diffVal1
    subtractNumber2 = diffVal2

    return print("The difference is: "+str(diffVal2 - diffVal1))

def division():
    quotientVal1 = int(input("Please input the dividend: "))
    quotientVal2 = int(input("Now input the divisor: "))
    divisionNumber1 = quotientVal1
    divisionNumber2 = quotientVal2

    return print("The quotient is: "+str(quotientVal1 / quotientVal2))

def multiplication():
    productVal1 = int(input("Please input the multipicand: "))
    productVal2 = int(input("Now the multiplier: "))
    multiplicationNumber1 = productVal1
    multiplicationNumber2 = productVal2
    return print("The product is: "+str(productVal1*productVal2))

operationInput = input("Please input the operation you want to use on your values(+ _ * /): ")
if operationInput == "+":    
    print(addition())
elif operationInput == "-":
    print(subtraction())
elif operationInput == "*":
    print(multiplication())
elif operationInput == "/":
    print(division())
