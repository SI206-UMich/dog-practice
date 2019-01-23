# Discussion 2 Example Dog Class

class Dog:

    def __init__(self, name = "Fido", weight = 20):
        self.name = name
        self.weight = weight
        self.treat_count = 0
        self.tricks = []

    def __str__(self):
        """Returns <name> says woof!"""
        # TODO
        pass

    def teach_trick(self, trick_name):
        """add trick_name to the ticks list"""
        # TODO
        pass

    def feed_treat(self):
        """increase treat count by 1"""
        # TODO
        pass

    def doggie_deets(self):
        print("Name:", self.name)
        print("Weight:", self.weight)
        print("Treats in Belly:", self.treat_count)
        print("Tricks:")
        for trick in self.tricks:
            print(trick)


if __name__ == "__main__":
    fido = Dog()
    print(fido)
    fido.doggie_deets()
    fido.teach_trick("Sit")
    fido.teach_trick("Shake")
    fido.feed_treat()
    fido.doggie_deets()

    lassie = Dog("Lassie", 40)
    print(lassie)
    print(lassie)
    lassie.doggie_deets()
    lassie.teach_trick("Rescue")
    for i in range(20):
        lassie.feed_treat()
    lassie.doggie_deets()