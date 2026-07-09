import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def can_finish(speed: int) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / speed)
            return total_hours <= h

        while l <= r:
            mid = (l + r) // 2
            
            if can_finish(mid):
                res = mid      
                r = mid - 1    
            else:
                l = mid + 1    
                
        return res

        