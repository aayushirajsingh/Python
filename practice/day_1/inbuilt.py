# Python program to demonstrate basic inbuilt library 
#Three lines to make our compiler able to draw:

import os
fd = "python.txt"
    
# popen() is similar to open()
file = open(fd, 'w')
file.write("This is awesome")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
      
# popen() provides gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("This is awesome!")
# File not closed, shown in next function.