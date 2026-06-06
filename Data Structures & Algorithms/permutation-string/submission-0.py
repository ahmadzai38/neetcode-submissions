class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        count1 = {}
        
        count2 = {}
        l = 0
        for r in range(len(s1)):
            if s1[r] not in count1:
                count1[s1[r]] = 0
            count1[s1[r]] += 1
        for j in range(len(s2)):
            if s2[j] not in count2:
                count2[s2[j]] = 0
            count2[s2[j]] += 1
            while (j-l + 1 > len(s1)):
                count2[s2[l]] -=1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l +=1
            if count1 == count2:
                return True
        return False