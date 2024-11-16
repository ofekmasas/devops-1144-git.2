import os
import send2trash
#file=open('yoni.txt','r')
#print(file.read())

#file2=open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\omer is gay.txt")
#print(file2.read())
def file3_func():
  file3 = open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\demofile.txt", "r")
  for x in file3:
    if '!' not in x:
      print(x)

#file3_func()

#file4 = open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\demofile2.txt", 'a')
#file4.write('\nAnother line')
#file4.close()
#file4 = open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\demofile2.txt", 'r')
#print(file4.read())

#file5=open(r'C:\Users\ofekp\OneDrive\שולחן העבודה\newfile.txt','x')
#file5.close()
#file5=open(r'C:\Users\ofekp\OneDrive\שולחן העבודה\newfile.txt','a')
#file5.write('my content!\n')
#file5.close()
#file5=open(r'C:\Users\ofekp\OneDrive\שולחן העבודה\newfile.txt','r')

#print(file5.read())

if os.path.exists(r"C:\Users\ofekp\OneDrive\שולחן העבודה\send me to trash.txt"):
  send2trash.send2trash(r"C:\Users\ofekp\OneDrive\שולחן העבודה\send me to trash.txt")
else:
  print("The file does not exist")
