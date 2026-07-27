class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)): #O(n) time
            cars.append([position[i], speed[i]]) #O(n) space
        
        cars.sort(reverse = True) #O(nlogn) time and O(n) space due to Python using Timsort

        stack = []
        for i in range(len(cars)): #O(n) time
            distance = target - cars[i][0]
            speed = cars[i][1]
            time = distance / speed
            if stack and time > stack[-1]:
                stack.append(time)
            elif not stack: 
                stack.append(time)

        return len(stack)