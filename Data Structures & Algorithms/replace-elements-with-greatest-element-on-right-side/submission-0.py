class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_num = -1
            for j in range(i + 1, len(arr)): 
                if arr[j] > max_num : 
                    max_num = arr[j] 
            arr[i] = max_num
            
        return arr
            