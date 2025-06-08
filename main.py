from Envelope import Envelope
from DeliveryItem import DeliveryItem
from Package import Package
from Driver import Driver

def main():
    # create drivers
    # create envelopes
    # create packages
    # assign deliveries to drivers
    # accomplish deliveries
    # print the results at each step
    # try some error cases
    
    envelopes = []
    packages = []
    drivers = []
    
    # create drivers
    driver1 = Driver('alik', [10000, 40000], [], '112233', 500.0, 5000.0)
    driver2 = Driver('vladimir', [40000, 80000], [], '445566', 600.0, 6000.0)
    driver3 = Driver('raluca', [80000, 120000], [], '778899', 700.0, 7000.0)
    drivers.append(driver1)
    drivers.append(driver2)
    drivers.append(driver3)
    
    # create envelopes
    envelope1 = Envelope('jacques', 'younis', 90000, 36554, False, 'A2')
    envelope2 = Envelope('jacques', 'ayman', 23629, 16254, False, 'A6')
    envelope3 = Envelope('ayman', 'younis', 71721, 57459, True, 'A7')
    envelope4 = Envelope('mohammad', 'jacques', 21113, 78469, True, 'A9')
    envelope5 = Envelope('younis', 'wiktor', 99797, 108590, False, '4 square')
    envelope6 = Envelope('jacques', 'polina', 98789, 119980, True, '5 square')
    envelopes.append(envelope1)
    envelopes.append(envelope2)
    envelopes.append(envelope3)
    envelopes.append(envelope4)
    envelopes.append(envelope5)
    envelopes.append(envelope6)
    
    # create packages
    package1 = Package('jacques', 'younis', 10000, 35555, False, 2, 2, 2, 1)
    package2 = Package('jacques', 'ayman', 20000, 22555, False, 3, 3, 3, 2)
    package3 = Package('ayman', 'younis', 10000, 55556, True, 4, 4, 4, 3)
    package4 = Package('mohammad', 'jacques', 40000, 78989, True, 5, 5, 5, 4)
    package5 = Package('younis', 'wiktor', 80000, 104522, False, 6, 6, 6, 5)
    package6 = Package('jacques', 'polina', 50000, 112223, True, 7, 7, 7, 6)
    packages.append(package1)
    packages.append(package2)   
    packages.append(package3)
    packages.append(package4)   
    packages.append(package5)
    packages.append(package6)
  
    # assign deliveries to drivers
    driver1.setDeliveries(envelopes[:2] + packages[:2])
    driver2.setDeliveries(envelopes[2:4] + packages[2:4])
    driver3.setDeliveries(envelopes[4:] + packages[4:])
    
    # driver1.assignDelivery(envelope1)
    # driver1.assignDelivery(envelope2)
    # driver1.assignDelivery(package1)
    # driver1.assignDelivery(package2)
    # driver2.assignDelivery(envelope3)
    # driver2.assignDelivery(envelope4)
    # driver2.assignDelivery(package3)
    # driver2.assignDelivery(package4)
    # driver3.assignDelivery(envelope5)
    # driver3.assignDelivery(envelope6)
    # driver3.assignDelivery(package5)
    # driver3.assignDelivery(package6)
    
    print('\n\n\n\n')
    
    # print drivers and their deliveries
    for driver in drivers:
        print('Driver:')
        print(driver)
        print('\nDeliveries:\n')
        for delivery in driver.getDeliveries():
            print(delivery)
            print('\n')
        print('\n\n')
        
    # accomplish deliveries
    for driver in drivers:
        for delivery in driver.getDeliveries():
            driver.accomplishedDelivery(delivery.getSerialNumber())

    print('\n\n')
    
    # try to exceed the weight and volume limits
    print("Trying to assign a package that exceeds the weight and volume limits:")
    oversized_package = Package('jacques', 'younis', 100000, 30000, False, 1000.0, 1000.0, 1000.0, 9999.0)
    driver1.assignDelivery(oversized_package)
    print('\n\n')
    
    # try to assign a delivery outside the driver's zone
    print("Trying to assign a delivery outside the driver's zone:")
    out_of_zone_package = Package('jacques', 'younis', 10000, 99999, False, 0.2, 0.2, 0.2, 0.1)
    driver1.assignDelivery(out_of_zone_package)
    print('\n\n')
    
    # try to accomplish a delivery that does not exist
    print("Trying to accomplish a delivery that does not exist:")
    driver1.accomplishedDelivery(9999)
    print('\n\n')
    
    # try to accomplish a delivery with an invalid number
    print("Trying to accomplish a delivery with an invalid number:")
    driver1.accomplishedDelivery(999)  # Invalid delivery number
    print('\n\n')
    
    # for all envelopes and pacages, if no insurance add insurance to it, and if insurance remove it
    print("Adding or removing insurance for all deliveries:")
    for driver in drivers:
        for delivery in driver.getDeliveries():
            if delivery.hasInsurance() is False:
                delivery.addInsurance()
            else:
                delivery.cancelInsurance()        
    print('\n\n')
    
    # print drivers and their deliveries after insurance changes
    for driver in drivers:
        print('Driver:')
        print(driver)
        print('\nDeliveries:\n')
        for delivery in driver.getDeliveries():
            print(delivery)
            print('\n')
        print('\n\n')
        
if __name__ == "__main__":
    main()