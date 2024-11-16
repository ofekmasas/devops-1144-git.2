def calculate_lines_and_words(filepath):
    jornal=open(filepath,'r')

    list_of_lines = jornal.readlines()
    lines_num = len(list_of_lines)

    sum=0
    for line in list_of_lines:
        words_in_line = line.split()
        num_of_words = len(words_in_line)
        sum += num_of_words

    return lines_num,sum

lines_num,words_num =calculate_lines_and_words(r"C:\Users\ofekp\OneDrive\שולחן העבודה\journal.txt")
print(f'The number of lines is {lines_num}\nThe number of words is {words_num}')





