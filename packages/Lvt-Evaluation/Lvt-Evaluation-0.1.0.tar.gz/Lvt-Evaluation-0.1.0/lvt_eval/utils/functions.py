import math


def sigmoid_function(z):
    return 1 / (1 + math.exp(-z))

def log_function(z):
    return 1 / (math.log10(z + 1) + 1)

def arc_function(z, y):
    return 1 / (abs((2 / math.pi) * math.atan(z) * (z / y)) + 1)

if __name__ == "__main__":
    print(arc_function(14946, 436763))
    print((2 / math.pi))
    print(math.atan(14946))
    print((14946 / 436763))