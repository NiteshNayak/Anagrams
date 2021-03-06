# Optimized Anagram
# nnayak
# Sep 27 2018

#path = '/Users/nnayak/Desktop/list.txt'

dict_sort_count = {}
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
            #del sort_wordFile[i]
            dict_sort_count[sort_wordFile[i]] += 1
        else:
            dict_sort_count[sort_wordFile[i]] = 1

    for key in list(dict_sort_count.keys()):
        if dict_sort_count[key] == 1:
            del dict_sort_count[key]

    for w in sorted(dict_sort_count, key=dict_sort_count.get, reverse=True):
        print w, dict_sort_count[w]


print("Enter the filename along with the path: ")

readFile = read_file()
print("")
print("The File has words :")
print(readFile)

print("")
print("Most words are useds from the combination are: ")
sortFile = sort_count(readFile)
