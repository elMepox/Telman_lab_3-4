from prettytable import PrettyTable


def f1(x, y):
    return x ** 2 + y ** 2 - 4


def f2(x, y):
    return x * y - 2


def alpha(x, y):
    return x / (2 * (y ** 2 - x ** 2))


def betta(x, y):
    return y / (x ** 2 - y ** 2)


def gamma(x, y):
    return y / (2 * (x ** 2 - y ** 2))


def teta(x, y):
    return x / (y ** 2 - x ** 2)


def x_next(x, y):
    return x + f1(x, y) * alpha(x, y) + f2(x, y) * betta(x, y)




def y_next(x, y):
    return y + f1(x, y) * gamma(x, y) + f2(x, y) * teta(x, y)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == "__main__":
    E = 0.001
    x = 3
    y = 2
    k = 0
    result = PrettyTable()
    result.field_names = ["k", "x(k)", "x(k+1)", " |x(k+1)-x(k)| ", "y(k)", "y(k+1)", " |y(k+1)-y(k)| "]



    while abs(x_next(x, y) - x) > E or abs(y_next(x, y) - y) > E:
        result.add_row([k, x, x_next(x, y), abs(x_next(x, y) - x), y, y_next(x, y), abs(y_next(x, y) - y)])
        print(k,abs(x_next(x, y) - x), (y_next(x, y) - y))
        new_x = x_next(x, y)
        new_y = y_next(x, y)
        x = new_x
        y = new_y
        k += 1
    result.add_row([k, x, x_next(x, y), abs(x_next(x, y) - x), y, y_next(x, y), abs(y_next(x, y) - y)])

    print(result)
