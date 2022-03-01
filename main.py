def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

x_in = input("x = ")
y_in = input("y = ")
opt_in = input("1. add\n2. multiply\n")

try:
    x = float(x_in)
    y = float(y_in)
    opt = int(opt_in)
    if opt == 1:
        print("x + y = " + str(add(x, y)))
    elif opt == 2:
        print("x * y = ", str(multiply(x, y)))
except:
    print("input should be a number")