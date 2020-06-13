contact = {
    'Cehune': '0558706195',
    'Leyla' : '0553577271',
    'Nayma' : '0503255415',
    'Terlan': '0509786757',
    'Sevda' : '0505390810',
    }
def contact_Clear():
    return contact.clear()

def contact_Add(name, number):
    contact[name] = f'{number},'
    return print(f"{name} add to contact")

    
def contact_SearchNumber(name):
    return contact.setdefault(name, 'No results')

def contact_delete(name):
    return contact.pop(name) 


def allContact():
    l = contact.items()
    for k , v in l:
        print(f'{k} : {v}\n')


while True:
    command = input("input command -'Clear Contact', 'Add Contact', 'Search', 'Delete Contact', 'Contact List', 'Exit' : ")
    command = command.lower()
    if (command == 'clear contact'):
        contact_Clear()
        print("Your contact clear!")

    elif (command == 'add contact'):
        name = f"{input('input name: ')}"
        number =f"{input('input number: ')}"
        contact_Add(name, number)
        allContact()
        

    elif (command == "search"):
        name = f"{input('input name: ')}"
        result = contact_SearchNumber(name) 
        if result != "No results":
            print(f"{name}'s number is {result}")
        else:
            print(result)


    elif (command == 'delete contact'):
        number = f"{input('input name: ')}"
        contact_delete(number)
        allContact()
        print(f'{name} was delete in contact!')
        
    
    elif (command == 'contact list'):
        allContact()

    elif (command == 'exit'):
        print("Exiting program...")
        break

    else:
        print("Error: Wrong command!")

