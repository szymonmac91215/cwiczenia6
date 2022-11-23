from inspect import signature


def argumenty(ars):
    def inner(f):
        def wrapper(*args, **kwargs):
            aa = len(list(signature(f).parameters))
            a = list(args)
            k = aa - len(a)

            if k > len(ars):
                raise TypeError(f'{f.__name__} takes exactly {aa} arguments ({len(ars) + len(a)} given)')

            for i in range(0, k):
                a.append(ars[i])

            return f(*a)

        return wrapper

    return inner


class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def __init__(self):
        self.update()

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        pass

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        pass

    def u_suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')
        return a + b + c

    def u_roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')
        return x - y

    def update(self):
        self.suma = (argumenty(self.argumentySuma))(self.u_suma)
        self.roznica = (argumenty(self.argumentyRoznica))(self.u_roznica)

    def __setitem__(self, key, value):
        if key == 'suma':
            self.argumentySuma = value
        elif key == 'roznica':
            self.argumentyRoznica = value
        self.update()


if __name__ == '__main__':
    op = Operacje()
    op.suma(1, 2, 3)  # Wypisze: 1+2+3=6
    op.suma(1, 2)  # Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1)  # Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    # op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
    op.roznica(2, 1)  # Wypisze: 2-1=1
    op.roznica(2)  # Wypisze: 2-4=-2
    wynik = op.roznica()  # Wypisze: 4-5=-1
    print(wynik)  # Wypisze: 6

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma'] = [1, 2]
    # oznacza, że argumentySuma=[1,2]

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica'] = [1, 2, 3]
    # oznacza, że argumentyRoznica=[1,2,3]

    op.suma(0)
