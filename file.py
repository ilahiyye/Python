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

let = max(letter_dict, key=letter_dict.get)              #letter.dict. deki en bouk value tapir
w = max(word_dict, key=word_dict.get)                    #word.dict. deki en boyuk value tapir
print(f"Frequent letters:'{let}'-{letter_dict.get(let)}") #hemin herin valusunu get metodu ile aliriq
print (f'Count: {len(words)} ')
print(f'Frequent word: {w} - {word_dict.get(w)}')
    
      

