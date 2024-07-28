def cube(num):
    return num*num*num

print("The cube of 3 is: ", cube(3))
print("The cube of 5 is: ", cube(5))

def multiply(num1, num2):
    return num1 * num2

number1 = input("Pick a number: ")
number2 = input("Pick another number: ")
product = multiply(float(number1), float(number2))

print(f"The product of {number1} and {number2} is {product}.")

def convertFtoC(degrees_Fahrenheit):
    return (degrees_Fahrenheit - 32) * 5/9

def convertCtoF(degrees_Celsius):
    return degrees_Celsius * 9/5 + 32

temp1 = input("Enter a temperature in Fahrenheit: ")
tempC = convertFtoC(float(temp1))
print(f"{temp1} degrees F = {tempC} degrees C")

temp2 = input("Enter a temperature in Celsius: ")
tempF = convertCtoF(float(temp2))
print(f"{temp2} degrees C = {tempF} degrees F")

