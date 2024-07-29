"""Design Parking System
https://leetcode.com/problems/design-parking-system
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.free_spaces = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        if self.free_spaces[carType] > 0:
            self.free_spaces[carType] -= 1
            return True
        return False


obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
