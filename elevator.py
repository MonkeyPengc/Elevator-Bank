
import threading
import logging
import time

class ElevatorState:
    STAND = 0
    UP = 1
    DOWN = 2

class Elevator(threading.Thread):
    requests = []
    LOG_FILENAME = 'r.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    
    def __init__(self, id, min_level, max_level):
        super().__init__()
        self.id = id
        self.state = ElevatorState.STAND
        self.level = min_level
        self.min_level = min_level
        self.max_level = max_level
        self.lock=threading.RLock()
        self.stopped = False
    
    def startOperation(self):
        self.start()
    
    def stopOperation(self):
        self.stopped = True
    
    def run(self):
        while not self.stopped:
            self.lock.acquire()
            if self.state == ElevatorState.UP or self.state == ElevatorState.DOWN:
                self.move()

            self.lock.release()

    def move(self):
        if self.state == ElevatorState.UP:
            if self.needStop():
                self.openDoor()
                self.updateState()
            else:
                self.level += 1

        elif self.state == ElevatorState.DOWN:
            if self.needStop():
                self.openDoor()
                self.updateState()
            else:
                self.level -= 1

    def needStop(self):
        for l in self.requests:
            if l == self.level:
                return True

        return False

    def openDoor(self):
        logging.info("Elevator " + str(self.id) + " arriving at level " + str(self.level))
        logging.info("Door open")
        time.sleep(0.33)
        logging.info("Door close")
        self.requests.remove(self.level)

    def updateState(self):
        if self.state == ElevatorState.UP:
            if not self.requests:
                self.state = ElevatorState.STAND

            else:
                if self.requests[-1] < self.level:
                    self.state = ElevatorState.DOWN

        elif self.state == ElevatorState.DOWN:
            if not self.requests:
                self.state = ElevatorState.STAND

            else:
                if self.requests[0] > self.level:
                    self.state = ElevatorState.UP

    def addRequest(self, level):
        self.lock.acquire()
        
        if level < self.min_level or level > self.max_level:
                logging.warn("Invalid request.")
                self.lock.release()
                return
        
        if not self.requests:
            self.requests.append(level)

            if level > self.level:
                logging.info("Elevator " + str(self.id) + " moving up...")
                self.state = ElevatorState.UP

            elif level < self.level:
                logging.info("Elevator " + str(self.id) + " moving down...")
                self.state = ElevatorState.DOWN

            else:
                self.openDoor()
                self.state = ElevatorState.STAND
    
        else:
            for i in range(len(self.requests)):
                if self.requests[i] == level:
                    return

                elif self.requests[i] > level:
                    self.requests.insert(i, level)

        self.lock.release()

    def getState(self):
        self.lock.acquire()
        current_state = self.state
        self.lock.release()
        return current_state

    def getLevel(self):
        self.lock.acquire()
        current_level = self.level
        self.lock.release()
        return current_level



