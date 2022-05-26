from ParkingLot import ParkingLot
from Vehicle import Vehicle


COMMANDS = ["Create_parking_lot", "Park", "Slot_numbers_for_driver_of_age",
            "Slot_number_for_car_with_number", "Leave", "Vehicle_registration_number_for_driver_of_age"]


def main():
    lot = ParkingLot()
    file = open("input.txt", "r")
    Lines = file.readlines()
    for line in Lines:
        splittedLine = line.split(" ")
        command = splittedLine[0]

        if(command == COMMANDS[0]):
            numOfSlots = int(splittedLine[1].strip())
            lot.createParkingLot(numOfSlots)
            print("Created parking of " + str(numOfSlots) + " slots")
            continue

        elif command == COMMANDS[1]:
            licenseNumber = splittedLine[1].strip()
            driverAge = int(splittedLine[3].strip())
            vehicle = Vehicle(licenseNumber, driverAge)
            slotNo = lot.parkVehicle(vehicle)
            print("Car with vehicle registration number \"" +
                  licenseNumber+"\" has been parked at slot number", slotNo)
            continue

        elif command == COMMANDS[2]:
            driverAge = int(splittedLine[1].strip())
            slots = lot.getSlotNumbersWithDriverAge(driverAge)
            print(",".join(map(str, slots)))
            continue

        elif command == COMMANDS[3]:
            licenseNumber = splittedLine[1].strip()
            slotNumber = lot.getSlotNumberWithRegisteredNumber(licenseNumber)
            print(slotNumber)
            continue

        elif command == COMMANDS[4]:
            slotNo = int(splittedLine[1].strip())
            [licenseNumber, driverAge] = lot.leave(slotNo)
            print("Slot number " + str(slotNo) + " vacated, the car with vehicle registration number \"" + licenseNumber +
                  "\" left the space, the driver of the car was of age", driverAge)
            continue

        elif command == COMMANDS[5]:
            driverAge = int(splittedLine[1].strip())
            licenseNumbers = lot.getLicenseNumberWithDriverAge(driverAge)
            print(",".join(map(str, licenseNumbers)))

        else:
            print("Command not found. Please enter a valid commands from :", COMMANDS)


if __name__ == '__main__':
    main()
