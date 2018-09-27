# Anagram
# nnayak
# sep 25 2018

#ask the user for the file

path = '/Users/nnayak/Desktop/list.txt'

list_file = open(path,'r')
list_file_s = list_file.readlines()
print(list_file_s)
list_re_words = []
anagram_words = []

for i in range(len(list_file_s)):
    each_word = list_file_s[i]
    rearrange_word = ''.join(sorted(each_word))
    #print(rearrange_word)
    list_re_words.append(rearrange_word)

#print(list_re_words)

# Compare the words in the same list
for i in range(0,len(list_re_words)-1,1):
    for j in range(i+1,len(list_re_words)-1,1):
        if list_re_words[i] == list_re_words[j]:
            #print(list_re_words[i])
            anagram_words.append(list_file_s[i])

print(anagram_words)

# This is to remove the common words from the list 

for i in range(0, len(anagram_words)-1,1):
    for j in range(i+1, len(anagram_words)-1,1):
        if anagram_words[i] == anagram_words[j]:
            del anagram_words[i]

print(anagram_words)
