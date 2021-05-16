from typing import *

# 144 ms, faster than 17.38% of Python3 online submissions for Design Parking System
# 14.7 MB, less than 81.11% of Python3 online submissions for Design Parking System.
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.car_number = {1:big, 2:medium, 3:small}

    def addCar(self, carType: int) -> bool:
        self.car_number[carType] -= 1
        if self.car_number[carType] >= 0 :
            return True
        else:
            return False

# 136 ms, faster than 70.01% of Python3 online submissions for Design Parking System.
# 14.9 MB, less than 23.64% of Python3 online submissions for Design Parking System.
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.car_number = {1:big, 2:medium, 3:small}

    def addCar(self, carType: int) -> bool:
        self.car_number[carType] -= 1
        if self.car_number[carType] >= 0 :
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
if __name__ == "__main__":
    obj = ParkingSystem(1, 1, 0)
    print( obj.addCar(1) )
    print( obj.addCar(2) )
    print( obj.addCar(3) )
    print( obj.addCar(1) )