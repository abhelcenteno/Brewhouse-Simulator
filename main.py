from datetime import datetime, timedelta
import time
from brewhouse import Brewhouse
from brew import Brew
from process import CerealCooker, MashTunKettle


def main():
    current_time = datetime(month=3, day=1, year=2022, hour=0, minute=0)
    simulated_time = datetime(month=3, day=1, year=2022, hour=4, minute=0)

    brewhouse_1 = Brewhouse(1)
    brewhouse_2 = Brewhouse(2)

    cereal_cooker_1 = CerealCooker(brewhouse_1)
    cereal_cooker_2 = CerealCooker(brewhouse_2)

    mash_tun_kettle_1 = MashTunKettle(brewhouse_1)
    mash_tun_kettle_2 = MashTunKettle(brewhouse_2)

    brew1 = Brew(brewhouse_1, "RH")

    while current_time < simulated_time:
        cereal_cooker_1.start(brew1, current_time)

        # time.sleep(1 / 10)
        current_time = current_time + timedelta(minutes=1)

    for data in brew1.cereal_cooker_data:
        print(data)


if __name__ == '__main__':
    main()
