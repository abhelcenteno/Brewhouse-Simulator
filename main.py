from datetime import datetime, timedelta
import time
from brewhouse import Brewhouse
from brew import Brew
from process import Process, TransportSystem, CerealCooker


def main():
    Process.time = datetime(month=3, day=1, year=2022, hour=0, minute=0)
    end_time = datetime(month=3, day=1, year=2022, hour=12, minute=0)

    malt_transport_1 = TransportSystem("Malt Transport System")
    cereal_transport_1 = TransportSystem("Cereal Transport System")
    starch_transport_1 = TransportSystem("Starch Transport System")
    cereal_cooker_1 = CerealCooker()
    brewhouse_1 = Brewhouse(1, malt_transport_1, cereal_transport_1, starch_transport_1, cereal_cooker_1)

    malt_transport_2 = TransportSystem("Malt Transport System")
    cereal_transport_2 = TransportSystem("Cereal Transport System")
    starch_transport_2 = TransportSystem("Starch Transport System")
    cereal_cooker_2 = CerealCooker()
    brewhouse_2 = Brewhouse(2, malt_transport_2, cereal_transport_2, starch_transport_2, cereal_cooker_2)

    while Process.time < end_time:
        if cereal_cooker_1.brew is None:
            cereal_cooker_1.enter_brew(Brew("Red Horse"))
        cereal_cooker_1.start()
        print(cereal_cooker_1.current_status, Process.time)


        # time.sleep(1/60)
        Process.add_one_minute()

    for brew in cereal_cooker_1.idle:
        print(brew)


if __name__ == '__main__':
    main()
