# IMPORTS
from nltk import everygrams
import enchant
import string

# INITIALIZATION
d = enchant.Dict("en_US")

# REPLACE WITH THE PATH OF THE WORDSEARCH LETTERS
cw = open('./')
wordsearch = []
s = ''
length = len(cw.readline())
indices = range(length - 1)
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
al = alphabet_list[:15];
alr = al[::-1];
cw.seek(0)


def get_char(n, string):
    return string[n]

def add_word_tags(row, words, is_reverse, is_vertical, is_diagonal):
    # adding location tags to words
    # format is: rows are [a-z] columns are [1-n]
    for word in words:
        start = str(row.find(word)+1) if is_reverse == False else str(length - row.find(word) - 1);
        end = str(len(row) - row[::-1].find(word[::-1])) if is_reverse == False else str(length - (len(row) - row[::-1].find(word[::-1])));
        if is_diagonal == False:
            word += ' - ' + alphabet_list[index] + start + ':' + alphabet_list[index] + end if is_vertical == False else ' - ' + str(indices[index] +1) + alphabet_list[int(start)-1] + ':' + str(indices[index] + 1) + alphabet_list[int(end)-1];
        else:
            word += ' - ' + alphabet_list[index] + start + ':' + alphabet_list[index] + end if is_vertical == False else ' - ' + str(indices[index] + int(start)) + alphabet_list[int(start)-1] + ':' + str(indices[index] + int(end)) + alphabet_list[int(end)-1];
        print(word)
        

def add_word_tags_left_diagonal(row, words, is_reverse):
    # adding location tags to words
    # format is: rows are [a-z] columns are [1-n]
    for word in words:
        start = str(row.find(word)+1) if is_reverse == False else str(row.find(word) - 1);
        end = str(len(row) - row[::-1].find(word[::-1])) if is_reverse == False else str(row[::-1].find(word[::-1])+1);
        word += ' - ' + str(alphabet_list[index + int(start) - 1]) + str(indices[int(start)]) + ':' + str(alphabet_list[index+ int(end)-1]) + str(indices[int(end)]);
        print(word)

# get all possible words horizontally
for index,x in enumerate(cw):
    
    
    # getting all words in this row
    s += x.strip()+' '
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    add_word_tags(s,words, False, False, False);
    s = '';
    
    # getting all words of this row as reversed
    s += x[::-1].strip()
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    add_word_tags(s,words, True, False, False);
    
    # pushing this line to an array
    wordsearch.append(x.strip())
    
    # cleaning the string holder for the next row
    s = '';
cw.seek(0)


# get all possible words vertically
for index, x in enumerate(cw):
    buckets = [index] * (length - 1)
    vertical = ''.join(list(map(get_char, buckets, wordsearch))).strip()
    
    # get words of this column
    s += vertical
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    add_word_tags(s,words, False, True, False);
    s = '';
    
    # get words of this column as reversed
    s += vertical[::-1]
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    add_word_tags(s,words, True, True, False);
    s = '';
cw.seek(0)

temp = wordsearch[:]

# get all possible words in the right diagonal
for index, x in enumerate(cw):
    x = range(index, length - 1)
    diagonal = ''.join(list(map(get_char, x, temp))).strip()
    temp.pop()
    
    # get words of this diagonal
    s += diagonal
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    add_word_tags(s,words, False, True, True);
    s = '';
    
    # get words of this diagonal as reversed
    s += diagonal[::-1]
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    add_word_tags(s,words, True, True, True);
    s = '';
cw.seek(0)

temp = wordsearch[:]

# get all possible words in the left diagonal
for index, x in enumerate(cw):
    x = range(length - 1 - index)
    diagonal = ''.join(list(map(get_char, x, temp))).strip()
    temp.pop(0)

    # get words of this diagonal
    s += diagonal
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    if index > 0 : add_word_tags_left_diagonal(s,words, False);
    s = '';
    
    # get words of this diagonal as reversed
    s += diagonal[::-1]
    words = [''.join(z) for z in everygrams(s) if d.check(''.join(z)) and len(z) > 3 and ''.join(z).find(' ') == -1];
    if index > 0: add_word_tags_left_diagonal(s,words, True);
    s = '';

# print(wordsearch)
# print(cw.read());
# print(string);
