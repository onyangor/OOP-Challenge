
from pet import Pet

def main():
    # Create a pet named "Fluffy"
    fluffy = Pet("Fluffy")

    # Check status
    fluffy.get_status()

    # Pet eats, plays, and sleeps
    fluffy.eat()
    fluffy.play()
    fluffy.sleep()

    # Pet learns some tricks
    fluffy.train("Sit")
    fluffy.train("Roll over")

    # Show learned tricks
    fluffy.show_tricks()

    # Final status
    fluffy.get_status()

if __name__ == "__main__":
    main()




