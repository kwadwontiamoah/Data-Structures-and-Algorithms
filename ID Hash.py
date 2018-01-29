from HashTable import *
import random
file = open('StudentID.txt', 'w')
H = HashTable()

def generateID(classYear):
   ind = 0
   for i in range(1000):
        digits=random.randint(0,9999)
        studentID =(('%04d'%digits)+ str(classYear))
        val = int(studentID)%H.size
        
        for n in H.data:
           if studentID == n:
              digits=random.randint(0,9999)
              studentID =(('%04d'%digits)+ str(classYear))
           else:
              val = int(studentID)%H.size
              H[val] = studentID
              ind = ind + 1

   print('Program regenerated Student ID %d times'%ind)
   print(H.slots)
   print(H.data)
   for item in H.data:
      data = str(H.data)
   file.write("{}\n".format(data))

generateID(2019)

