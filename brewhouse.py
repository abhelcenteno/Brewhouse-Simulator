class Brewhouse:

    def __init__(self, number,
                 malt_transport_system=None,
                 cereal_transport_system=None,
                 starch_transport_system=None,
                 cereal_cooker=None,
                 mash_tun_kettle = None,
                 lauter_tun = None,
                 pre_run_tank = None,
                 wort_kettle = None,
                 whirlpool = None):
        self.number = number
        self.current_brew = None

        self.malt_transport_system = malt_transport_system
        self.cereal_transport_system = cereal_transport_system
        self.starch_transport_system = starch_transport_system
        self.cereal_cooker = cereal_cooker
        self.mash_tun_kettle = mash_tun_kettle
        self.lauter_tun = lauter_tun
        self.pre_run_tank = pre_run_tank
        self.wort_kettle = wort_kettle
        self.whirlpool = whirlpool

        self.vessels = [
            self.malt_transport_system,
            self.cereal_transport_system,
            self.starch_transport_system,
            self.cereal_cooker,
            self.mash_tun_kettle,
            self.lauter_tun,
            self.pre_run_tank,
            self.wort_kettle,
            self.whirlpool]
        self.assign_brewhouse_of_vessel()
        self.brews_processing = []
        self.brews_processed = []

    def assign_brewhouse_of_vessel(self):
        for vessel in [x for x in self.vessels if x is not None]:
            vessel.assign_brewhouse(self)

    def add_brew(self, brew):
        self.brews_processing.append(brew)
        brew.assign_brewhouse(self)

    def __str__(self):
        return f'Brew House {self.number}'
