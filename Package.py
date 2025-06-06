from DeliveryItem import DeliveryItem

class Package(DeliveryItem):
    def __init__(self, __senderName: str = None, __receiverName: str = None, __senderPostalCode: int = 10000, 
                 __receiverPostalCode: int = 10000, __cost: float = 2.0 , __insurance: bool = False,
                 __height: float = 0.2, __width: float = 0.2, __length: float = 0.2, __weight: float = 0.1):
        super().__init__(__senderName, __receiverName, __senderPostalCode, __receiverPostalCode, __cost, __insurance)
        self.setHeight(__height)
        self.setWidth(__width)
        self.setLength(__length)
        self.setWeight(__weight)
        self.setVolume()
    
    def setHeight(self, __height: float):
        if __height > 0:
            self.__height = __height
        self.__height = 0.2
    
    def setWidth(self, __width: float):
        if __width > 0:
            self.__width = __width
        self.__width = 0.2
    
    def setLength(self, __length: float):
        if __length > 0:
            self.__length = __length
        self.__length = 0.2
    def setWeight(self, __weight: float):
        if __weight > 0:
            self.__weight = __weight
        self.__weight = 0.1
        
    def getHeight(self):
        return self.__height
    
    def getWidth(self):
        return self.__width
    
    def getLength(self):
        return self.__length
    
    def getWeight(self):
        return self.__weight
    
    def setVolume(self):
        self.__volume = self.getHeight() * self.getWidth() * self.getLength()
        
    def getVolume(self):
        return self.__volume
    
    def __setCost(self):
        if self.getVolume() <= 2.0:
            self.setCost(2.0 + (self.getWeight() * 3.0))
        elif self.getVolume() <= 5.0 and self.getVolume() > 2.0:
            self.setCost(2.8 + (self.getWeight() * 3.0))
        elif self.getVolume() > 5:
            self.setCost(2.8 + (self.getWeigth() * 3.0) + ( self.getVolume() - 5.0))
            
        if self.hasInsurance():
            self.setCost(self.getCost() + 20 * self.getWeigth())

    def __repr__(self):
        return ('Package: ' + super().__repr__() + '\nDimension: ' 
                + (str)(self.getHeight()) + ' * ' + (str)(self.getWidth()) 
                + ' * ' + (str)(self.getLength()) + '\nVolume: ' + (str)(self.getVolume().__round__(2)) 
                + '\nCost: ' + (str)(self.getCost()))
    