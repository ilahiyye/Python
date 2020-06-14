dictionary = {
    "room" : "otaq",
    "accommodation": "yaşamaq",
    "night" : "gecə",
    "day" : "gün",
    "child" : "uşaq",
    "adult" : "böyük",
    "passport" : "pasport	",
    "road" : "yol",
    "turn" : "döngə",
    "intersection" : "dörd yol ayrıcı		",
    "detour" : "dolayı yol	",
    "stop" : "dayan",
    "no passage" : "keçmək qadağandır",
    "parking" : "dayanacaq",
    "attention" : "diqqət",
    "entrance" : "giriş",
    "exit" : "çıxış",
    "left" : "sol",
    "right" : "sağ",
    "open"  : "açıq",
    "close" : "bağlı",
    "prohibite" :  "qadağa",
    "allowed" : "icazə",
    "pull" : "dartmaq",
    "push" : "itələmək",
    "here" : "burada",
    "there" : "orada",
    "danger" : "təhükəlidir",
    "careful" : "ehtiyatlı olun",
    "break" : "fasilə",
    "crossing" : "keçid",
    "information" : "məlumat",
    "spicy" : "acı",
    "cheese" : "pendir",
    "bread" : "çörək",
    "soup" : "şorba",
    "juice" : "şirə",
    "water" : "su",
    "customs" : "gömrük",
    "waiter" : "ofisiant",
    "house" : "ev",
    "city" : "şəhər",
    "street" : "street",
    "ticket" : "bilet"
}

def search_Key(key):
    
    return dictionary.setdefault(key, "No result or Wrong word!") 

print("\t--------------   Welcome!  ------------\n\tFor 'Azerbaijan to English' enter  to  1\n\tFor 'English to Azerbaijan' enter  to  2")
print("\tIf yo want program running to stop enter 'exit'\n")
while True:
    command = input("\ninput 1 or 2 or exit: ")
    
    if command == "1":
        print('\n---------  You choise translet English to Azerbaijan  ----------\n')
        eng_word = input('\tEnglish word: ')
        print(f'\tTranslations: {search_Key(eng_word)}')

    elif command == "2":
        print('\n---------  You choise translet Azerbaijan to English  ----------\n')
        az_word = input('\tAzerbaijan word: ')
        
        translete = [key for key, value in dictionary.items() if value == az_word]
        
        if translete:
            print('\tTranslations:   ', *translete)#*list listin elementlerini [] olmadan cap edir.  ,sep(', v' ya \n') yazsan ona uygun el arasina elave edecek
        else:
            print("\tNo result or Wrong word\n")

    
    elif command == "exit":
        print("\n\tYour choice: Exit\n\n-------------------------  Exiting program  ----------------------\n")
        break

    else:
        print("\n--------------------   Error: Wrong input!    -----------------\n")


        
        
