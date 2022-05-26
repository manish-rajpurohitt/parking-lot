class ParkingLot:
    def __init__(self) -> None:
        self.totalSlots = 0
        self.totalSlotsOccupied = 0

    def createParkingLot(self, numOfSlots):
        self.slots = [-1] * numOfSlots
        self.totalSlots = numOfSlots
        return self.totalSlots

    def getSlotNumbersWithDriverAge(self, driverAge):
        slotsWithDriverAge = []
        for i in range(len(self.slots)):
            if(self.slots[i] == -1):
                continue
            if(self.slots[i].driverAge == driverAge):
                slotsWithDriverAge.append(i + 1)
        return slotsWithDriverAge

    def getSlotNumberWithRegisteredNumber(self, licenseNumber):
        for i in range(0, len(self.slots)):
            if(self.slots[i] == -1):
                continue
            if(self.slots[i].licenseNumber == licenseNumber):
                return i+1

    def parkVehicle(self, vehicle):
        if(self.totalSlotsOccupied < self.totalSlots):
            slotIndex = 0
            for i in range(len(self.slots)):
                if(self.slots[i] == -1):
                    slotIndex = i
                    break
            self.slots[slotIndex] = vehicle
            self.totalSlotsOccupied = self.totalSlotsOccupied + 1
            return slotIndex + 1

    def leave(self, slotId):
        if self.totalSlotsOccupied > 0 and self.slots[slotId-1] != -1:
            licenseNumber = self.slots[slotId-1].licenseNumber
            driverAge = self.slots[slotId-1].driverAge
            self.slots[slotId-1] = -1
            self.totalSlotsOccupied = self.totalSlotsOccupied - 1
            return [licenseNumber, driverAge]
        else:
            return False

    def getLicenseNumberWithDriverAge(self, driverAge):
        licenseNumbersWithDriverAge = []
        for i in range(len(self.slots)):
            if(self.slots[i] == -1):
                continue
            if(self.slots[i].driverAge == driverAge):
                licenseNumbersWithDriverAge.append(self.slots[i].licenseNumber)
        return licenseNumbersWithDriverAge
