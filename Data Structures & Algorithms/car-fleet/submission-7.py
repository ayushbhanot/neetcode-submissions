class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)): #O(n) time
            cars.append([position[i], speed[i]]) #O(n) space

        cars.sort(reverse=True) #O(nlogn) time and O(n) space due to Python's Timsort

        stack = [] 
        for i in range(len(cars)): #O(n) time
            distance = target - cars[i][0]
            time = distance / cars[i][1]
            if stack and time <= stack[-1]:
                continue
            stack.append(time) #O(n) space

        return len(stack)