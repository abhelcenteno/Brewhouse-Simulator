from datetime import datetime, timedelta
from process_data import RedHorse


class Process:

    time = datetime.today()

    def __init__(self, name):
        self.name = name
        self.of_brewhouse = None
        self.current_step = 0
        self.current_status = None
        self.next_target_time = None
        self.brew = None
        self.data = None
        self.start_time = None
        self.end_time = None
        self.idle = []
        self.brews_processed = []

    def assign_brewhouse(self, brewhouse):
        self.of_brewhouse = brewhouse

    def enter_brew(self, brew):
        self.brew = brew
        self.start_time = self.time
        if self.brew.product_type == "Red Horse":
            self.data = RedHorse.get_data(self.name, self.of_brewhouse.number)
            self.current_status = self.data[0][0]
            self.start()

        elif self.brew.product_type == "San Mig Light":
            # self.data = SanMigLight.get_data(self.name, self.of_brewhouse.number)
            pass

        elif self.brew.product_type == "Pale Pilsen":
            # self.data = PalePilsen.get_data(self.name, self.of_brewhouse.number)
            pass

    def next_step(self):
        self.current_step += 1
        self.current_status = self.data[self.current_step][0]
        self.next_target_time = self.next_target_time + self.data[self.current_step][1]
        self.start()


    def exit_brew(self):
        self.end_time = self.time
        self.brews_processed.append((self.brew, self.start_time, self.end_time))
        self.brew = None
        self.current_step = 0
        self.current_status = "Idle"
        self.end()


    @classmethod
    def add_one_minute(cls):
        cls.time += timedelta(minutes=1)

    def __str__(self):
        return f'{self.name} {self.of_brewhouse.number}'


class TransportSystem(Process):
    system_transporting = []

    def __init__(self, name):
        super().__init__(name)

    def start(self):
        if (self.brew is not None and self.next_target_time is None and
                not bool([x for x in TransportSystem.system_transporting if x[0] == self.name])):
            TransportSystem.system_transporting.append((self.name, self))
            self.next_target_time = self.time + self.data[0][1]
            self.start_time = self.time
        elif self.brew is not None and (self.name, self) not in TransportSystem.system_transporting:
            self.current_status = 'Waiting for other Brewhouse to finish Transport'
        elif self.brew is not None and self.next_target_time is not None:
            if self.time >= self.next_target_time:
                self.exit_brew()

    def end(self):
        TransportSystem.system_transporting.remove((self.name, self))
        self.next_target_time = None

class CerealCooker(Process):
    def __init__(self):
        super().__init__("Cereal Cooker")
        self.waiting_for_MTK_start = None
        self.waiting_for_MTK_end = None

    def start(self):
        if self.brew is not None and self.next_target_time is None:
            self.next_target_time = self.time + self.data[0][1]
            self.start_time = self.time
        elif self.brew is not None and self.next_target_time is not None:
            if self.time >= self.next_target_time and self.current_step == len(self.data)-1:
                self.exit_brew()
            elif self.time >= self.next_target_time and self.current_status == "Liquefaction Rest":
                if self.waiting_for_MTK_start is None:
                    self.waiting_for_MTK_start = self.time
                self.is_mash_tun_kettle_available()
            elif self.time >= self.next_target_time:
                self.next_step()

    def is_mash_tun_kettle_available(self):
        if True:
        # if self.of_brewhouse.mash_tun_kettle.is_ready_for_cereal_cooker:
            self.waiting_for_MTK_end = self.time
            if self.waiting_for_MTK_start != self.waiting_for_MTK_end:
                self.idle.append((self.brew,self.waiting_for_MTK_start, self.waiting_for_MTK_end))
            self.waiting_for_MTK_start, self.waiting_for_MTK_end = None, None
            self.next_step()

    def end(self):
        self.next_target_time = None

class MashTunKettle(Process):
    def __init__(self):
        super().__init__("Mash Tun Kettle")
        self.waiting_for_CC_start = None
        self.waiting_for_CC_end = None
        self.waiting_for_LT_start = None
        self.waiting_for_LT_end = None

    def start(self):
        if self.brew is not None and self.next_target_time is None:
            self.next_target_time = self.time + self.data[0][1]
            self.start_time = self.time
        elif self.brew is not None and self.next_target_time is not None:
            if self.time >= self.next_target_time and self.current_step == len(self.data)-1:
                self.exit_brew()
            elif self.time >= self.next_target_time and self.current_status == "Mash Do In, 55":
                if self.waiting_for_CC_start is None:
                    self.waiting_for_CC_start = self.time
                self.is_cereal_cooker_available()
            elif self.time >= self.next_target_time and self.current_status == "Saccharification Rest":
                if self.waiting_for_LT_start is None:
                    self.waiting_for_LT_start = self.time
                self.is_cereal_cooker_available()
            elif self.time >= self.next_target_time:
                self.next_step()

    def is_cereal_cooker_available(self):
        if True:
        # if self.of_brewhouse.mash_tun_kettle.is_ready_for_cereal_cooker:
            self.waiting_for_CC_end = self.time
            if self.waiting_for_CC_start != self.waiting_for_CC_end:
                self.idle.append((self.brew,self.waiting_for_CC_start, self.waiting_for_CC_end))
            self.waiting_for_CC_start, self.waiting_for_CC_end = None, None
            self.next_step()

    def is_lauter_tun_available(self):
        if True:
        # if self.of_brewhouse.mash_tun_kettle.is_ready_for_cereal_cooker:
            self.waiting_for_LT_end = self.time
            if self.waiting_for_LT_start != self.waiting_for_LT_end:
                self.idle.append((self.brew,self.waiting_for_LT_start, self.waiting_for_LT_end))
            self.waiting_for_LT_start, self.waiting_for_LT_end = None, None
            self.next_step()

    def end(self):
        self.next_target_time = None



