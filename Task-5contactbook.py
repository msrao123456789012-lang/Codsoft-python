contacts={}
def createcontact():
    name=(input("Enter new contact name:")).upper()
    while True:
        phone=input("Enter phone number:")
        if phone.isdigit() and len(phone)==10:
            break
        else:
            print("Enter a valid number")
    email=input("Enter new contact email adress:")
    Adress=input("Enter address of the contact:")
    if phone in contacts:
        print("Already that number exists in your contacts")
    else:
        contacts[phone]={
            "Name":name,
            "Email":email,
            "Adress":Adress
        }
    #return contacts
def viewcontact():
    if len(contacts)==0:
        print("No contacts to view !")
    else:    
        for key,value in contacts.items():
          print(key,"{")
          for key,valu in value.items():
              print(f"{key}:{valu}")
          print("}")
def searchcontact():
    keyword=(input("Enter phone 📱 number or name of the contact to be searched:"))
    found=False
    for key,value in contacts.items():
        if keyword.upper() in value["Name"] or keyword==key:
            print("-----Contact found----")
            print(f"Name:{value["Name"]}")
            print(f"email:{value["Email"]}")
            print(f"Adress:{value["Adress"]}")
            found=True
            break
    if(not found):
        print("No such contact found")
def updatecontact():
    contact=input("Enter phone number details have to be updated:")
    if contact in contacts:
       update_item=input(f"What has to be updated of {contact}:")
       contacts[update_item]=input(f"Enter value of updatable item {update_item}:")
       print("contact detalis updated successfully")
    else:
        print("No such contact found")
def deletecontact():
    contact=input("Enter phone number which has to be delted:")
    if contact in contacts:
        del contacts[contact]
        print("contact deleted successfully !")
    else:
        print("Such contacts not exist !")
def op(choice):
    match choice:
        case 1: return createcontact()
        case 2: return viewcontact()
        case 3: return searchcontact()
        case 4: return updatecontact()
        case 5: return deletecontact()
        case _: print("Enter valid operation to perform !")
print("="*40)
print("Welcome to contact book 📖 ")
print("="*40)
while True:
    print("Enter your choice from above")
    choice=int(input(f" 1 for create new contact \n 2 for view contact \n 3 for search contact \n 4 for updatecontact \n 5 for delete contact\n choice:"))
    op(choice)
    op_again=(input("Do you to perform any operation else:")).upper()
    if op_again=='YES':
      continue
    else:
      break
