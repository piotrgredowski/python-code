class Knedlik:
    def __init__(self, name: str):
        self.name = name
        self.is_delicious = True
        self.is_healthy = False

    def __repr__(self):
        is_delicious_str = "😋 delicious" if self.is_delicious else "😞 not delicious"
        is_healthy_str = "🥗 healthy" if self.is_healthy else "🍄 not healthy"
        return f"<🥟 {self.name} 🥟, is {is_delicious_str} and {is_healthy_str}>"


def get_super_funny_name():
    return "Knedleak"


def main():
    answer = input(f"Do you want a 🥟 {get_super_funny_name().lower()} 🥟? [yes/of_course] > ")
    print()

    if answer.strip().lower() in ("yes", "of_course"):
        czech_dumpling = Knedlik(name=get_super_funny_name())
        print(f"🥟 {Knedlik.__name__} 🥟 is ready for you!")
        print(czech_dumpling)
    else:
        knedlist = [
            Knedlik(name="Houskový knedlík"),
            Knedlik(name="Bramborový knedlík"),
            Knedlik(name="Karlovarský knedlík"),
            Knedlik(name="Ovocný knedlík"),
        ]
        knedlist_str = ",\n".join(f"🥟 {knedlik.name}" for knedlik in knedlist)
        print(f"If you change your mind, we have these knedlíky for you:\n{knedlist_str}.")


if __name__ == "__main__":
    main()
