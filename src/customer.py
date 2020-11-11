class Customer:

    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness


    def add_drunkeness_to_customer(self, drink):
        self.drunkenness += drink.alcohol_level

