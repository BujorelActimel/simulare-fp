import os
from utilities import Utility
from repo import Repo
from service import Service
from controller import Controller

class App:
    def __init__(self):
        self._utility = Utility()
        self._repo = Repo("data/activities.txt")
        self._service = Service(self.repo)
        self._controller = Controller(self.service)

    @property
    def utility(self):
        return self._utility

    @property
    def repo(self):
        return self._repo    
    
    @property
    def service(self):
        return self._service

    @property
    def controller(self):
        return self._controller

    def menu(self):
        print("""Meniu:
        1 - Afiseaza activitati dupa baterie
        2 - Pozitie si nivel baterie final pentru fiecare activitate
        3 - Exit
        """)

    def run(self):
        while True:
            os.system("cls")
            self.menu()
            option = self.utility.get_option()

            if option == 1:
                word = input("Cuvant: ")
                self.controller.cerinta1(word)

            if option == 2:
                starting_position = self.utility.get_pos()
                self.controller.cerinta2(starting_position)

            if option == 3:
                exit()
    

if __name__ == "__main__":
    app = App()
    app.run()
