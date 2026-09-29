class Solution:
    def calPoints(self, operations: list[str]) -> int:
        arr = []

        for i in range(len(operations)):
            print(arr)
            if len(arr) >= 2 and operations[i] == '+':
                pop_prev1 = arr.pop()
                pop_prev2 = arr.pop()
                sum_of_two_prev = pop_prev1 + pop_prev2

                arr.append(pop_prev2)
                arr.append(pop_prev1)
                arr.append(sum_of_two_prev)
            elif  len(arr) > 0 and operations[i] == 'D':
                new_value = 2 * arr[len(arr) -1] 
                arr.append(new_value)
            elif  len(arr) > 0 and operations[i] == 'C':
                arr.pop()
            else:
                arr.append(int(operations[i]))

        return sum(arr)
