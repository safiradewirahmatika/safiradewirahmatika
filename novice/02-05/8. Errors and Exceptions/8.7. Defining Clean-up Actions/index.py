try:
# raise KeyboardInterrupt
# finally
        print('Goodbye, world!')

# KeyboardInterrupt
# Traceback (most recent call last):
# File "<stdin>", line 2, in <module>

def bool_return():
    try:
        return True
    finally
        return False
print(bool_return())

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
print(divide(2, 1))

divide(2, 0)
divide("2", "1")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'