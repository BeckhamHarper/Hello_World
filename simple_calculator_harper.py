print("Welcome to my simple calculator program, it will calculate problems for you!") # Prints beginning message

firstNumber = int(input("What's the first number? ")) # Input for 1st number
secondNumber = int(input("What's the second number? ")) # Input for 2nd number

print("Sum of "+ str(firstNumber)+" and " + str(secondNumber) +" = "+ str(firstNumber+secondNumber)) # Prints the addition of the two numbers
print("Difference of "+ str(firstNumber)+ " and "+ str(secondNumber)+ " = "+ str(firstNumber-secondNumber)) # Prints the subtraction of the two numbers
print("Product of "+str(firstNumber)+ " and "+ str(secondNumber)+ " = "+ str(firstNumber*secondNumber)) # Prints the multiplication of the two numbers
print("Quotient of "+ str(firstNumber)+ " and "+ str(secondNumber)+ " = "+ str(firstNumber/secondNumber)) # Prints the division of the two numbers
print("Calculations for the numbers "+ str(firstNumber)+ " and "+ str(secondNumber)+ " complete.") # Prints the final message