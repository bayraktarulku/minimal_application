class ConsoleMenu:
    def __init__(self, title, items: dict):
        self.items = items
        self.title = title
        self.back_button = False

    def __display(self):
        print("\n")
        print(self.title)
        i = 1
        for key in self.items:
            print(str(i) + ") " + str(key))
            i += 1
        print("{}) {}".format(str(i), "back" if self.back_button else "exit"))

    def execute(self):
        while True:
            self.__display()

            try:
                argument = int(input("run: "))
            except (TypeError, ValueError):
                print("Error: Invalid input type")
                continue
            except KeyboardInterrupt:
                break

            if argument not in range(1, len(self.items) + 2):
                print("Error: No such item in menu")
                continue

            if argument == len(self.items) + 1:
                break

            try:
                item = list(self.items.values())[argument - 1]
                item()

            except Exception:
                print(
                    "Error: Failed to run item '{}'".format(
                        list(self.items.keys())[argument - 1]
                    )
                )
