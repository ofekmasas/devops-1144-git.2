#capitals = {'France': 1, 'Spain': 5, 'Japan': 9}
#capitals['France']= capitals['France'] +1
#print(capitals)

text = "abcdeeefffggggg"

def count_chars(text):
    d = {} # { "h": 2, "e": 1, "l": 2, "o": 1, " ": 1 } 

    for c in text:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

print(count_chars('123145235'))
print(count_chars('1231ADFADGa45235'))
print(count_chars('12314aaaaa5235'))