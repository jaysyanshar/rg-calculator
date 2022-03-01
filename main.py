def add(x: float, y: float) -> float:
    return x + y

x_in = input("x = ")
y_in = input("y = ")
try:
    x = float(x_in)
    y = float(y_in)
    print("x + y = " + str(x + y))
except:
    print("input should be a number")