#calc
operator = input()
var1 = int(input())
var2 = int(input())

if operator == '+':
    print(var1 + var2)
elif operator == '-':
    print(var1 - var2)
elif operator == '*':
    print(var1 * var2)
elif operator == '/':
    print(var1 // var2)
else:
    print("Unable to understand operation")