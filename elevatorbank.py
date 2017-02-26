
from elevator import Elevator, ElevatorState

class ElevatorBank:
    def __init__(self, num_elevator, min_level, max_level):
        self.num_elevator = num_elevator
        self.elevators = [Elevator(i, min_level, max_level) for i in range(self.num_elevator)]

    def startElevator(self, index):
        if index < 0 or index > self.num_elevator:
            raise ValueError
        
        self.elevators[index].startOperation()

    def stopElevator(self, index):
        if index < 0 or index > self.num_elevator:
            raise ValueError

        self.elevators[index].stopOperation()

    def setRequest(self, level):
        index = self.selectElevator(level)
        self.elevators[index].addRequest(level)

    def selectElevator(self, level):
        selectedIndex = 0
        for i in range(1, self.num_elevator):
            if self.isBetterCandidate(selectedIndex, i, level):
                selectedIndex = i

        return selectedIndex

    def isBetterCandidate(self, current, other, level):
        return self.calculateScore(current, level) > self.calculateScore(other, level)

    def calculateScore(self, index, level):
        current_state = self.elevators[index].getState()
        current_level = self.elevators[index].getLevel()
        
        if current_state == ElevatorState.STAND:
            return abs(current_level - level)

        if current_state == ElevatorState.UP and current_level < level:
            return level - current_level

        if current_state == ElevatorState.DOWN and current_level > level:
            return current_level - level

        return float('inf')

