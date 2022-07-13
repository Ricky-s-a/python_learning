def square(x):
    return x*x

x = -2
assert square(x) >= 0

def square(x):
    return x+x

assert square(x) >= 0

assert square(2) == 4
assert square(-2) == 4
assert square(0) == 0

# define
def median(x, y, z):
    if x > y:
        w = x
        x = y
        y = w
    if z < x:
        return x
    if z < y:
        return z
    return y

# ckeck
assert median(3, 1, 2) == 2

pip install pycodestyle

import pandas as pd
# initialize list elements
data = [10,20,30,40,50,60]

# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data, columns=['Numbers'])
df.head(2)
