class Solution:
    def mergeSort(self, points: List[List[int]], s, e):
        if e <= s:
            return points
 
        pivot = e
        l = s

        dist_p = (points[e][0]**2 + points[e][1] **2) 
        for i in range(s, e):
            dist_i = (points[i][0]**2) + (points[i][1] **2) 
            if dist_i < dist_p:
                temp = points[i]
                points[i] = points[l]
                points[l] = temp
                l += 1
        
        points[l], points[e] = points[e], points[l] 
        self.mergeSort(points, s, l - 1)
        self.mergeSort(points, l+1, e)

        return points

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        self.mergeSort(points, 0, len(points) - 1)

        return points[:k]
