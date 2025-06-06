import datetime

class DeliveryItem:

    __serialGenerator = 999 # Private Static Variable
    
    # class methods
    @classmethod
    # prvt since the serial number is not accessed outside the class, this method used below in the setSerialData()
    def __get_next_serial(cls):
        cls.__serialGenerator += 1
        return cls.__serialGenerator
    
    
    # instance methods   
    def __init__(self, __senderName: str = None, __receiverName: str = None, __senderPostalCode: int = 10000, 
                 __receiverPostalCode: int = 10000, __cost: float = 2.0 , __insurance: bool = False):
        self.setDeliveryItem(__senderName, __receiverName, __senderPostalCode, __receiverPostalCode, __cost, __insurance)
    
    def setDeliveryItem(self, __senderName: str = None, __receiverName: str = None, __senderPostalCode: int = 10000, 
                 __receiverPostalCode: int = 10000, __cost: float = 2.0 , __insurance: bool = False):
        self.setSenderName(__senderName)
        self.setReceiverName(__receiverName)
        self.setReceiverPostalCode(__receiverPostalCode)
        self.setSenderPostalCode(__senderPostalCode)
        self.setCost(__cost)
        self.setInsurance(__insurance)
        self.setSerialData()
    
    def setSenderName(self, __senderName: str):
        self.__senderName = __senderName
    
    def setReceiverName(self, __receiverName: str):
        self.__receiverName = __receiverName
    
    def setSenderPostalCode(self, __senderPostalCode: int):
        if __senderPostalCode < 0:
            self.__senderPostalCode = 10000
        self.__senderPostalCode = __senderPostalCode
    
    def setReceiverPostalCode(self, __receiverPostalCode: int):
        if __receiverPostalCode < 0:
            self.__receiverPostalCode = 10000
        self.__receiverPostalCode = __receiverPostalCode
        
    def setCost(self, __cost: float):
        if __cost < 0:
            self.__cost = 2.0
        self.__cost = __cost
    
    def setInsurance(self, __insurance: bool):
        self.__insurance = __insurance
    
    def setStatus(self, __status: str):
        if __status not in ['A', 'D', 'R']:
            self.__status = 'R'
        self.__status = __status
    
    def setSerialData(self):
        self.date = datetime.datetime.today()
        self.__serialNumber = DeliveryItem.__get_next_serial()
        self.setStatus(self.getStatus()[0]) # since the status may change
    
    def getSerialNumber(self):
        return self.__serialNumber
    
    def getSenderName(self):
        return self.__senderName
    
    def getReceiverName(self):
        return self.__receiverName
    
    def getSenderPostalCode(self):
        return self.__senderPostalCode
    
    def getReceiverPostalCode(self):
        return self.__receiverPostalCode
    
    def getCost(self):
        return self.__cost
    
    def getInsurance(self):
        return self.__insurance
    
    def getStatus(self):
        if self.__status == 'A':
            return 'Assigned'
        elif self.__status == 'D':
            return 'Delivered'
        else:
            return 'Received'
    
    def getDate(self):
        return self.date
    
    def hasInsurance(DeliveryItem):
        return DeliveryItem.__insurance
    
    def addInsurance(self):
        if not DeliveryItem.hasInsurance(self):
            self.setInsurance(True)
            self.setCost(self.__cost + 3)
    
    def cancelInsurance(self):
        if DeliveryItem.hasInsurance(self):
            self.setInsurance(False)
            self.setCost(self.__cost - 3)
            
    def __repr__(self): # like the toString method in JAVA
        
        insurance = self.getInsurance()
        
        if insurance:
            insurance = 'With Insurance'
        else:
            insurance = 'Without Insurance'
            
        return ((str)(self.getSerialNumber()) + ' - ' + (str)(self.getDate())
        + '\nSender: ' + (str)(self.getSenderName()) + ' - ' + (str)(self.getSenderPostalCode()) 
        +'\nReceiver: ' + (str)(self.getReceiverName()) + ' - ' + (str)(self.getReceiverPostalCode())
        + '\n' + (str)(insurance) + '\nStatus: ' + (str)(self.getStatus()))