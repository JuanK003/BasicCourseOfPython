# Assigning the value 3.3 to the variable x and then printing the value of x.
x = 3.3
print(x)

# Adding 1.1 and 2.2 and printing the result.
y = 1.1 + 2.2
print(y)

# Comparing the values of x and y.
print(x == y)

# Formatting the value of y to 2 decimal places and then comparing it to the value of x.
y_str = format(y, ".2g")
print(y_str)
print("V1 ⟹", str(x) == y_str)

# Comparing the values of x and y with a tolerance of 0.00001.
print(x, y)
tolerance = 0.00001
# Comparing the absolute value of the difference between x and y to the tolerance.
print("V2 ⟹",abs(x - y) < tolerance)

# Rounding the value of y to 1 decimal place and then comparing it to the value of x.
print(x, y)
# Comparing the value of x to the value of y rounded to 1 decimal place.
print("V3 ⟹",x == round(y,1))