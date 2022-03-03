class Brew:

    latest_brew_number = 0

    def __init__(self, brewhouse, product_type):
        self.product_type = product_type
        self.brew_number = None
        self.assign_brew_number()
        self.of_brewhouse = brewhouse
        brewhouse.add_brew(self)

        self.cereal_cooker_data = []

    def assign_brew_number(self):
        self.brew_number = Brew.latest_brew_number + 1
        Brew.latest_brew_number = Brew.latest_brew_number + 1

    def __str__(self):
        return f'Brew Number {self.brew_number}'
