

# This is my input
expression = input("Expression: ")

x,z,y = expression.split(" ")

# Hear I want to convert string into float value to have the possibility to
# do operations
x_n = float(x)
y_n = float(y)

# this is the calculation
if z == "+":
    result = round((x_n + y_n) * 1.0,1)
elif z == "-":
    result = round((x_n - y_n) * 1.0,1)
elif z == "*":
    result = round((x_n * y_n) * 1.0,1)
elif z == "/":
    result = round((x_n / y_n) * 1.0,1)




# print result
print(result)
