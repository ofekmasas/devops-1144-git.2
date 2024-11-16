import datetime
import os
############################task1
if(not os.path.exists(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt")):
    journal=open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt",'x')

journal=open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt",'a')

journal_entries=input("Please enter a few lines (to stop type 'stop'):\n")

while journal_entries !='stop':
    journal.write(str(datetime.datetime.now()) + ' ')
    journal.write(journal_entries + '\n')
    journal_entries=input("Please enter a few lines (to stop type 'stop'):\n")
journal.close()

############################task2
print('The lines you wrote: \n')
jornal = open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt",'r')
print(jornal.read())

############################task3
journal=open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt",'a')
journal_entries=input("Please enter a few more lines (to stop type 'stop'):\n")

while journal_entries !='stop':
    journal.write(str(datetime.datetime.now()) + ' ')
    journal.write(journal_entries + '\n')
    journal_entries=input("Please enter a few more lines (to stop type 'stop'):\n")

############################task4
jornal=open(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt",'r')


lines = len(jornal.readlines())
print(f'The number of lines: {lines}')





for line in lines:
    len(line.split())
sum = 
words= sum()
print('Number of words: ' + words)

