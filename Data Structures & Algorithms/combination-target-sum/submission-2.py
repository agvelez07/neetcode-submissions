class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        lis = []

        def dfs(i, trg):
            if trg == 0:
                return res.append(lis.copy())
            if i >= len(nums) or trg < 0:
                return 
            lis.append(nums[i])
            dfs(i,trg - nums[i])
            lis.pop()
            dfs(i+1,trg )
           

        dfs(0, target)
        return res
            
