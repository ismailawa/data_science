import math

# Function to calculate e^x
def calculate_exponential(x):
    return math.exp(x)

# Example usage
x = input("enter x: ")
result = calculate_exponential(int(x))
y = ""
print(f"e raised to the power of {x} is: {result, 6}")
