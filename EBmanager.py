
import sys
import argparse
from elevatorbank import ElevatorBank

class Manager:
    def run(self, num_elevator, min_level, max_level):
        if num_elevator > 0 and min_level < max_level and min_level >= 0:
            eb = ElevatorBank(num_elevator, min_level, max_level)
            
            for i in range(num_elevator):
                eb.startElevator(i)

            while True:
                req = input(">>F: ")
            
                if req.isalpha():
                    for i in range(num_elevator):
                        eb.stopElevator(i)
                    break
            
                else:
                    eb.setRequest(int(req))

        else:
            raise ValueError


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number_of_elevator', help="Enter the number of elevators.")
    parser.add_argument('min_level', help="Enter the min level.")
    parser.add_argument('max_level', help="Enter the max level.")

    args = parser.parse_args()
    num_elevator = int(args.number_of_elevator)
    min_level = int(args.min_level)
    max_level = int(args.max_level)
    
    app = Manager()

    try:
        app.run(num_elevator, min_level, max_level)

    except Exception:
        sys.exit(0)
