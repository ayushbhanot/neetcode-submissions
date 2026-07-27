class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)): #O(n) time
            cars.append([position[i], speed[i]]) #O(n) space

        cars.sort(reverse=True) #O(nlogn) time and O(n) space due to Python's Timsort

        prevTime = (target - cars[0][0]) / cars[0][1]
        fleet = 1
        for i in range(1, len(cars)): #O(n) time
            distance = target - cars[i][0]
            time = distance / cars[i][1]
            if time > prevTime:
                fleet += 1
                prevTime = time
            
        return fleet