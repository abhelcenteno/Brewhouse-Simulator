class Brew:

    last_brew_number = 0

    def __init__(self, product_type):
        self.product_type = product_type
        self.number = None
        self.assign_brew_number()
        self.of_brewhouse = None
        self.current_vessel = None

    def assign_brew_number(self):
        self.number = Brew.last_brew_number + 1
        Brew.last_brew_number = Brew.last_brew_number + 1

    def assign_brewhouse(self, brewhouse):
        self.of_brewhouse = brewhouse

    def __str__(self):
        return f'Brew Number {self.number}'
