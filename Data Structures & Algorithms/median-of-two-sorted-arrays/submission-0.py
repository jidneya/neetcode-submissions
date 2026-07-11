class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays( nums2, nums1)
        
        l, r = 0, n
        while l <= r:
            mid1 = (l+r)//2
            l1 = nums1[mid1 - 1] if mid1 > 0 else -float('inf')
            r1 = nums1[mid1] if mid1 < n else float('inf')

            mid2 = (n+m+1)//2 - mid1
            l2 = nums2[mid2 - 1] if mid2 > 0 else -float('inf')
            r2 = nums2[mid2] if mid2 < m else float('inf')
            
            if l1 <= r2 and l2 <= r1:
          
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            if l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1
        return 0
        