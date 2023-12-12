from domain import Activity

class Repo:
    def __init__(self, file_name):
        self._file_name = file_name
        self._activities = self.loadData()

    @property
    def file_name(self):
        return self._file_name

    @property
    def activities(self):
        return self._activities

    def loadData(self):
        data = []
        with open(self.file_name, "r") as f:
            robot_activities = f.readlines()

            max_id = 0

            for activity in robot_activities[1:]:
                id_, battery, description, instructions = activity.strip().split(";")
                instructions = list(instructions.strip().split(","))
                id_ = int(id_)
                battery = int(battery)

                max_id = max(id_, max_id)

                data.append(Activity(battery, description, instructions, id_=id_))

            Activity.id_counter = max_id + 1
        return data
