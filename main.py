from DeliveryItem import DeliveryItem

print("Setting orders to delievery:\n")

items = list()
    
for i in range(1):
    senderName = input("Enter sender name: ")
    senderPostalCode = (int)(input("Enter sender postal code: "))
    receiverName = input("Enter receiver name: ")    
    receiverPostalCode = (int)(input("Enter receiver postal code: ")) 
    cost = (int)(input("Set item cost: "))
    insurance = input("Set item insurance: ")
    status = input("Set item delivery status: ")
    
    item = DeliveryItem(senderName, receiverName, senderPostalCode, receiverPostalCode, cost, insurance, status)
    items.append(item)
    
for i in items:
    print(i.__repr__())




    
    