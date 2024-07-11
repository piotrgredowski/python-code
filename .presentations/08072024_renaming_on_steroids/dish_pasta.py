class Pasta:
    def __init__(self, name: str):
        self.name = name
        self.is_delicious = True
        self.is_healthy = False

    def __repr__(self):
        is_delicious_str = "😋 delicious" if self.is_delicious else "😞 not delicious"
        is_healthy_str = "🥗 healthy" if self.is_healthy else "🍄 not healthy"
        return f"<🍝 {self.name} 🍝, is {is_delicious_str} and {is_healthy_str}>"

def get_super_funny_name():
    return "Pastarotti"

def main():
    answer = input(f"🤌 Do you want a 🍝 {get_super_funny_name().lower()} 🍝? [yes/of_course] > ")
    print()

    if answer.strip().lower() in ("yes", "of_course"):
        italian_pasta = Pasta(name=get_super_funny_name())
        print(f"🍝 {Pasta.__name__} 🍝 is ready for you!")
        print(italian_pasta)
    else:
        pasta_list = [
            Pasta(name="Spaghetti"),
            Pasta(name="Fettuccine"),
            Pasta(name="Ravioli"),
            Pasta(name="Linguine"),
        ]
        pasta_list_str = ",\n".join(f"🍝 {pasta.name}" for pasta in pasta_list)
        print(f"If you change your mind, we have these pastas for you:\n{pasta_list_str}.")

if __name__ == "__main__":
    main()
