class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        maxFreq = 0
        for num in nums:
            if count.get(num, 0)+1 > maxFreq:
                maxFreq = count.get(num, 0)+1
            count[num]= count.get(num, 0) + 1

        arr = [[0 for i in range(0)] for j in range(maxFreq)]

        for key, value in count.items():
            arr[value-1].append(key)

        result = []
        for i in arr:
            for j in i:
                result.append(j)
        return result[-k:]
        