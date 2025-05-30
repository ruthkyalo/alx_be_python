numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "*":
        result = numb1 * numb2
        print(f"The result is {result}.")
    case "+":
        result = numb1 + numb2
        print(f"The result is {result}.")
    case "-":
        result = numb1 - numb2
        print(f"The result is {result}.")
    case "/":
        try:
            result = numb1 / numb2
            print(f"The result is {result}.")
        except ZeroDivisionError as e:
            print("You can't divide a number by zero.", e)
    case _:
        print("Invalid operation.")
