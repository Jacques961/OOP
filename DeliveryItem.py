import datetime

class DeliveryItem:

    __serialGenerator = 1000 # Private Static Variable
    __serialNumber = __serialGenerator
    
    # class methods
    @classmethod
    # prvt since the serial number is not accessed outside the class, this method used below in the setSerialData()
    def __get_next_serial(cls):
        cls.__serialGenerator += 1
        return cls.__serialNumber
    
    
    # instance methods   
    def __init__(self, senderName: str = None, receiverName: str = None, senderPostalCode: int = 10000, 
                 receiverPostalCode: int = 10000,cost: float = 2.0 , insurance: bool = False, status: str = 'R'):
        self.setDeliveryItem(senderName, receiverName, senderPostalCode, receiverPostalCode, cost, insurance, status)
    
    def setDeliveryItem(self, senderName: str = None, receiverName: str = None, senderPostalCode: int = 10000, 
                 receiverPostalCode: int = 10000,cost: float = 2.0 , insurance: bool = False, status: str = 'R'):
        self.setSenderName(senderName)
        self.setReceiverName(receiverName)
        self.setReceiverPostalCode(receiverPostalCode)
        self.setSenderPostalCode(senderPostalCode)
        self.setCost(cost)
        self.setInsurance(insurance)
        self.setStatus(status)
        self.setSerialData()
    
    def setSenderName(self, senderName: str):
        self.__senderName = senderName
    
    def setReceiverName(self, receiverName: str):
        self.__receiverName = receiverName
    
    def setSenderPostalCode(self, senderPostalCode: int):
        if senderPostalCode < 0:
            self.__senderPostalCode = 10000
        self.__senderPostalCode = senderPostalCode
    
    def setReceiverPostalCode(self, receiverPostalCode: int):
        if receiverPostalCode < 0:
            self.__receiverPostalCode = 10000
        self.__receiverPostalCode = receiverPostalCode
        
    def setCost(self, cost: float):
        if cost < 0:
            self.__cost = 2.0
        self.__cost = cost
    
    def setInsurance(self, insurance: bool):
        self.__insurance = insurance
    
    def setStatus(self, status: str):
        if status not in ['A', 'D', 'R']:
            self.__status = 'R'
        self.__status = status
    
    def setSerialData(self):
        self.date = datetime.datetime.today()
        self.__serialNumber = DeliveryItem.__get_next_serial()
    
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
            return 'Receiver'
    
    def getDate(self):
        return self.date
    
    def addInsurance(self):
        if self.getInsurance == False:
            self.setInsurance(True)
            self.setCost(self.__cost + 3)
    
    def cancelInsurance(self):
        if self.getInsurance == True:
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