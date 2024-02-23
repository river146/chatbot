import math

def calculator_bot():
    print("hi!!! i can do addition, subtraction, multiplication, division, exponents, and logarithms.")
    while True:
        try:
            operation = input("enter the operation you want to perform (+, -, *, /, ^, log) or 'exit' to end: ").lower()

            # Check if user wants to exit
            if operation == 'exit':
                print("bye!")
                break

            if operation == 'log':
                #log operation 
                base = float(input("enter the base of the logarithm. It cannot be e: "))
                num = float(input("enter the number for the logarithm: "))
                if base <= 0 or base == 1 or num <= 0:
                    print("error. invalid input for logarithm.")
                    continue
                result = math.log(num, base)
                print("Result: log_{:.2f}({:.2f}) = {:.2f}".format(base, num, result))

            else:
                # Get user input for numbers
                num1 = float(input("enter the first number: "))
                num2 = float(input("enter the second number: "))

                #aperform the operation
                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("error: cannot divide by zero.")
                        continue
                    else:
                        result = num1 / num2
                elif operation == '^':
                    result = num1 ** num2
                else:
                    print("invalid operation. please enter +, -, *, /, ^, or log.")
                    continue

                #display the result
                print("result: {:.2f}".format(result))

        except ValueError:
            print("invalid input. please enter valid numbers.")

if __name__ == "__main__":
    calculator_bot()
