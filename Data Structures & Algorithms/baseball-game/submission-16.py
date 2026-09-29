class Solution:
    def calPoints(self, operations: list[str]) -> int:
        arr = []
        for op in operations:
            if len(arr) >= 2 and op == '+':
                a = arr.pop()
                b = arr.pop()
                arr.append(b)
                arr.append(a)
                arr.append(a+b)
                #arr.append(arr[-2] + arr[-1])
            elif  len(arr) > 0 and op == 'D':
                arr.append( 2 * arr[-1] )
            elif  len(arr) > 0 and op == 'C':
                arr.pop()
            else:
                arr.append(int(op))
        return sum(arr)
