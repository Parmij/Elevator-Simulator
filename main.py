import ElevatorSimulationModule

listOfPassengers = []
listOfElevator = []


def fillPersons(personsCount):
    for i in range(0,personsCount,1):
        print("Enter the Gender of the passenger ",(i+1), " Choose 1 for male or 0 for female")
        gender = int(input())
        print("Enter the weight of the pessanger ",(i+1), " Press Enter to skip")
        weight = input()
        if weight == "":
            weight = 80
        print("Enter the current floor for the pessanger ",(i+1))
        currentFloor = int(input())
        print("Enter the wanted floor for the pessanger ",(i+1))
        wantedFloor = int(input())
        person = ElevatorSimulation.Person(gender, weight)
        person.setCurrentFloor(currentFloor)
        person.setWantedFloor(wantedFloor)
        listOfPassengers.append(person)

def fillGroups(groupCount):
    for i in range(0,groupCount,1):
        print("Enter the number of the passengers in the group ",(i+1))
        personsCount = int(input())
        listOfPersonsForThisGroup = []      
        for j in range(0, personsCount, 1): 
            print("Enter the Gender of the passenger ",(j+1), " Choose 1 for male or 0 for female")
            gender = int(input())
            print("Enter the weight of the pessanger ",(j+1), " Press Enter to skip")
            weight = input()
            if weight == "":
                weight = 80
            person = ElevatorSimulation.Person(gender, weight)
            listOfPersonsForThisGroup.append(person)
        print("Enter the current floor for the group ",(i+1))
        currentFloor = int(input())
        print("Enter the wanted floor for the group ",(i+1))
        wantedFloor = int(input())
        group = ElevatorSimulation.Group(currentFloor, wantedFloor, listOfPersonsForThisGroup)
        listOfPassengers.append(group)

def fillElevatorInfo(elevatorCount):
    for i in range(0,elevatorCount,1):
        print ("Enter the maximun person that elevator can handle it ")
        maxPersons = int(input())
        print ("Enter the maximum weight that elevator can handle it ")
        maxWeight = int(input())
        print("Enter the weight that elevator alert ")
        alertWeight = int(input())
        elevator = ElevatorSimulation.Elevator(maxPersons)
        elevator.setMaxWeight(maxWeight)
        elevator.setAlertWeight(alertWeight)
        listOfElevator.append(elevator)
    

def printListOfPassengers():
    i = 1
    print(" This of The People and Group in the building")
    for passenger in listOfPassengers:
        if isinstance(passenger,ElevatorSimulation.Group)== True:
            print(i,": Group:  current floor is:  " ,passenger.getCurrentFloor()," target Floor is:  ", passenger.getWantedFloor())
        else:
            print(i,": Person:  current floor is:  " ,passenger.getCurrentFloor()," target Floor is:  ", passenger.getWantedFloor())
        i = i + 1
        
def makeOperation(elevtorNumber):
    option2 = "0"
    
    while option2 != "8":
        print("1: Make Elevator Direction to Top")
        print("2: Make Elevator Direction to Bottom")
        print("3: Set Target Floor")
        print("4: Take a passenger")
        print("5: Move The Elevator")
        print("6: Change Direction")
        print("7: Show Current Floor ")
        print("8: Exit ")
        option2 = input()
        if option2 == "1":
            listOfElevator[elevtorNumber].setGoingToTop(True)
        elif option2 == "2":
            listOfElevator[elevtorNumber].setGoingToTop(False)
        elif option2 == "3":
            print ("Choose the floor which u want to go to")
            choosenFloor = int(input())
            listOfElevator[elevtorNumber].setTargetFloor(choosenFloor)
        elif option2 == "4":
            printListOfPassengers()
            print("Choose one of the passenger to get on to the elevator")
            choosenPassenger = int(input())
            if listOfPassengers[choosenPassenger-1].getCurrentFloor() != listOfElevator[elevtorNumber].getCurrentFloor():
                print("The current Floor of passenger is not same the current floor of elevator")
                print("Try Again")
            else:
                listOfElevator[elevtorNumber].takePassenger(listOfPassengers[choosenPassenger-1])
        elif option2 == "5":
            listOfElevator[elevtorNumber].setToNextFloor()
        elif option2 == "6":
            listOfElevator[elevtorNumber].changDirection()
        elif option2 == "7":
            print("Elevator is in Floor ",listOfElevator[elevtorNumber].getCurrentFloor())
                    

        
        
option = "1"           
while option == "1":
    print ("Please select one of these:");
    print ("press 1 to Start");
    print ("press 2 to Exit");
    option  = input()
    if option == "1":
        print("Enter the number of floors in the building")
        floorCount = int(input())

        # Fill Individual Passengers Information
        print("Enter the number of individual passengers in the building ")
        personsCount = int(input())
        fillPersons(personsCount)

        # Fill Group Passengers Information
        print("Enter the number of group passengers in the building ")
        groupCount = int(input())
        fillGroups(groupCount)

        # Fill Elevator Information
        print("Enter the number of elevators in this building ")
        elevatorCount = int(input())
        fillElevatorInfo(elevatorCount)
        
        building = ElevatorSimulation.Building(floorCount, listOfElevator, listOfPassengers)

        # Print List of Passengers
        printListOfPassengers()

        # Show Some of Features
        print("Choose the Elevator to make operation ")
        elevtorNumber = int(input())
        makeOperation(elevtorNumber-1)

        
