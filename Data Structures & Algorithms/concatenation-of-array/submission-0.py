class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0] *(len(nums) * 2) #Create array 'ans' with double size of received array 'nums'

        #Traverse throgh 
        for i in range(len(nums)):
            ans[i + len(nums)] = ans[i] = nums[i]
        return ans
