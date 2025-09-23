import math
from typing import Any


def mul(a, b) -> Any:
    return a * b


def id(a) -> Any:
    return a


def add(a, b) -> Any:
    return a + b


def lt(a, b) -> Any:
    return a < b


def eq(a, b) -> Any:
    return a == b


def neg(a) -> Any:
    return -a


def max(a, b) -> Any:
    if a >= b:
        return a
    return b


def is_close(a, b) -> Any:
    return abs(a - b) < 1e-2


def sigmoid(x) -> Any:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        exp_x = math.exp(x)
        return exp_x / (1.0 + exp_x)


def relu(x) -> Any:
    return max(0.0, x)


def log(x) -> Any:
    return math.log(x)


def exp(x) -> Any:
    return math.exp(x)


def log_back(x, d) -> Any:
    return d / x


def inv(x) -> Any:
    return 1.0 / x


def inv_back(x, d) -> Any:
    return -d / (x ** 2.0)


def relu_back(x, d) -> Any:
    return d if x > 0.0 else 0.0


def map(f, lst) -> Any:
    return [f(x) for x in lst]


def zipWith(f, lst1, lst2) -> Any:
    return [f(x, y) for x, y in zip(lst1, lst2)]


def reduce(f, lst, start) -> Any:
    result = start
    for x in lst:
        result = f(result, x)
    return result


def negList(lst) -> Any:
    return map(neg, lst)


def addLists(lst1, lst2) -> Any:
    return zipWith(add, lst1, lst2)


def sum_(lst) -> Any:
    return reduce(add, lst, 0.0)


def prod(lst) -> Any:
    return reduce(mul, lst, 1.0)
