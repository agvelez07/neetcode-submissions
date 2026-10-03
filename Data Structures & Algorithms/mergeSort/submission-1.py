#Definition for a pair.
class Pair:
     def __init__(self, key: int, value: str):
         self.key = key
         self.value = value
class Solution:
    def merge(self, left: list[Pair], right: list[Pair]) -> list[Pair]:
        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right) :
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result

    def mergeSort(self, pairs: list[Pair]) -> list[Pair]:
        if len(pairs) <= 1:
            return pairs

        m = len(pairs) // 2
        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])

        return self.merge(left, right)
