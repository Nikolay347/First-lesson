class Fraction:
    a: int = 0
    b: int = 1

    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Illegal value of the denominator")
        self.__numerator = a
        self.__denominator = b

    # Клонировать дробь.
    def __clone(self):
        return Fraction(self.__numerator, self.__denominator)

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = int(value)


    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        value = int(value)
        if value == 0:
            raise ValueError("Illegal value of the denominator")
        self.__denominator = value


    # Привести дробь к строке.
    def __str__(self):
        return f"Fraction: {self.__numerator}, {self.__denominator}"

    # def __repr__(self):
    #     return self.__str__()

    # Привести дробь к вещественному значению.
    def __float__(self):
        if self.__denominator == 0:
            raise ZeroDivisionError()
        return self.__numerator / self.__denominator

    # Привести дробь к логическому значению.
    # def __bool__(self):
    #     return self.__numerator != 0

#
    # Сложение обыкновенных дробей.
    def __iadd__(self, rhs):  # +=
        if isinstance(rhs, Fraction):
            a = self.numerator * rhs.denominator + \
                self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator
            self.__numerator, self.__denominator = a, b

            return self
        else:
            raise ValueError("Illegal type of the argument")

    # drob1 + drob2 ====> drob1 += drob2
    def __add__(self, rhs):  # +
        return self.__clone().__iadd__(rhs)

    # Вычитание обыкновенных дробей.
    # def __isub__(self, rhs):  # -=
    #     if isinstance(rhs, Fraction):
    #         a = self.numerator * rhs.denominator - \
    #             self.denominator * rhs.numerator
    #         b = self.denominator * rhs.denominator
    #         self.__numerator, self.__denominator = a, b
    #
    #         return self
    #     else:
    #         raise ValueError("Illegal type of the argument")

    def __sub__(self, rhs):  # -
        if isinstance(rhs, Fraction):
            a = self.numerator * rhs.denominator - \
                self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator
            self.__numerator, self.__denominator = a, b

            return self
        else:
            raise ValueError("Illegal type of the argument")

    # Умножение обыкновенных дробей.
    def __imul__(self, rhs):  # *=
        if isinstance(rhs, Fraction):
            a = self.numerator * rhs.numerator
            b = self.denominator * rhs.denominator
            self.__numerator, self.__denominator = a, b

            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __mul__(self, rhs):  # *
        return self.__clone().__imul__(rhs)

    # Деление обыкновенных дробей.
    # def __itruediv__(self, rhs):  # /=
    #     if isinstance(rhs, Fraction):
    #         a = self.numerator * rhs.denominator
    #         b = self.denominator * rhs.numerator
    #         if b == 0:
    #             raise ValueError("Illegal value of the denominator")
    #         self.__numerator, self.__denominator = a, b
    #
    #         return self
    #     else:
    #         raise ValueError("Illegal type of the argument")

    def __truediv__(self, rhs):  # /
        if isinstance(rhs, Fraction):
            a = self.numerator * rhs.denominator
            b = self.denominator * rhs.numerator
            if b == 0:
                raise ValueError("Illegal value of the denominator")
            self.__numerator, self.__denominator = a, b

            return self
        else:
            raise ValueError("Illegal type of the argument")

    # Отношение обыкновенных дробей.
    def __eq__(self, rhs):  # ==
        if isinstance(rhs, Fraction):
            return self.__float__() == rhs.__float__()
        else:
            return False

    def __ne__(self, rhs):  # !=
        if isinstance(rhs, Fraction):
            return not self.__eq__(rhs)
        else:
            return False

    def __gt__(self, rhs):  # >
        if isinstance(rhs, Fraction):
            return self.__float__() > rhs.__float__()
        else:
            return False

    def __lt__(self, rhs):  # <
        if isinstance(rhs, Fraction):
            return self.__float__() < rhs.__float__()
        else:
            return False

    def __ge__(self, rhs):  # >=
        if isinstance(rhs, Fraction):
            return not self.__lt__(rhs)
        else:
            return False

    def __le__(self, rhs):  # <=
        if isinstance(rhs, Fraction):
            return not self.__gt__(rhs)
        else:
            return False


if __name__ == '__main__':
    r1 = Fraction(3, 4)

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(str(f_c))
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
print(f_d)
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

# r1 = Fraction(3, 4)
# print()
# print(float(r1))
# print(r1)
# print(f"r1 = {r1}")
# r2 = Fraction(5, 6)
# r1 += r2

# print(r1)
# print(f"r2 = {r2}")
# print(f"{r1} + {r2} = {r1 + r2}")
# print(f"{r1} - {r2} = {r1 - r2}")
# print(f"{r1} * {r2} = {r1 * r2}")
# print(f"{r1} / {r2} = {r1 / r2}")