class Brewhouse:

    def __init__(self, number):
        self.number = number
        self.vessels = []
        self.brews = []

    def add_vessel(self, vessel):
        self.vessels.append(vessel)

    def add_brew(self, brew):
        self.brews.append(brew)

    def print_vessels(self):
        for vessel in self.vessels:
            if not vessel == self.vessels[-1]:
                print(vessel, end=", ")
            else:
                print(vessel)

    def print_brews(self):
        for brew in self.brews:
            if not brew == self.brews[-1]:
                print(brew, end=", ")
            else:
                print(brew)

    def __str__(self):
        return f'Brew House {self.number}'
