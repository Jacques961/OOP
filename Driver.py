from DeliveryItem import DeliveryItem
from Envelope import Envelope
from Package import Package
from typing import List

class Driver:
    def __init__(self, __name: str = None, __zone: list = (10000, 50000), __deliveries: list = None, __carRegistrationNumber: str = None, 
                 __maxWeight: float = 500.0, __maxVolume: float = 50.0):
        self.setDriver(__name, __zone, __deliveries, __carRegistrationNumber, __maxWeight, __maxVolume, 0.0, 0.0)
        
    def setDriver(self, __name: str = None, __zone: list = (10000, 50000), __deliveries: list = None, __carRegistrationNumber: str = None, 
                  __maxWeight: float = 500.0, __maxVolume: float = 50.0, __currentWeight: float = 0.0, __currentVolume: float = 0.0):
        self.setName(__name)
        self.setZone(__zone)
        self.setDeliveries(__deliveries)
        self.setCarRegistrationNumber(__carRegistrationNumber)
        self.setMaxWeight(__maxWeight)
        self.setMaxVolume(__maxVolume)
        self.setCurentWeight(__currentWeight)
        self.setCurentVolume(__currentVolume)
        
    def setName(self, __name: str):
        if __name is None or len(__name) == 0:
            self.__name = None
        self.__name = __name
    
    def setZone(self, __zone: list):
        if len(__zone) != 2 or __zone[0] > __zone[1]:
            self.__zone = [10000, 50000]    
        self.__zone = __zone
        
    def setDeliveries(self, __deliveries: List[DeliveryItem]):
        if not hasattr(self, '__deliveries'):
            self.__deliveries = []
        
        if __deliveries is None:
            print("Deliveries list is None. Not Assigned")
            return
            
        # if self.__deliveries() is None:
        #     self.__deliveries = [] # this will cause error 
            
        for item in __deliveries:
            if isinstance(item, DeliveryItem):
                self.assignDelivery(item)
            else:
                raise TypeError("All items must be of type DeliveryItem")
    
    def assignDelivery(self, delivery: DeliveryItem):
        if delivery is None:
            print("Delivery item is None. Not Assigned")
            return False
        
        # check for the zone
        if (delivery.getReceiverPostalCode() < self.getZone()[0] or
            delivery.getReceiverPostalCode() > self.getZone()[1]):
            print("Zone is not of driver responsibility")
            return False
        
        # check for the weight and volume
        if isinstance(delivery, Envelope):
            if delivery.getSize() is None:
                print("Envelope is Empty. Not Delivered")
                return False
            self.__deliveries.append(delivery)
            delivery.setStatus('A')
            print("Envelope is Assigned")
            return True
                
        if isinstance(delivery, Package):
            if ((delivery.getVolume() + self.getCurentVolume()) > self.getMaxVolume() 
                or (delivery.getWeight() + self.getCurentWeight()) > self.getMaxWeight()):
                print("Package is too heavy or too big. Not Delivered")
                return False
            self.__deliveries.append(delivery)
            self.setCurentWeight(delivery.getWeight() + self.getCurentWeight())
            self.setCurentVolume(delivery.getVolume() + self.getCurentVolume())
            delivery.setStatus('A')
            print("Package is Assigned")
            return True
    
    def accomplishedDelivery(self, deliveryNb: int):
        if deliveryNb < 1000:
            print ("Invalid delivery number")
            return False
        
        for item in self.getDeliveries():
            if item.getSerialNumber() == deliveryNb:
                if isinstance(item, Envelope):
                    item.setStatus('D')
                    self.__deliveries.remove(item)
                    print("Envelope is Delivered")
                    return True
                if isinstance(item, Package):
                    item.setStatus('D')
                    self.__deliveries.remove(item)
                    self.setCurentWeight(self.getCurentWeight() - item.getWeight())
                    self.setCurentVolume(self.getCurentVolume() - item.getVolume())
                    print("Package is Delivered")
                    return True
        print("Delivery not found")
        return False
                
    def setCarRegistrationNumber(self, __carRegistrationNumber: str):
        if __carRegistrationNumber is None or len(__carRegistrationNumber) == 0:
            self.__carRegistrationNumber = None
        self.__carRegistrationNumber = __carRegistrationNumber
    
    def setMaxWeight(self, __maxWeight: float):
        if __maxWeight <= 0:
            self.__maxWeight = 500.0
        self.__maxWeight = __maxWeight
    
    def setMaxVolume(self, __maxVolume: float):
        if __maxVolume <= 0:
            self.__maxVolume = 50.0
        self.__maxVolume = __maxVolume
    
    def setCurentWeight(self, __currentWeight: float):
        if __currentWeight < 0:
            self.__currentWeight = 0.0
        self.__currentWeight = __currentWeight
    
    def setCurentVolume(self, __currentVolume: float):
        if __currentVolume < 0:
            self.__currentVolume = 0.0
        self.__currentVolume = __currentVolume
    
    def getName(self):
        return self.__name
    
    def getZone(self):
        return self.__zone
    
    def getDeliveries(self):
        return self.__deliveries
    
    def getCarRegistrationNumber(self):
        return self.__carRegistrationNumber
    
    def getMaxWeight(self):
        return self.__maxWeight
    
    def getMaxVolume(self):
        return self.__maxVolume
    
    def getCurentWeight(self):
        return self.__currentWeight
    
    def getCurentVolume(self):
        return self.__currentVolume
    
    def __repr__(self):
        return (self.getName() + '\nActive Zone: ' + (str)(self.getZone()) 
                + '\nCar: ' + (str)(self.getCarRegistrationNumber()) + '\nMax Weight: ' + (str)(self.getMaxWeight())
                + ' - Max Volume: ' + (str)(self.getMaxVolume()))
    