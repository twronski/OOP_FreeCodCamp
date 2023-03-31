from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_broken_phones=0):
        assert number_broken_phones >= 0, f"Broken Phones {number_broken_phones} is not greater than 0"
        self.number_broken_phones = number_broken_phones

        super().__init__(name, price, quantity)
