from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0, 100) < self.reliability:  # could i call the drive method of the Car class....how tho?
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance




