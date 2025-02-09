# Class "Correct fraction"
class Fraction:
    numerat: int = 0
    denominat: int = 1

    def __init__(self, numerat, denominat):
        if denominat == 0:
            raise ValueError("Illegal value of the denominator")
        self.__numerator = numerat
        self.__denominator = denominat

    # Fraction cloning:
    def __clone(self):
        return Fraction(self.__numerator, self.__denominator)

    # getters and setters:
    @property
    def numerator(self):
        return self.__numerator
    @numerator.setter
    def numerator(self, value):
        self.__numerator = value
    #     # self.__reduce()


    @property
    def denominator(self):
        return self.__denominator
    @denominat.setter
    def denominator(self,value):
        value = int(value)
        if value != 0:
            self.__denominator = value
        else:
            print("Incorrect input denominator!")
    #     # self.__reduce()


# Using magic methods:

    # Bringing the fraction to the term:
    def __str__(self):
        return f"Fraction: {self.__numerator}, {self.__denominator}"

    # Adding methods:
    def __iadd__(self, other):  # +=
        if isinstance(other, Fraction):
            numerat = self.numerator * other.denominator + self.denominator * other.numerator
            denominat = self.denominator * other.denominator
            self.__numerator, self.__denominator = numerat, denominat
            return self
        else:
            raise ValueError("Illegal type of the argument!")

    def __add__(self, other):  # +
        return self.__clone().__iadd__(other)

    # Subtraction method:
    def __sub__(self, other):           # Better method variant use case than the adding method
        if isinstance(other, Fraction):
            numerat = self.__numerator * other.__denominator - other.__numerator * self.__denominator
            denominat = self.__denominator * other.__denominator
            self.__numerator, self.__denominator = numerat, denominat
            return self
        else:
            raise ValueError("Illegal type of the argument!")

    # Multiplying fractions methods:
    def __imul__(self, other):  # *=
        if isinstance(other, Fraction):
            numerat = self.numerator * other.numerator
            denominat = self.denominator * other.denominator
            self.__numerator, self.__denominator = numerat, denominat
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __mul__(self, other):  # *
        return self.__clone().__imul__(other)

    # Division fractions method:
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            numerat = self.__numerator * other.__denominator
            denominat = self.__denominator * other.__numerator
            if denominat == 0:
                raise ValueError("Illegal value of the denominator!")
            self.__numerator, self.__denominator = numerat, denominat
            # self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of the argument!")
##
    # Conversion of fractions to a real value.
    def __float__(self):
        if self.__denominator == 0:
            raise ZeroDivisionError()
        return self.__numerator / self.__denominator
##
    # Comparing fractions methods:
    def __eq__(self, other): # ==
        if isinstance(other, Fraction):
            return self.__float__() == other.__float__()
        else:
            return False

    def __gt__(self, other): # >
        if isinstance(other, Fraction):
            return self.__float__() > other.__float__()
        else:
            return False

    def __lt__(self, other):  # <
        if isinstance(other, Fraction):
            return self.__float__() > other.__float__()
        else:
            return False

    def __ne__(self, other):  # !=
        if isinstance(other, Fraction):
            return not self.__eq__(other)
        else:
            return False


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
print('OK!')
########################################################################################################