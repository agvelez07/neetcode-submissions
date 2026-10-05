class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count = [0,0,0]

        for n in nums:
            count[n] += 1

        i = 0

        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1
