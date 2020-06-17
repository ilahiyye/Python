contact = {
    'Cehune': '05387264195',
    'Leyla' : '05327727421',
    'Nayma' : '25133255215',
    'Terlan': '05997869547',
    'Sevda' : '05953900410',
    }
def contact_clear():
    return contact.clear()

def contact_add(name='None', number='None'):
    contact[name] = f'{number},'
    return print(f"{name} add to contact")

    
def contact_search_number(name='None'):
    return contact.setdefault(name, 'No results')

def contact_delete(name='None'):
    if name in contact.keys():
        del contact[name] 
        return True
    
def all_contact():
    for k , v in contact.items():
        print(f'{k} : {v}\n')


while True:
    command = input("input command -'Clear Contact', 'Add Contact', 'Search', 'Delete Contact', 'Contact List', 'Exit' : ")
    command = command.lower()
    if (command == 'clear contact'):
        contact_clear()
        print("Your contact clear!")

    elif (command == 'add contact'):
        name   = input('input name: ')
        number = input('input number: ')
        contact_add(name, number)
        all_contact()
        

    elif (command == "search"):
        name = input('input name: ')
        result = contact_search_number(name) 
        if result != "No results":
            print(f"{name}'s number is {result}")
        else:
            print(result)


    elif (command == 'delete contact'):
        name = input('input name: ')
        
        if contact_delete(name):
            contact_delete(name)
            all_contact()
            print(f'{name} was delete in contact!')
        else:
            print("Wrong Contact Name!")
        
    
    elif (command == 'contact list'):
        all_contact()

    elif (command == 'exit'):
        print("Exiting program...")
        break

    else:
        print("Error: Wrong command!")

