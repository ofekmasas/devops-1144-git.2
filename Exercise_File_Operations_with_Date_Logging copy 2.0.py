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
def calculate_lines_and_words(filepath):
    jornal=open(filepath,'r')

    list_of_lines = jornal.readlines()
    lines_num = len(list_of_lines)

    sum=0
    for line in list_of_lines:
        words_in_line = len(line.split())
        sum += words_in_line

    return lines_num,sum

lines_num,words_num =calculate_lines_and_words(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt")
print(f'The number of lines is {lines_num}\nThe number of words is {words_num}')
