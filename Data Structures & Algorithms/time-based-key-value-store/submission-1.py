class TimeMap:
    
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        nums = self.map[key]
        l, r = 0, len(nums)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if nums[mid][1] == timestamp:
                return nums[mid][0]
            elif nums[mid][1] < timestamp:
                l = mid + 1
                res = nums[mid][0]
            else:
                r = mid - 1
        return res

        
