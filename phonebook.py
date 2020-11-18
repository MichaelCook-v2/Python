def phone_menu():
    print("Look up a Contact")
    print("Set an entry")
    print("Delete a Contact")
    print("List all Contacts")
    print("Quit")
    print("What would you like to do?")
number = {}
menu_choice = 0
print_menu ()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
if menu_choice ==1:
    print("Enter a search")
    for x in search.keys():
    print("Name: ", x "\tnumber:", numbers[x])
    print()
elif menu_choice ==2:
    print("Enter a Name and number")
    name = input("Name: ")
    phone number = input("Number: ")
    numbers[name]= phone
elif menu_choice ==3:
    print("Remove a Contact")
    contact = input("Name: ")
    if name in numbers:
        del numbers[name]
    else:
    print(name, "was not found")
elif menu_choice ==4:
    print("List all Contacts")
    contacts = input ("Contacts: ")
    if contacts in contacts:
    print("Contacts", numbers[name])
    else:
    print(contact, "Contacts not found")
elif menu_choice !=5:
    print("Goodbye")
    phone_menu()
clear()
import pickle