from rev_variable import *
from collections import defaultdict

def get_gradients(var):
    def default_val(self):
        return 0

    gradients = defaultdict(lambda: 0)

    def compute_gradients(var, path_val):
        for child, local_gradient in var.local_gradients:
            # Multiply edges of path to compute summative value of given path to child
            val_path_to_child = path_val * local_gradient
            # Sum all paths to child 
            gradients[child] += val_path_to_child
            # Recursively move through graph to compute all gradients
            compute_gradients(child, val_path_to_child)

    # path_val is 1 to begin with since initial value is derivative of node with respect to itself, which is 1
    compute_gradients(var, 1)
    return gradients


# a = Variable(4)
# b = Variable(3)
# c = a + b
# d = a * c

# gradients = get_gradients(d)

# print(gradients[a])


def f(a,b):
    # return (a / b - a) * (b / a + a + b) * (a - b)
    return a ** b

a = Variable(1)
b = Variable(2)
y = f(a, b)

gradients = get_gradients(y)

print("The partial derivative of y with respect to a =", gradients[a])
print("The partial derivative of y with respect to b =", gradients[b])


