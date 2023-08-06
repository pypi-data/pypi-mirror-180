## Takes inputs from user and prints number students


class School:
    def __init__(self,name,regno,marks):
        self.name= name
        self.regno=regno
        self.marks=marks

    def print_name(self):
        return self.name,self.regno,self.marks


Number_of_students = int(input('Enter number of stduents:\n'))

list1=[]


for _ in range(0,Number_of_students):
    student_name = input("Enter student Name: \n")
    student_rego = int(input("Enter stduent Rego: \n"))
    student_marks= int(input("Enter student Marks: \n"))

    obj1= School(student_name,student_rego,student_marks)
    list1.append(obj1.print_name())
    #print(list1)
    #list1=[]
    student_name=''
    student_rego=int(0)
    student_marks=int(0)
    obj1=''

for i in list1:
    print(i)


    

    
