contact = {
    'Cehune': '05387264195',
    'Leyla' : '05327727421',
    'Nayma' : '25133255215',
    'Terlan': '05997869547',
    'Sevda' : '05953900410',
    }
def contact_Clear():
    return contact.clear()

def contact_Add(name='None', number='None'):
    contact[name] = f'{number},'
    return print(f"{name} add to contact")

    
def contact_SearchNumber(name='None'):
    return contact.setdefault(name, 'No results')

def contact_delete(name='None'):
    if name in contact.keys():
        del contact[name] 
        return True
    


def allContact():
    for k , v in contact.items():
        print(f'{k} : {v}\n')


while True:
    command = input("input command -'Clear Contact', 'Add Contact', 'Search', 'Delete Contact', 'Contact List', 'Exit' : ")
    command = command.lower()
    if (command == 'clear contact'):
        contact_Clear()
        print("Your contact clear!")

    elif (command == 'add contact'):
        name   = input('input name: ')
        number = input('input number: ')
        contact_Add(name, number)
        allContact()
        

    elif (command == "search"):
        name = input('input name: ')
        result = contact_SearchNumber(name) 
        if result != "No results":
            print(f"{name}'s number is {result}")
        else:
            print(result)


    elif (command == 'delete contact'):
        name = input('input name: ')
        
        if contact_delete(name):
            contact_delete(name)
            allContact()
            print(f'{name} was delete in contact!')
        else:
            print("Wrong Contact Name!")
        
    
    elif (command == 'contact list'):
        allContact()

    elif (command == 'exit'):
        print("Exiting program...")
        break

    else:
        print("Error: Wrong command!")

