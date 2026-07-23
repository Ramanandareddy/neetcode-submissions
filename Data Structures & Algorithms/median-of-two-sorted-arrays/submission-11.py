from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        
        l1, r1 = 0, n1 - 1
        
        while True:
            m1 = (l1 + r1) // 2
            m2 = (total // 2) - m1 - 2
            
            amin1 = nums1[m1] if m1 >= 0 else float('-inf')
            amax1 = nums1[m1 + 1] if (m1 + 1) < n1 else float('inf')
            
            bmin2 = nums2[m2] if m2 >= 0 else float('-inf')
            bmax2 = nums2[m2 + 1] if (m2 + 1) < n2 else float('inf')
            
            if amin1 <= bmax2 and bmin2 <= amax1:
                if total % 2:
                    return min(amax1, bmax2)
                return (max(amin1, bmin2) + min(amax1, bmax2)) / 2
            
            elif amin1 > bmax2:
                r1 = m1 - 1
            else:
                l1 = m1 + 1