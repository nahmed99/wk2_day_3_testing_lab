class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till

        self.drinks = []


    def drinks_list_length(self):
        return len(self.drinks)


    def add_drink(self, drink):
        self.drinks.append(drink)


    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink


    def add_money_to_till(self, drink):
        self.till += drink.price
        print(" alsdjalsjdldjaldksjalsdkj",self.till)


    def get_till_total(self):
        return self.till



    #def take_money_from_customer(self, customer, drink):
    #    customer.wallet -= drink.price

    def sell_drink_to_customer(self, drink_name):
        pass