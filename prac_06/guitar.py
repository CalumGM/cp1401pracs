
CURRENT_YEAR = 2019
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2}"format(self.name, self.year, self.cost)

    def __get_age__(self):
        return "{} is {}".format(self.name, CURRENT_YEAR - self.year)

    def __is_vintage(self):
        return self.__get_age__() > 50

