def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero is not allowed"
        return a / b
    elif op == "%":
        if b == 0:
            return "Error: Modulo by zero is not allowed"
        return a % b
    else:
        return "Invalid Operator"


a = int(input("ENTER FIRST NUMBER: "))
op = input("ENTER OPERATOR (+ - * / %): ")
b = int(input("ENTER SECOND NUMBER: "))

result = calculator(a, op, b)
print("OUTPUT:", result)
