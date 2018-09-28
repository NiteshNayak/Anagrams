# Optimized Anagram
# nnayak
# Sep 27 2018

#path = '/Users/nnayak/Desktop/list.txt'

dict_sort_count = {}
most_anagram = {}
count = 0
readFile = []
sort_wordFile = []

from collections import Counter

def read_file():
    path = raw_input()
    openFile = open(path,'r')
    rdFile = openFile.readlines()
    rdFile_clean = [x.replace('\n','') for x in rdFile]
    return rdFile_clean

def sort_count(self):
    for i in range(0, len(readFile), 1):
        sort_word = readFile[i]
        sort_word = sort_word.lower()
        sort_word = ''.join(sorted(sort_word))
        sort_wordFile.append(sort_word)
        if sort_wordFile[i] in dict_sort_count:
            dict_sort_count[sort_wordFile[i]] += 1
        else:
            dict_sort_count[sort_wordFile[i]] = 1
    print(dict_sort_count)
   # most_anagram = dict(Counter(dict_sort_count))
   # print (most_anagram)


print("Enter the filename along with the path: ")

readFile = read_file()
print("")
print("The File has words :")
print(readFile)
print len(readFile)

sortFile = sort_count(readFile)
print("")
print("The sorted file is: ")
#print(sortFile)
