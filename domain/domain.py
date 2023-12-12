class Activity:
    id_counter = 0
    def __init__(self, battery, description, instructions, id_ = None):
        self._battery = battery
        self._description = description
        self._instructions = instructions
        if id_:
            self._id = id_
        else:
            self._id = Activity.id_counter
            Activity.id_counter += 1

    def __str__(self):
        return f"{self.id_}: baterie:{self.battery} descriere:{self.description} instructiuni:{self.instructions}"

    def __repr__(self):
        return str(self)

    @property
    def battery(self):
        return self._battery

    @property
    def description(self):
        return self._description
    
    @property
    def instructions(self):
        return self._instructions

    @property
    def id_(self):
        return self._id

    @battery.setter
    def battery(self, val):
        self.battery = val