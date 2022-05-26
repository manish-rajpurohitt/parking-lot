from Driver import Driver


class Vehicle(Driver):
    def __init__(self, licenseNumber, driverAge) -> None:
        Driver.__init__(self, driverAge)
        self.licenseNumber = licenseNumber
