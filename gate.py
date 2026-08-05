# print(2**3**2)


# a=[1,2,3,]
# b=a
# c=a[:]
# print(a is b,a is c,)
# print(ord ,'s')







l1=[10,20,30,40,50]
# for iyem in l1:
#     print(iyem)

for i in range(len(l1)-1,-1,-1):
      print(l1[i])











# getters in python
class collage:
      def __init__(self,student):
            
        self._student=student
      @property
      def student(self):
           return self._student
      
a=collage("sujay") 
print(a.student)   