CURRENT_YEAR = 2019
VINTAGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def __get_age__(self):
        return CURRENT_YEAR - self.year

    def __is_vintage__(self):
        return self.__get_age__() >= VINTAGE
