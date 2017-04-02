import math
from random import randint

class FunctionGenerator:
    def __init__(self, x0_range, x0_max_count):
        self.x0_range = x0_range
        self.x0_max_count = x0_max_count
        self.trigonometric_list = [math.sin, math.cos, math.atan]
    def generateFunction(self):

        x0_amount = randint(1, self.x0_max_count)
        print("Function contains", x0_amount, "zero places")

        zero_places = self.generateZeroPlaces(x0_amount)
        trigonometric_function = self.trigonometric_list[randint(0, len(self.trigonometric_list)-1)]
        print(trigonometric_function)

        def function(x):
            result = trigonometric_function(x)

            exponentials = self.generateExponental()
            result *= exponentials[0] ** (exponentials[1]*x)
            result *= exponentials[2] ** (exponentials[3]*x)

            print(exponentials[0], "**", exponentials[1], "x")
            print(exponentials[2], "**", exponentials[3], "x")

            for x0 in zero_places:
                result *= (x-x0)
                print("(x-", x0, ")")
            return result
        return function

    def generateZeroPlaces(self, x0_amount):
        zero_places = []
        for x0 in range(0, x0_amount):
            x = randint(-self.x0_range, self.x0_max_count)
            zero_places.append(x)
        print(zero_places)
        return zero_places

    def generateExponental(self):
        a1 = randint(1, self.x0_range)
        b1 = randint(-self.x0_range, -1)

        a2 = randint(1, self.x0_range)
        b2 = randint(1, self.x0_range)

        return (a1,b1,a2,b2)
