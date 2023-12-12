class Utility:
    def enter(self, msg=""):
        input(f"{msg}\nPress Enter to continue")

    def get_option(self):
        while True:
            try:
                option = int(input("Alege o optiune: "))
                assert option in [1, 2, 3]
                return option
            except (ValueError, AssertionError):
                print("Optiune invalida, incearca 1, 2 sau 3")

    def get_pos(self):
        while True:
            try:
                x = int(input("X: "))
                y = int(input("Y: "))
            except ValueError:
                print("Not a number")
            else:
                return [x, y]