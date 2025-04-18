class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """Reduces hunger by 3 points, but not below 0, and increases happiness by 1."""
        if self.hunger > 0:
            self.hunger -= 3
            self.happiness += 1
        else:
            self.hunger = 0
        print(f"{self.name} eats. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        """Increases energy by 5 points, but not above 10."""
        if self.energy < 10:
            self.energy = min(10, self.energy + 5)
        print(f"{self.name} sleeps. Energy: {self.energy}")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1."""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
        else:
            print(f"{self.name} is too tired to play!")
        print(f"{self.name} plays. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def train(self, trick):
        """Adds a new trick to the tricks list."""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    def show_tricks(self):
        """Prints all learned tricks."""
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        """Prints the current state of the pet."""
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print("Tricks learned:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print("No tricks learned yet.")
