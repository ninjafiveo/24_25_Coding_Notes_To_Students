# Original Code:
# Below is the original code
# num_1 = input("Enter First number: ")
# num_2 = input("Enter Second number: ")
# operator = input("Enter operator: ")

# print num_1 + operator + num_2

# The Fix
# Remember "input()" only takes in a string. AKA words. You can't math with words. 5+5 = 55 when you use strings. To get the input to be numbers, you need to convert them to either an int ("integer" aka a whole number which is 1, 3, 100, 105, -10, -10005948) or a float ("float" aka a number that has numbers beyond the decimal point. Examples are 96.7, -459.67, 3.14, 1.0, 2.0, -3.0). Changing from a string datatype to a float datatype is also known as datatype casting. Because you are casting from one datatype (string) to another (float)
#! So let's convert the number below to take in a float as the value. 
num_1 = float(input("Enter First number: "))
num_2 = float(input("Enter Second number: "))
print(type(num_1)) # This will print that the number inputted is now a float datatype. 

# The next line really throws a tricky wrench into the problem, that is actually beyond the scope of the assignment or what we've done in class thus far. But let's dive into it and examine how we can make your code work. 
operator = input("Enter operator: ") # You're asking for a math operator here. A math operator is neither a string nor number. So we have to do some python wizardry below.

# Construct the math expression as a string. This actually makes converting the input to numbers above unecessary above. Normally for a math operation there would be an elif statement used or dictionary used, see below for further examples. 
math_expression = f"{num_1} {operator} {num_2}" # If 5, 5, and + is inputted, this makes the string 5 + 5.

# Evaluate the math expression
# The eval() function evaluates this string as a Python expression, performing the arithmetic operation.
math_result = eval(math_expression)
# So what is eval()????
# Imagine you have a calculator in your hand, and you type in a math problem, like 5 + 3. When you press the "equals" button, the calculator looks at the math problem you typed in, figures out what it means, and gives you the answer 8.

# In Python, eval() is like that "equals" button on the calculator. When you give eval() a math problem written as a string, like "5 + 3", it figures out what the problem is asking and then gives you the answer.

# So, if you have the string "5 + 3" and you use eval("5 + 3"), Python will do the math and give you back 8, just like your calculator would.
# While eval() is convenient for simple scripts and learning exercises, it can be dangerous if used with untrusted input in a real-world application, as it can execute arbitrary code. For controlled environments, like this specific case where the input is simple and expected, it can be quite handy.

#? Output the math results. 
print(math_result)

#############
#############
#! Same Problem, but using Elif to determine the expression based on the user input. 
# Take inputs from the user
num_1 = float(input("Enter First number: "))
num_2 = float(input("Enter Second number: "))
operator_input = input("Enter operator (+, -, *, /): ")

# Use elif to determine the operation based on the operator input
if operator_input == '+':
    result = num_1 + num_2
elif operator_input == '-':
    result = num_1 - num_2
elif operator_input == '*':
    result = num_1 * num_2
elif operator_input == '/':
    if num_2 != 0:  # Check to avoid division by zero
        result = num_1 / num_2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operator!"

# Print the result
print(f"The result is: {result}")


#################
#################
# Same problem using Dictionaries.
import operator

# Define a dictionary that maps operator strings to corresponding functions
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Take inputs from the user
num_1 = float(input("Enter First number: "))
num_2 = float(input("Enter Second number: "))
operator_input = input("Enter operator (+, -, *, /): ")

# Get the corresponding function from the dictionary
operation_function = operations.get(operator_input)

# If the operator is valid, perform the calculation; otherwise, print an error message
if operation_function:
    result = operation_function(num_1, num_2)
    print(f"The result is: {result}")
else:
    print("Invalid operator!")
