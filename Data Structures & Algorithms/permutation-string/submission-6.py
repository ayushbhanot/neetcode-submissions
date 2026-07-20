class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1, countS2 = {}, {}

        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1

        sortedS1 = sorted(s1)

        for i in range(len(s2)):
            if s2[i] in s1:
                l = i - len(s1)
                r = i + len(s1)
                if 0 <= l + 1 < len(s2) and sorted(s2[l + 1 : i + 1]) == sortedS1:
                    return True
                elif 0 <= r - 1 < len(s2) and sorted(s2[i : r]) == sortedS1:
                    return True
            else:
                continue
        return False