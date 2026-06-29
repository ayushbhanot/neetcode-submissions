class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for course in range(numCourses):
            preMap[course] = []
        for [course, required] in prerequisites:
            preMap[course].append(required)
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True

            visit.add(course)
            for required in preMap[course]:
                if not dfs(required):
                    return False
            visit.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            