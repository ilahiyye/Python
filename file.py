path = "C:/Users/user/Desktop/Tech_Python/Week2/story.txt"

with open(path, 'r') as file:  #bu cur yailisda file.close() yazmaga ehtiyac qalmir
    content = file.read()       #readlines() yazdiqda ise metni bir listin icine yazdirir

content = content.upper()
content = content.translate({ord(i): None for i in ''',.;:-)(_"'''})   
words = content.split()


word_dict = {}
letter_dict = {}

for word in words:
    if (word in word_dict):
        word_dict[word] += 1  # lugete ozu elave olunur
    else:
        word_dict[word] = 1

for word in words:
    for letter in word:
        if (letter in letter_dict): #herflerin saynini dictionariye elave edirik
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

print(f"Frequent letters:'{max(letter_dict, key=letter_dict.get)}'") #dict. deki en bouk value tapir
print (f'Count: {len(words)} ')
print(f'Frequent word: {max(word_dict, key=word_dict.get)}')
    


#for i, j in letter_dict.items():
    #print(i, ":",  j)

       

