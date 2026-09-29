class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums * 2
        return ans
        #ans = [0] *(len(nums) * 2) #Create array 'ans' with double size of received array 'nums'

        #Traverse throgh nums array
        #for i in range(len(nums)):
        #    ans[i + len(nums)] = ans[i] = nums[i] #value set to the nums(index + length) and nums(index) position  
        #return ans
