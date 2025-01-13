# Will need a atan function for argument of ComplexNum

class ComplexNum:
    def __init__(self, re: float, im: float) -> None:
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ComplexNum(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return ComplexNum(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im)

    def __truediv__(self, other):
        if other.re == 0 and other.im == 0:
            raise Exception("Cannot divide by 0!")
        factor = other.re**2 + other.im**2
        return ComplexNum((self.re*other.re+self.im*other.im)/factor,(self.im*other.re - self.re*other.im)/factor)

    # def __pow__(self, other)

    def __eq__(self, other) -> bool:
        return self.re == other.re and self.im == other.im

    def __repr__(self) -> str:
        return str(self.re) + " + "+str(self.im)+"i"

    def abs(self):
        return ((self.re ** 2) + (self.im ** 2)) ** 0.5

if __name__ == "__main__":
    a = ComplexNum(1, 2)
    b = ComplexNum(-1, 2)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
