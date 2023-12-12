class Service:
    def __init__(self, repo):
        self._repo = repo

    @property
    def repo(self):
        return self._repo
    
    def sortByBatteryWithGivenString(self, search_string):
        return sorted([activity for activity in self.repo.activities if search_string in activity.description], key=lambda x: x.battery)

    def finalPositions(self, activity, starting_position):
        movement_cost = activity.battery // 10
        halt_bonus = activity.battery // 5

        current_position = list(map(int, starting_position))
        current_battery = int(activity.battery)

        for instruction in activity.instructions:
            if instruction == "halt":
                current_battery += halt_bonus
            elif instruction in ["up", "down", "right", "left"]:
                if current_battery - movement_cost > 0:
                    current_battery -= movement_cost
                    match instruction:
                        case "up":
                            current_position[1] += 1
                        case "down":
                            current_position[1] -= 1
                        case "left":
                            current_position[0] -= 1
                        case "right":
                            current_position[0] += 1
            else:
                pass
        return current_position, current_battery