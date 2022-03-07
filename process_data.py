from datetime import timedelta


class RedHorse:

    @staticmethod
    def get_data(vessel_name, of_brewhouse):
        # Get the data of for each Processes of Brewhouse 1 of Red Horse
        if vessel_name == "Malt Transport System" and of_brewhouse == 1:
            return (
                ("Transporting Malt", timedelta(minutes=74)),
            )

        elif vessel_name == "Cereal Transport System" and of_brewhouse == 1:
            return (
                ("Transporting Cereal", timedelta(minutes=88)),
            )

        elif vessel_name == "Starch Transport System" and of_brewhouse == 1:
            return (
                ("Transporting Starch", timedelta(minutes=57)),
            )

        elif vessel_name == "Cereal Cooker" and of_brewhouse == 1:
            return (
                ("Starch Do In, 55", timedelta(minutes=46)),
                ("Starch Rest", timedelta(minutes=10)),
                ("Raise to 65", timedelta(minutes=6)),
                ("Cereal Do In, 65", timedelta(minutes=9)),
                ("Cereal Rest", timedelta(minutes=10)),
                ("Raise to 85", timedelta(minutes=14)),
                ("Liquefaction Rest", timedelta(minutes=75)),
                ("Transfer to MTK", timedelta(minutes=16)),
            )

        elif vessel_name == "Mash Tun Kettle" and of_brewhouse == 1:
            return (
                ("Mash Do In, 55", timedelta(minutes=38)),
                ("Combining Mash", timedelta(minutes=16)),
                ("Maltose Rest", timedelta(minutes=60)),
                ("Raise to 72", timedelta(minutes=18)),
                ("Saccharification Rest", timedelta(minutes=20)),
                ("Raise to 76", timedelta(minutes=10)),
                ("Transfer to LT", timedelta(minutes=17)),
            )

        elif vessel_name == "Lauter Tun" and of_brewhouse == 1:
            return (
                ("Underletting", timedelta(minutes=4)),
                ("Underletting Inspection", timedelta(minutes=5)),
                ("Mash Inlet", timedelta(minutes=17)),
                ("Circulation to Clarity", timedelta(minutes=15)),
                ("First Wort Run off", timedelta(minutes=55)),
                ("Sparging", timedelta(minutes=54)),
                ("Weak Wort Recovery", timedelta(minutes=20)),
                ("Drip off", timedelta(minutes=10)),
                ("Spent Grain Removal", timedelta(minutes=16)),
            )

        elif vessel_name == "Wort Kettle" and of_brewhouse == 1:
            return (
                ("PRT to Wort Kettle", timedelta(minutes=29)),
                ("Dosing of Additives", timedelta(minutes=10)),
                ("Boiling", timedelta(minutes=25)),
                ("Post Boil", timedelta(minutes=10)),
                ("Dosing of Additives", timedelta(minutes=10)),
                ("KO Boiling", timedelta(minutes=10)),
                ("Transfer to Whirlpool", timedelta(minutes=12))
            )

        elif vessel_name == "Whirlpool" and of_brewhouse == 1:
            return (
                ("Wort Kettle to Whirlpool", timedelta(minutes=12)),
                ("Whirlpool Rest", timedelta(minutes=25)),
                ("Wort Cooling", timedelta(minutes=75))
            )

        # Get the data of for each Processes of Brewhouse 2 of Red Horse
        elif vessel_name == "Malt Transport System" and of_brewhouse == 2:
            return (
                ("Transporting Malt", timedelta(minutes=86)),
            )

        elif vessel_name == "Cereal Transport System" and of_brewhouse == 2:
            return (
                ("Transporting Cereal", timedelta(minutes=90)),
            )

        elif vessel_name == "Starch Transport System" and of_brewhouse == 2:
            return (
                ("Transporting Starch", timedelta(minutes=67)),
            )

        elif vessel_name == "Cereal Cooker" and of_brewhouse == 2:
            return (
                ("Starch Do In, 55", timedelta(minutes=40)),
                ("Starch Rest", timedelta(minutes=10)),
                ("Raise to 65", timedelta(minutes=7)),
                ("Cereal Do In, 65", timedelta(minutes=9)),
                ("Cereal Rest", timedelta(minutes=10)),
                ("Raise to 85", timedelta(minutes=16)),
                ("Liquefaction Rest", timedelta(minutes=75)),
                ("Transfer to MTK", timedelta(minutes=15)),
            )

        elif vessel_name == "Mash Tun Kettle" and of_brewhouse == 2:
            return (
                ("Mash Do In, 55", timedelta(minutes=37)),
                ("Combining Mash", timedelta(minutes=15)),
                ("Maltose Rest", timedelta(minutes=60)),
                ("Raise to 72", timedelta(minutes=10)),
                ("Saccharification Rest", timedelta(minutes=20)),
                ("Raise to 76", timedelta(minutes=5)),
                ("Transfer to LT", timedelta(minutes=20)),
            )

        elif vessel_name == "Lauter Tun" and of_brewhouse == 2:
            return (
                ("Underletting", timedelta(minutes=4)),
                ("Underletting Inspection", timedelta(minutes=5)),
                ("Mash Inlet", timedelta(minutes=20)),
                ("Circulation to Clarity", timedelta(minutes=10)),
                ("First Wort Run off", timedelta(minutes=62)),
                ("Sparging", timedelta(minutes=47)),
                ("Weak Wort Recovery", timedelta(minutes=12)),
                ("Drip off", timedelta(minutes=10)),
                ("Spent Grain Removal", timedelta(minutes=20)),
            )

        elif vessel_name == "Wort Kettle" and of_brewhouse == 2:
            return (
                ("PRT to Wort Kettle", timedelta(minutes=39)),
                ("Dosing of Additives", timedelta(minutes=10)),
                ("Boiling", timedelta(minutes=25)),
                ("Post Boil", timedelta(minutes=10)),
                ("Dosing of Additives", timedelta(minutes=10)),
                ("KO Boiling", timedelta(minutes=10)),
                ("Transfer to Whirlpool", timedelta(minutes=15))
            )

        elif vessel_name == "Whirlpool" and of_brewhouse == 2:
            return (
                ("Wort Kettle to Whirlpool", timedelta(minutes=15)),
                ("Whirlpool Rest", timedelta(minutes=25)),
                ("Wort Cooling", timedelta(minutes=75))
            )
