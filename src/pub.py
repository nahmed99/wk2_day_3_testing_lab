class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till

        self.drinks = []



    def drinks_list_length(self):
        return len(self.drinks)