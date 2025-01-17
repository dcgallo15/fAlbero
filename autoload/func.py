from math import atan

E   = 2.7182818284
PI  = 3.1415926535

# My Implementations of functions
# TODO: factorial, ln, sec, csc, cot, asin, acos, atan, asec, acsc, acot, sinh, cosh, tanh, asinh, acosh, atanh
# TODO: complex numbers implementation?

# NOTE: can maybe move to a new file?
class Fn:
    def factorial(self, x: int) -> int:
        if x <= 0:
            return 1
        return (self.factorial(x - 1)  * x)

    def ln(self, x: float) -> float:
        if x <= 0:
            raise Exception("Domain Error in ln function")
        # Use approx of ln(x) : ax^(1/a) - a where a is some very large number
        a = 10**9
        return a*(x ** (1/a)) - a

    def sin(self, x: float) -> float:
        if x == PI or x == 2*PI:
            return 0
        # Converts input into 0->2*PI using periodicity of sin function
        frac = x/(2*PI)
        if frac > 0:
            floor = int(frac)
        else:
            floor = int(frac - 0.9999999999999999)
        x = (x - 2*PI * floor);
        # TODO: add more terms
        return (x - ((x ** 3) / 6) + ((x ** 5) / 120) - ((x ** 7) / 5040) +
                ((x **9) / 362880) - ((x ** 11) / 39916800) + ((x ** 13) / 6227020800) - ((x ** 15) / 1307674368000) + ((x ** 17) / 355687428096000) -
                ((x ** 19) / 121645100408832000) + ((x ** 21) / 51090942171709440000))

    def cos(self, x: float) -> float:
        return self.sin(x + (PI / 2))

    def tan(self, x: float) -> float:
        tmp = self.cos(x)
        if tmp == 0:
            raise Exception("Domain Error in tan function")
        return (self.sin(x) / tmp)

    def asin(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def acos(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def atan(self, x: float) -> float:
        return atan(x)

    def sec(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def csc(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def cot(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

fn = Fn()


