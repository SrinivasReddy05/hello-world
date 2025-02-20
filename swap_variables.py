# # Swap using a temporary variable
#
# # Define the numbers
# a = 5
# b = 10
#
# # Print original numbers
# print(f"Original numbers: a = {a}, b = {b}")
#
# # Swap
# temp = a
# a = b
# b = temp
#
# # Print swapped numbers
# print(f"Swapped numbers: a = {a}, b = {b}")
# Swap without using a temporary variable

# Define the numbers
a = 3546
b = 10

# Print original numbers
print(f"Original numbers: a = {a}, b = {b}")

# Swap
a = a + b
b = a - b
a = a - b

# Print swapped numbers
print(f"Swapped numbers: a = {a}, b = {b}")
