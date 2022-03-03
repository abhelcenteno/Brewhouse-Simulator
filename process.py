from datetime import timedelta


class Vessel:
    def __init__(self, name, brewhouse):
        self.availability = True
        self.name = name
        self.of_brewhouse = brewhouse
        brewhouse.add_vessel(self)

    def step(self, brew_number, description, duration, time_start):
        pass

    def __str__(self):
        return self.name


class CerealCooker(Vessel):
    def __init__(self, brewhouse):
        super().__init__(f'Cereal Cooker {brewhouse.number}', brewhouse)

    def start(self, brew_number, time):
        self.step(brew_number, "Starch Do In",
                  timedelta(minutes=35 if brew_number.of_brewhouse.number == 1 else 23), time)
        self.step(brew_number, "Rest for Starch",
                  timedelta(minutes=10), time)
        self.step(brew_number, "Starch Heat Up",
                  timedelta(minutes=8), time)
        self.step(brew_number, "Cereal Do In",
                  timedelta(minutes=50), time)
        self.step(brew_number, "Rest for Cereal",
                  timedelta(minutes=50), time)
        self.step(brew_number, "Raise to Liquefaction",
                  timedelta(minutes=50), time)
        self.step(brew_number, "Rest at Liquefaction",
                  timedelta(minutes=50), time)
        self.step(brew_number, "Transfer to Mash Tun Kettle",
                  timedelta(minutes=50), time)


class MashTunKettle(Vessel):
    def __init__(self, brewhouse):
        super().__init__(f'Mash Tun Kettle {brewhouse.number}', brewhouse)

    def start(self):
        pass
