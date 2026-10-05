class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        m = len(matrix[0]) - 1
        mid = 0
        #  10
        # 8 13 40
        while t <= b:
            mid = t + (b - t) // 2
            print(mid)
            if target < matrix[mid][0]:
                b = mid - 1 
            elif target > matrix[mid][m]:  
                t = mid + 1
            else: 
                break
        l, r = 0, m
        print('Chigou! ',matrix[mid] )
        while l <= r:
            c = l + (r - l) // 2
            if target < matrix[mid][c]:  
                r = c - 1
            elif target > matrix[mid][c]:  
                l = c + 1
            else:
                break
        if target == matrix[mid][c]:
            return True
        return False