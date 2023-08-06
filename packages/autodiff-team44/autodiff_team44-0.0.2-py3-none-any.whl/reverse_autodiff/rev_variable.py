import numpy as np

class Variable:
    def __init__(self, value, local_gradients = ()):
        self.value = value
        self.local_gradients = local_gradients

    def __add__(self, other):
        return add(self, other)

    def __mul__(self, other):
        return mul(self, other)

    def __sub__(self, other):
        return add(self, negative(other))

    def __truediv__(self, other):
        return mul(self, inv(other))

    def __rtruediv__(self, other):
        return mul(other, inv(self))

    def __neg__(self):
        return negative(self)

    def __pow__(self, other):
        return power(self, other)

    __radd__ = __add__

    __rmul__ = __mul__

def add(a, b):
    value = a.value + b.value
    local_gradients = (
        (a, 1),
        (b, 1)
    )

    return Variable(value, local_gradients)

def mul(a, b):
    value = a.value * b.value
    local_gradients = (
        (a, b.value),
        (b, a.value)
    )

    return Variable(value, local_gradients)

def negative(a):
    value = -1 * a.value
    local_gradients = (
        (a, -1),
    )

    return Variable(value, local_gradients)

def inv(a):
    value = 1. / a.value
    local_gradients = (
        (a, -1 / a.value**2),
    )

    return Variable(value, local_gradients)

def sin(a):
    if isinstance(a, Variable):
        value = np.sin(a.value)
        local_gradients = {
            (a, np.cos(a.value)),
        }

        return Variable(value, local_gradients)
    else:
        return np.sin(a)
    

def cos(a):
    value = np.cos(a.value)
    local_gradients = {
        (a, -1*np.sin(a.value))
    }

    return Variable(value, local_gradients)

def tan(a):
    value = np.tan(a.value)
    local_gradients = {
        (a, (1. / np.cos(a.value)) ** 2)
    }

    return Variable(value, local_gradients)

def exp(a):
    value = np.exp(a.value)
    local_gradients = {
        (a, value),
    }

    return Variable(value, local_gradients)

def log(a):
    value = np.log(a.value)
    local_gradients = {
        (a, 1. / a.value),
    }

    return Variable(value, local_gradients)

def sqrt(a):
    value = np.sqrt(a.value)
    local_gradients = {
        (a, 0.5 * (1. / a.value ** 2)),
    }

    return Variable(value, local_gradients)

def power(a, b):
    value = a.value ** b.value
    local_gradients = {
        (a, b.value * (a.value ** (b.value - 1))),
        (b, value * np.log(a.value)),
    }

    return Variable(value, local_gradients)





