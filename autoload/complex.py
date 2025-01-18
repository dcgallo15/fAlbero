from func import Fn
# Will need a atan function for argument of ComplexNum

fn = Fn()

class ComplexNum:
    def __init__(self, re: float, im: float) -> None:
        self.re = re
        self.im = im

    def __add__(self, other):
        # NOTE: this only works if the complex number is first
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.re + other, self.im)
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.re - other, self.im)
        return ComplexNum(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.re * other, self.im * other)
        return ComplexNum(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im)

    # def __div__ (self, other) -> ComplexNum: # Does this make sense here?

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise Exception("Cannot divide by 0!")
            return ComplexNum(self.re / other, self.im / other)
        if other.re == 0 and other.im == 0:
            raise Exception("Cannot divide by 0!")
        factor = other.re**2 + other.im**2
        return ComplexNum((self.re*other.re+self.im*other.im)/factor,(self.im*other.re - self.re*other.im)/factor)

    # def __pow__(self, other)

    def __eq__(self, other) -> bool:
        if not isinstance(other, ComplexNum):
            return False
        return self.re == other.re and self.im == other.im

    def __repr__(self) -> str:
        if self.im == 0:
            return str(self.re)
        if self.im < 0:
            return str(self.re) + " - "+str(-1.0*self.im) + "i"
        return str(self.re) + " + "+str(self.im) + "i"


    def mod(self):
        return ((self.re ** 2) + (self.im ** 2)) ** 0.5

    def arg(self):
        return fn.atan(self.im / self.re)

if __name__ == "__main__":
    a = ComplexNum(1, 2)
    b = ComplexNum(-1, 2)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
