
class Student_List():
    def __init__(self,s_list):
        self.students=s_list
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index==len(self.students):
            raise StopIteration
        return self.students[self.index]

r=Student_List(['charan','vinit','naveen','deepak'])

i=iter(r)

print(next(i))
print(next(i))
print(next(i))