from prettytable import PrettyTable


def f1(x, y):
    return x ** 2 + y ** 2 - 4


def f2(x, y):
    return x * y - 2


def x_next(x, y):
    return x - 0.1*((x * f1(x, y) - y * f2(x, y)) / (2 * (x * x - y * y)))


def y_next(x, y):
    return y - 0.1*((x * f2(x, y) - y * f1(x, y)) / (x * x - y * y))



if __name__ == "__main__":
    E = 0.001
    x = 3
    y = 2
    k = 0
    result = PrettyTable()
    result.field_names = ["k", "x(k)", "x(k+1)", " |x(k+1)-x(k)| ", "y(k)", "y(k+1)", " |y(k+1)-y(k)| "]

    while abs(x_next(x, y) - x) > E or abs(y_next(x, y) - y) > E:
        result.add_row([k, x, x_next(x, y), abs(x_next(x, y) - x), y, y_next(x, y), abs(y_next(x, y) - y)])
        print(k, abs(x_next(x, y) - x), abs(y_next(x, y) - y))
        new_x = x_next(x,y)
        new_y = y_next(x,y)
        x = new_x
        y = new_y
        k += 1
    result.add_row([k, x, x_next(x, y), abs(x_next(x, y) - x), y, y_next(x, y), abs(y_next(x, y) - y)])

    if k > 50:
        print(result.get_string(start=k-50, end = k))
    else:
        print(result)
