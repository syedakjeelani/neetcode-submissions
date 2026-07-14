class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleet, PrevTime = 0, 0
        for position, speed in reversed(cars):
            time = (target - position) / speed
            if PrevTime < time:
                fleet += 1
                PrevTime = time
        return fleet
        