h = 188.0

h

w = 104.0

# BMI
w / (h/100.0) ** 2

w -= 10
w
w += 10

def bmi(height, weight):
    return weight / (height/100.0) ** 2

bmi(182, 82)
1.1*bmi(174.0, 119.0 * 0.454)

def felt_air_temperature(temperature, humidity):
    return temperature - 1 / 2.3 * (temperature - 10) * (0.8 - humidity / 100)

felt_air_temperature(38, 70)

def ft_to_cm(f, i):
    return f * 30.48 + i / 12 * 30.48

# debug
assert round(ft_to_cm(5, 2) - 157.48, 6) == 0
assert round(ft_to_cm(6, 5) - 195.58, 6) == 0

# 3.2.3
def quadratic(a, b, c, x):
    return a*x + b*x + c

# debug
assert quadratic(1, 2, 1, 3) == 10
assert quadratic(1, -5, -2, 7) == -30

# 3.3
import math
def heron(a, b, c):
    s = 0.5*(a+b+c)
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

heron(3, 4, 5)

def heron(a, b, c):
    s = 0.5*(a+b+c)
    print('The value of s is', str(s))
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

print('a', 'b')

heron(1, 1, 1)

g = 9.8
def force(m):
    return m*g

g = g/6
force(104)
