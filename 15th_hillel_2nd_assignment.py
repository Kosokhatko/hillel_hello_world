from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може дорівнювати нулю.")
        if a >= b:
            raise ValueError("Це не правильний дріб (чисельник має бути менший за знаменник).")
        self.a = a
        self.b = b
        self._reduce()

    def _reduce(self):
        """Скорочення дробу."""
        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

    def __add__(self, other):
        num = self.a * other.b + other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.a * other.b - other.a * self.b
        den = self.b * other.b
        if num < 0:
            raise ValueError("Результат не є правильним дробом (від'ємний).")
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.a * other.a
        den = self.b * other.b
        return Fraction(num, den)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

# Тестування
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)     # скоротиться до 1/2
f_c = f_b + f_a          # 1/2 + 2/3 = 7/6 → ValueError: не правильний дріб?

# Щоб пройти всі тести, зміню на очікувану реалізацію з **нескороченням**, як у тестах:
class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути нульовим.")
        self.a = a
        self.b = b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

    def __add__(self, other):
        num = self.a * other.b + other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.a * other.b - other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.a * other.a
        den = self.b * other.b
        return Fraction(num, den)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

# Тестування згідно з наданими assert
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c
assert f_d > f_e
assert f_a != f_b

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2

print("OK")
