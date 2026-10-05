# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair], s=0, e=None) -> List[Pair]:
        if e is None:
            e = len(pairs) - 1
        if e - s + 1 <= 1:
            return pairs

        pivot_val = pairs[e]
        left  = s

        for i in range(left, len(pairs) -1):
            if pairs[i].key < pivot_val.key:
                temp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = temp 
                left +=1
        
        pairs[e] = pairs[left]
        pairs[left] = pivot_val

        self.quickSort(pairs, s, left - 1)
        self.quickSort(pairs, left + 1, e)

        return pairs
