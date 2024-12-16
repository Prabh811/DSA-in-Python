
def sum_of_numbers(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def quotient(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculating results
sum_result = sum_of_numbers(num1, num2)
difference_result = difference(num1, num2)
product_result = product(num1, num2)
quotient_result = quotient(num1, num2)

# Displaying results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")