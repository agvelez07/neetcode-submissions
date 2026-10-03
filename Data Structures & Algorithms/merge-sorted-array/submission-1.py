class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        temp = nums1[:m]
        i = j = k = 0
         
        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1[k] = temp[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1
        
        while i < m:    
            nums1[k] = temp[i]
            k += 1
            i += 1
        while j < n: 
            nums1[k] = nums2[j]
            k += 1
            j += 1