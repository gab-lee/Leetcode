from typing import List
from collections import deque

class RideSharingSystem:

    def __init__(self):
        self.driver_queue = deque()
        self.rider_queue = deque()

    def addRider(self, riderId: int) -> None:
        self.rider_queue.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver_queue.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if not self.driver_queue or not self.rider_queue:
            return [-1,-1]
        
        matching = [self.driver_queue[0],self.rider_queue[0]]
        self.driver_queue.popleft()
        self.rider_queue.popleft()
        return matching 

    def cancelRider(self, riderId: int) -> None:
        new_queue = deque()
        removed = False

        while self.rider_queue:
            rider = self.rider_queue.popleft()
            if rider == riderId and not removed:
                removed = True   # skip exactly one
            else:
                new_queue.append(rider)

        self.rider_queue = new_queue

uber = RideSharingSystem()
uber.addRider(3)
uber.addDriver(2)
uber.addRider(1)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)