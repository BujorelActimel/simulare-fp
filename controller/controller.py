from utilities import Utility

class Controller:
    def __init__(self, service):
        self._servcie = service
        self._utility = Utility()

    @property
    def service(self):
        return self._servcie
    
    @property
    def utility(self):
        return self._utility

    def cerinta1(self, search_string):
        results = self.service.sortByBatteryWithGivenString(search_string)

        if results:
            for result in results:
                print(result)
            self.utility.enter()
        else:
            self.utility.enter("Niciun Rezultat")

    def cerinta2(self, starting_position):
        for activity in self.service.repo.activities:
            final_position, final_battery = self.service.finalPositions(activity, starting_position)
            print(f"{activity.id_}: <{final_position[0]}, {final_position[1]}>, {final_battery}")
        self.utility.enter()
