class Solution:
    def calPoints(self, operations: list[str]) -> int:
        arr = []

        for op in operations:
            print(arr)
            if len(arr) >= 2 and op == '+':
                pop_prev1 = arr.pop()
                pop_prev2 = arr.pop()
                sum_of_two_prev = pop_prev1 + pop_prev2

                arr.append(pop_prev2)
                arr.append(pop_prev1)
                arr.append(sum_of_two_prev)
            elif  len(arr) > 0 and op == 'D':
                new_value = 2 * arr[len(arr) -1] 
                arr.append(new_value)
            elif  len(arr) > 0 and op == 'C':
                arr.pop()
            else:
                arr.append(int(op))
        return sum(arr)
