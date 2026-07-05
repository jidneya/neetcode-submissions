class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Table = {}
        s2Table = {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1Table[s1[i]] = s1Table.get(s1[i], 0) + 1
            s2Table[s2[i]] = s2Table.get(s2[i], 0) + 1

        if s1Table == s2Table:
            return True

        l = 0
        for i in range(len(s1), len(s2)):
            s2Table[s2[i]] = s2Table.get(s2[i], 0) + 1
            s2Table[s2[l]] -= 1
            if s2Table[s2[l]] == 0:
                del s2Table[s2[l]]
            l+=1
            if s2Table == s1Table:
                return True
        return False         