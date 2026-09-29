class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0] *(len(nums) * 2) #Create array 'ans' with double size of received array 'nums'
        #Traverse throgh nums array
        for i in range(len(nums)):
            ans[i] = ans[i + len(nums)] = nums[i] #value set to the nums(index + length) and nums(index) position  
        return ans
