from datetime import datetime, timedelta
from brewhouse import Brewhouse
from brew import Brew
from process import CerealCooker, MashTunKettle


def main():
    current_time = datetime(month=3, day=1, year=2022, hour=0, minute=0)

    brewhouse_1 = Brewhouse(1)
    brewhouse_2 = Brewhouse(2)

    cereal_cooker_1 = CerealCooker(brewhouse_1)
    cereal_cooker_2 = CerealCooker(brewhouse_2)

    mash_tun_kettle_1 = MashTunKettle(brewhouse_1)
    mash_tun_kettle_2 = MashTunKettle(brewhouse_2)


if __name__ == '__main__':
    main()
