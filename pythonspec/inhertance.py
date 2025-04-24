class collage:
    def __init__(self,collage_id,collage_name):
        self.collage_id=collage_id
        self.collage_name=collage_name
    def prin(self):
        print(self.collage_id,self.collage_name)

class student(collage):
    pass
    # def __init__(self,student_id,student_name):
    #     self.student_id=student_id
    #     self.student_name=student_name
    # def prinn(self):
    #     print(self.student_id,self.student_name)   

r1=student(188,"hanan")
r1.prin()


        