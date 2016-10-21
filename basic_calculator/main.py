"""This is the entry point of the program."""


def basic_calculator(num1, num2, operation):
    if operation == 'add':
        ans=num1+num2
        return ans
    elif operation == 'subtract':
        ans=num1-num2
        return ans
    elif operation == 'multiply':
        ans=num1*num2
        return ans
    elif operation == 'divide':
        ans=num1/num2
        return ans
    elif operation != 'add'or'subtract'or'multiply'or'divide':
        return 'Invalid operation'