class Student:
    def __init__(self, id, name, age, group):
        self.id = id 
        self.name = name 
        self.age = age 
        self.group = group 
 
students = [] 
with open('students_new.txt',encoding = 'utf-8') as file:
    for line in file:
        data = line.strip().split(';') 
        
        student = Student(data[0], data[1], data[2], data[3]) 
        students.append(student) 
print('-' * 55)
print("|{:<3}|{:<35}|{:<7}|{:<5}|".format("ID", "FIO", "VARIANT", "GROUP")) 
print('-' * 55)
for student in students: 
    print("|{:<3}|{:<35}|{:<7}|{:<5}|".format(student.id, student.name, student.age, student.group))

print('-' * 55)
