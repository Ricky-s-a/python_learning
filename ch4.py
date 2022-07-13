def bmax(a, b):
    if  a > b:
        return a
    else:
        return b

# check
assert bmax(3, 4) == 4

1 != 2

def absolute(x):
    if x > 0:
        return x
    else:
        return -x
# ckeck
assert absolute(3) == 3
assert absolute(-3) == 3
assert absolute(0) == 0

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
# check
assert sign(5) == 1
assert sign(0) == 0
assert sign(-5) == -1

def is_even(x):
    return x%2 == 0

# check
assert is_even(50) == True
assert is_even(-5) == False

def is_odd(x):
    if is_even(x):
        return False
    else:
        return True

# check
assert is_odd(6) == False
assert is_odd(0) == False
assert is_odd(5) == True

print(None)

if 1:
    print('Ok')
else:
    print('NG')

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(10)
