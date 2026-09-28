class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) < 1 or len(nums) > 100000:
            return None
        
        max_consecutive_ones = counter = 0
        
        for i in range( len(nums)): 
            if nums[i] == 1:
                counter += 1
       
            if counter > max_consecutive_ones: 
                max_consecutive_ones = counter 
                
            if nums[i] == 0:
                counter = 0 
            

        return max_consecutive_ones
