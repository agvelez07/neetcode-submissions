class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        lis = []

        def dfs(i):
            if i >= len(nums):
                res.append(lis.copy())
                return

            lis.append(nums[i])
            dfs(i + 1)

            lis.pop()
            dfs(i + 1)

        dfs(0)
        return res
 