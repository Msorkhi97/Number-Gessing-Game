N = 'a'
a = 0
b = 99
from msvcrt import kbhit
import random
hads = random.randint(a,b)
print (hads)
while N != 'd':
     N = input ('hadse sys chetor ast ?'    )
     if N == 'b': 
         b = hads
         hads = random.randint(a,b)
         print (hads)
     elif N == 'k':
         a = hads
         hads = random.randint(a,b)
         print (hads)
     elif N == 'd': 
         break   
print ( 'hadse shoma' , hads , 'ast')

