import math
from random import randint

class FunctionGenerator:
    def __init__(self, x0_range, x0_max_count):
        self.x0_range = x0_range
        self.x0_max_count = x0_max_count
        self.trigonometric_list = [math.sin, math.cos, math.atan]
    def generateFunction(self):

        x0_amount = randint(1, self.x0_max_count)

        zero_places = self.generateZeroPlaces(x0_amount)
        trigonometric_function = self.trigonometric_list[randint(0, len(self.trigonometric_list)-1)]

        def function(x):
            result = trigonometric_function(math.radians(x))

            for x0 in zero_places:
                result *= (x-x0)
                #print("(x-", x0, ")")
            return result
        return function

    def generateZeroPlaces(self, x0_amount):
        zero_places = []
        for x0 in range(0, x0_amount):
            x = randint(-self.x0_range, self.x0_max_count)
            zero_places.append(x)
        return zero_places

