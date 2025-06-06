from DeliveryItem import DeliveryItem

class Envelope(DeliveryItem):
    
    def __init__(self, __senderName: str = None, __receiverName: str = None, __senderPostalCode: int = 10000, 
                 __receiverPostalCode: int = 10000, __cost: float = 2.0 , __insurance: bool = False,
                 __size: str = None):
        super().__init__(__senderName, __receiverName, __senderPostalCode, __receiverPostalCode, __cost, __insurance)
        self.setSize(__size)
        self.__setCost()
    
    def setSize(self, __size: str):
        if __size in ["A2", "A6", "A7", "A9", "4 square", " 5 square"]:
            self.__size = __size
        self.__size = "A2"
    
    def getSize(self):
        return self.__size
    
    def __setCost(self): # review it
        if self.getSize() == "A2":
            self.setCost(2.0)
        elif self.getSize() == "A6":
            self.setCost(1.6)
        elif self.getSize() == "A7":
            self.setCost(1.5)
        elif self.getCost() == "A9":
            self.setCost(1.2)
        elif self.getSize() == "4 square":
            self.setCost(1.8)
        elif self.getSize() == "5 square":
            self.setCost(1.6)
        
        if super().hasInsurance(): # same if used self.hasInsurance()
            self.setCost(self.getCost() + 3.0)
    
    # def getCost(self): # review it no need to override it
    #     return super().getCost()

    def __repr__(self):
        return 'Envelope: ' + super().__repr__() + '\nSize: ' + (str)(self.getSize()) +'\nCost: ' + str(self.getCost())
        
         
        