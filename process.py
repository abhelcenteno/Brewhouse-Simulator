from datetime import timedelta
from process_data import ProcessData


class Vessel:
    def __init__(self, name, brewhouse):
        self.status = None
        self.name = name
        self.of_brewhouse = brewhouse
        brewhouse.add_vessel(self)
        
        self.current_step = 0
        self.target_time = None
        self.steps = None

    def generate_steps(self, brew_number):
        self.steps = ProcessData.get_data(self.name, brew_number)

    def update_status(self, brew_number, time):
        if self.current_step == len(self.steps) - 1:
            self.status = None
            self.current_step = 0
            self.target_time = None

        else:
            brew_number.cereal_cooker_data[self.current_step].append(time)
            self.current_step += 1
            self.status = self.steps[self.current_step][0]
            self.target_time = time + self.steps[self.current_step][1]
            brew_number.cereal_cooker_data.append([self.status, time])

    def __str__(self):
        return self.name


class CerealCooker(Vessel):
    def __init__(self, brewhouse):
        super().__init__(f'Cereal Cooker {brewhouse.number}', brewhouse)

    def start(self, brew_number, time):
        if self.status is None and self.current_step == 0:
            self.generate_steps(brew_number)
            self.status = self.steps[self.current_step][0]
            self.target_time = time + self.steps[self.current_step][1]
            brew_number.cereal_cooker_data.append([self.status, time])

        if self.status is not None:
            # print(f"{brew_number} is currently at {self.status} as of {time}.")
            if time == self.target_time:
                self.update_status(brew_number, time)


class MashTunKettle(Vessel):
    def __init__(self, brewhouse):
        super().__init__(f'Mash Tun Kettle {brewhouse.number}', brewhouse)

