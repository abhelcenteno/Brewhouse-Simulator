from datetime import timedelta


class ProcessData:

    @staticmethod
    def get_data(vessel_name, brew_number):
        if vessel_name == "Transport System 1" and brew_number.product_type == "RH":
            transport_data_rh1 = (
                ("Malt Transport", timedelta(minutes=74)),
                ("Cereal Transport", timedelta(minutes=88)),
                ("Starch Transport", timedelta(minutes=57))
            )
            return transport_data_rh1

        elif vessel_name == "Cereal Cooker 1" and brew_number.product_type == "RH":
            cereal_cooker_data_rh1 = (
                ("Starch Do In, 55", timedelta(minutes=46)),
                ("Starch Rest", timedelta(minutes=10)),
                ("Raise to 65", timedelta(minutes=6)),
                ("Cereal Do In, 65", timedelta(minutes=9)),
                ("Cereal Rest", timedelta(minutes=10)),
                ("Raise to 85", timedelta(minutes=14)),
                ("Liquefaction Rest", timedelta(minutes=75)),
                ("Transfer to MTK", timedelta(minutes=16)),
            )
            return cereal_cooker_data_rh1
