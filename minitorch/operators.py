import math
# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back


def mul(a, b):
    return a * b


def id(a):
    return a


def add(a, b):
    return a + b


def lt(a, b):
    return a < b


def eq(a, b):
    return a == b


def neg(a):
    return -a


def max(a, b):
    if a >= b:
        return a
    return b


def is_close(a, b):
    return abs(a - b) < 1e-2


def sigmoid(x):
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        exp_x = math.exp(x)
        return exp_x / (1.0 + exp_x)


def relu(x):
    return max(0.0, x)


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def log_back(x, d):
    return d / x


def inv(x):
    return 1.0 / x


def inv_back(x, d):
    return -d / (x ** 2.0)


def relu_back(x, d):
    return d if x > 0.0 else 0.0


def map(f, lst):
    return [f(x) for x in lst]


def zipWith(f, lst1, lst2):
    return [f(x, y) for x, y in zip(lst1, lst2)]


def reduce(f, lst, start):
    result = start
    for x in lst:
        result = f(result, x)
    return result


def negList(lst):
    return map(neg, lst)


def addLists(lst1, lst2):
    return zipWith(add, lst1, lst2)


def sum_(lst):
    return reduce(add, lst, 0.0)


def prod(lst):
    return reduce(mul, lst, 1.0)
# ## Task 0.3

# Small practice library of elem

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists
