from abc import ABCMeta, abstractmethod

class Passenger(metaclass=ABCMeta):
    """ Return a '''Passenger''' object with currentFloor and wantedFloor """

    currentFloor = 0
    wantedFloor = 0
    elevator = None
    
    def __init__(self,currentFloor,wantedFloor):
        """Constructor Passenger with Parameter @param currentFloor @param wantedFloor """
        self.currentFloor = currentFloor
        self.wantedFloor = wantedFloor

    def setElevator(self,elevator):
        """set elevator @param elevator"""
        self.elevator = elevator

    def getElevator(self):
        """get elevator """
        return self.elevator

    def setCurrentFloor(self, currentFloor):
        """set passenger current floor @param currentFloor"""
        self.currentFloor = currentFloor

    def getCurrentFloor(self):
        """get current floor """
        return self.currentFloor

    def setWantedFloor(self, wantedFloor):
        """set wanted floor @param wantedFloor """
        self.wantedFloor = wantedFloor

    def getWantedFloor(self):
        """get wanted floor """
        return self.wantedFloor

    def isInTheElevator(self):
        """is passenger in the elevator"""
        if self.elevator != None:
            return True
        else:
            return False
    

    def isArrived(self):
        """is passenger arrive"""
        if self.currentFloor == self.wantedFloor and not self.isInTheElevator():
            return True
        else:
            return False

    def isWaitingAtFloor(self,floor):
        """is passenger waiting at floor @param floor"""
        if not self.isArrived() and not self.isInTheElevator() and self.currentFloor == floor:
            return True
        else:
            return False

    def isArrivedAtFloor(self,floor):
        """is passenger arrive at floor @param floor"""
        if self.isArrived() and self.currentFloor == floor:
            return True
        else:
            return False        
    

    
    @abstractmethod
    def getTotalMass(self):
        """abstract method get total math """
        pass

    @abstractmethod
    def getPersonCount(self):
        """abstract method get person count"""
        pass

    @abstractmethod
    def canEnterElevator(self,elevator):
        """abstract method get enter elevator """
        pass

class Person(Passenger):
    Male = 1
    Female = 0
    sex = None
    mass = None
    personCount = 1

    def __init__(self,sex,mass):
        """Constructor Person @param sex @param mass """
        self.sex = sex
        self.mass= mass

    def setSex(self,sex):
        """set sex @param sex """
        self.sex = sex

    def getSex(self):
        """get sex """
        return self.sex

    def setMass(self,mass):
        """set mass @param mass """
        self.mass = mass

    def getMass(self):
        """get mass"""
        return self.masss

    def getTextForSex(self):
        """get sex in string """
        if self.sex == self.Male:
            return "Male"
        elif self.sex == self.Female:
            return "Female"
        else:
            return "Unkown"
        

    def getTotalMass(self):
        """get weight in person"""
        return self.mass

    def getPersonCount(self):
        """return 1 """
        return self.personCount

    def canEnterElevator(self,elevator):
        """can person enter elevator"""
        return True


class Group(Passenger):
    persons = []

    def __init__(self,currentFloor, wantedFloor):
        """Constructor Group @param currentFloor @param wantedFloor """
        self.currentFloor = currentFloor
        self.wantedFloor = wantedFloor
        
    def __init__(self,currentFloor,wantedFloor,persons):
        """Constructor Group with Parameter @param currentFloor @param wantedFloor @param persons """
        self.currentFloor = currentFloor
        self.wantedFloor = wantedFloor
        self.persons = persons

    def setPersons(self,persons):
        """set persons @param persons """
        self.persons = persons

    def getPersons(self):
        """get persons """
        return self.persons

    def addPerson(self,person):
        """add persons in list of persons @param person """
        self.persons.append(person)

    def getTotalMass(self):
        """get total mass in group """
        summ = 0
        for person in self.persons:
            summ = summ + person.getTotalMass()
            
        return summ

    def getPersonCount(self):
        """get person count """
        summ = 0
        for person in persons:
            summ = summ + 1
        return summ

    def canEnterElevator(self,elevator):
        """can enter elevator @param elevator """
        return True
    
class Elevator:
    toTop = 1;
    toBottom = -1
    building = None
    identifier = None
    maxPersons = 7
    maxWeight = 1000
    alertWeight = 0
    currentFloor = 0
    targetFloor = 0
    currentWeight = 0
    goingToTop = True
    passengers = []
    moving = None

    def __init__(self,maxPersons):
        """Constructor Elevator  @param maxPerson """
        self.maxPersons = maxPersons
        self.constractor(maxPersons*80, maxPersons*80 - 60)

    def constractor(self, maxWeight,alertWeight):
        """method just called in contractor @param maxWeight @param alertWeight """
        self.maxWeight = maxWeight
        self.alertWeight = alertWeight
        self.currentFloor = 0
        self.goingToTop = True
        self.passengers = []
        self.moving = False
        self.targetFloor = 200000

    def setIdentifier(self,identifier):
        """set id to elevator @param id """
        self.identifier = identifier

    def getIdentifier(self):
        """get id """
        return self.identifier

    def setMaxWeight(self,maxWeight):
        """set elevator max weight @param maxWeight """
        self.maxWeight = maxWeight

    def getMaxWeight(self):
        """get max weight """
        return self.maxWeight

    def setAlertWeight(self,alertWeight):
        """set alert weight @param alertWeight"""
        self.alertWeight = alertWeight

    def setGoingToTop(self,goingToTop):
        """set goint to top or bottom """
        self.goingToTop = goingToTop

    def setMoving(self,moving):
        """set moving @param moving"""
        self.moving= moving

    def isMoving(self):
        """elevator is moving or not """
        return self.moving

    def getPassengers(self):
        """get passengers in elevator"""
        return self.passengers

    def getCurrentWeight(self):
        """get current weight in elevator """
        return self.currentWeight

    def getCurrentFloor(self):
        """get current floor """
        return self.currentFloor

    def getBuilding(self):
        """get elevator in each building """
        return self.building

    def isInAlert(self):
        """elevator is alert or not """
        if self.currentWeight > self.alertWeight:
            return True
        else:
            return False

    def atBottom(self):
        """elevator is botton or not """
        if self.currentFloor <= 0:
            return True
        else:
            return False
        
    def getStep(self):
        """get step top or bottom"""
        if self.goingToTop == True:
            return self.toTop
        else:
            return self.toBottom
    
        
    def getPassengerCount(self):
        """get passenger count in elevator"""
        summ = 0
        for passenger in passengers:
            summ = summ + 1

        return summ

    def changDirection(self):
        """Change elevator direction """
        self.goingToTop = not self.goingToTop

    def isGoingToTop():
        """is elevator going to top or to bottom """
        return self.goingToTop

    def getLastPassenger(self):
        """get last passenger in elevator """
        pas = None
        for passenger in passengers:
            pas = passenger

        return pas

    def isFull(self):
        """is full elevator or not"""
        if self.getPassengerCount() >= self.maxPersons:
            return True
        else:
            return False

    def isBlocked(self):
        """elevator is stop or not boolean"""
        if self.currentWeight >= maxWeight:
            return True
        else:
            return False

    def setToNextFloor(self):
        """set to next floor elevator and passenger inside it """
        self.currentFloor = self.currentFloor + self.getStep()
        for passenger in self.passengers:
            passenger.setCurrentFloor(self.currentFloor)

    def addTocurrentWeight(self,mass):
        """add weight to elevator @param mass """
        self.currentWeight  = self.currentWeight + mass

    def removeFromCurrentWeight(self,mass):
        """reduce weight from current weight in elevator @param mass """
        self.currentWeight  = self.currentWeight - mass

    def willBeBlockedWithThisMass(self, mass):
        """ if add weight will be block @param mass"""
        summ = 0
        summ = self.currentWeight + mass
        if summ >= self.maxWeight:
            return summ

    def setTargetFloor(self,floor):
        """set target floor @param floor """
        self.targetFloor = floor
        if self.targetFloor < self.getCurrentFloor():
            self.setGoingToTop(False)
        else:
            self.setGoingToTop(True)

    def getTargetFloor(self):
        """get target floor """
        return self.targetFloor

    def takePassenger(self, passenger):
        """elevator take passenger """
        if self.willBeBlockedWithThisMass(passenger.getTotalMass()) == True:
            return False
        else:
            self.passengers.append(passenger)
            self.addTocurrentWeight(passenger.getTotalMass())
            passenger.setElevator(self)
            return True

    def releasePassenger(self,passenger):
        """elevator release passenger"""
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            self.removeFromCurrentWeight(passenger.getTotalMass())
            passenger.setElevator(None)
            return True
        else:
            return False

    def releaseAllArrivedPassengers(self):
        """Constructor Passenger with Parameter @param currentFloor @param wantedFloor """
        for i in range(0,self.getPassengerCount(),1):
            if self.passengers[i].getWantedFloor() == self.getCurrentFloor():
                self.releasePassenger(passengers[i])
    

class Building:

    elevators = []
    passengers =[]
    floorCount = None

    def __init__(self,floorCount,elevators,passengers):
        """Constructor Building @param elevators @param passengers  """
        self.floorCount = floorCount
        self.elevators = elevators
        self.passengers = passengers

    def setElevator(self , elevators):
        """set elevator @param elevators """
        self.elevators = elevators

    def getElevators(self):
        """get elevator """
        return self.elevators

    def setPassengers(self , passengers):
        """set passenger @param passengers"""
        self.passengers = passengers

    def getPassengers(self):
        """get passengers """
        return self.passengers

    def setFloorCount(self, floorCount):
        """set floor count @param floorCount"""
        self.floorCount = floorCount

    def getFloorCount(self):
        """get floor count """
        return self.floorCount

    def getElevatorCount(self):
        """get elevator count"""
        summ = 0
        for elevator in elevators:
            summ = summ + 1

        return summ

    def getFloorCountWithGround(self):
        """get floor count with ground """
        return self.floorCount + 1

    def getElevatorAtFloor(self, floor):
        """ get elevator at floor @param floor"""
        for elevator in elevators:
            if elevator.getCurrentFloor() == floor:
                return elevator
        return None

    def getWaitingPassengersAtFloor(self,floor):
        """get waiting passenger at floor  @param floor """
        retList = []

        for passenger in self.passengers :
            if passenger.isWaitingAtFloor(floor):
                retList.append(passenger)

        return retList

    def getWaitingPersonsCountAtFloor(self, floor):
        """get waiting persons count at floor @param wantedFloor """
        summ = 0
        for passenger in self.getWaitingPassengersAtFloor(floor):
            summ = summ + passenger.getPersonCount()

        return summ

    def allPassengerAreArrived(self):
        """if all passenger arrive """
        for passenger in self.passengers:
            if not passenger.isArrived() == True:
                return False

        return True

    def getArrivedPassengersAtFloor(self ,floor):
        """get arrive assenger at floor @param floor """
        retList = []
        for passenger in self.passengers:
            if passenger.isArrivedAtFloor(floor) == True:
                retList.append(passenger)

        return retList

    def getCountPassengerArrivedAtFloor(self,floor):
        """get count passenger arrive at floor @param wantedFloor """
        summ = 0
        for passenger in self.passengers:
            if passenger.isArrivedAtFloor(floor) == True:
                summ = summ + passenger.getPersonCount()

        return summ

    def getWaitingPersonsCount(self):
        """get waiting person count in building """
        summ = 0
        for passenger in self.passengers:
            if not passenger.isArrived() and not passenger.isInTheElevator():
                summ = summ + passenger.getPersonCount()

        return summ

    def getMaximumWaitingFloor(self):
        """get maximum floor that person is wait its """
        maxCrowdedFloor = 0
        numberOfPeople = 0

        i = 0
        while i < self.floorCount:
            if self.getWaitingPersonsCountAtFloor(i) > numberOfPeople:
                numberOfPeople = self.getWaitingPersonsCountAtFloor(i)
                maxCrowdedFloor = i   
            i = i + 1

        return maxCrowdedFloor

        
        
        
        
                
            
        

    
        
        

    
                

    
            
            
        

    
            
        
        

    
        
            
            
        

    
        
                
            
            

        

    

    
    

    

    

    

    

    
        
    
    
    

    
            
            
            
            

    
    
            
            
            
            
        
        

    

    
        
            
    

        

    
            

    
        

    

    


    

    

    
        
        
        
        
        

    

    

    

    
        
        
    
        
    
    

