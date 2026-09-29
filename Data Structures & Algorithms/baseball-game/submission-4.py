class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        solution = 0

        for i in operations:

            if i == "D":

                ns = 2 * stack[-1]

                stack.append(ns)
            
            elif i == "+":

                ns = stack[-1] + stack[-2]

                stack.append(ns)
            
            elif i == "C":

                stack.pop()
            
            else:

                stack.append(int(i))
                
               
        
        for num in stack:

            solution += num

        return solution


            
