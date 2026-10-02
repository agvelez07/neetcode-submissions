class StudentChoice:
    def __init__(self, sandwich_type=-1):
        self.sandwich_type = sandwich_type
        self.next = None 

class StudentQuee:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_student(self, sandwich_type):
        student_choice = StudentChoice(sandwich_type)
        
        if not self.head:
            self.head = student_choice
            self.tail = student_choice
            return 
 
        self.tail.next = student_choice 
        self.tail = student_choice
    
    def remove_student(self):
        if not self.head:
            return 
        self.head = self.head.next 
    
    def get_choice(self):
        if self.head:
            return self.head.sandwich_type
        return -1
      

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sq = StudentQuee() 
        for i in students: 
            sq.add_student(i)

        refused_sandwiches = 0
        while sandwiches:
            next_in_quee = sq.get_choice()
            if next_in_quee == -1 or refused_sandwiches == len(students):
                break
            elif next_in_quee == sandwiches[0]:
                refused_sandwiches = 0
                sandwiches.pop(0)    
            else:
                refused_sandwiches +=1 
                sq.add_student(next_in_quee)
            sq.remove_student() 
           
  

        return len(sandwiches)
