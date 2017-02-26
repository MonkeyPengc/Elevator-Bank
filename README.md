
# Elevator Bank

## Support

Please run EBmanager.py through command line with 3 specified parameters.

> python EBmanager.py --help to see more detail.

It takes a simple Interface >>F:_ to accept a valid number as level request, or any character to stop. 

The output, which is a record of elevators responsing to requests, is written to a r.log file.

## Updates

* 2017-2-25: Added major functions of system.

# Design Principles

### Entities

Elevator Bank

Elevators

### Relationship between Entities

An elevator bank has N elevators, min level, and max level.


### Behavior of Entities

Elevator bank accept requests, select an optimal elevator according to the current status and current level of elevators, and the request.

Elevator bank send the corresponding level request to the elevator. 

Elevators put the level request to a shared list with lock, response to requests, and update status.


