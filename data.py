import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore

cred = credentials.Certificate("C:\Projects\SDK_Key\\family-tree-tuifua-firebase-adminsdk-m2yx2-7363018f9d.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_document():
    
    name = input("Name:")
    
    while True:
        try:
            age = int(input("Age: "))
            
            if isinstance(age, int) == True:
                break
        except:
            print("Please use numbers only.")
        
    birthday = input("birthday: ")
    birthplace = input("Birthplace: ")
    currentplace = input("Current living place: ")

    data = {

        u"name" : name,
        u"age" : age,
        u"birthday" : birthday,
        u"birthplace" : birthplace,
        u"currentplace" : currentplace
    }
    db.collection(u'family').document(u'mele').set(data)

def update_document():
    while True:
        while True:
            try:
                choice = int(input("Which one would you like to update? Or leave: 1 = name, 2 = age, 3 = birthday 4 = birthplace 5 = currentplace 6 = Leave: "))
                
                if isinstance(choice, int) == True:
                    break
            except:
                print("Please use numbers only.")
        

        if choice == 1:
            name = input("What would you like the new name to be: ")
            data = {u'name' : name}
            db.collection(u'family').document(u'viliami').update(data)

        elif choice == 2:
            while True:
                try:
                    age = int(input("Age: "))
                    
                    if isinstance(age, int) == True:
                        break
                except:
                    print("Please use numbers only.")
                    
            data = {u'age' : age}
            db.collection(u'family').document(u'viliami').update(data)

        elif choice == 3:
            birthday = input("What would you like the new birthday to be: ")
            data = {u'birthday' : birthday}
            db.collection(u'family').document(u'viliami').update(data)

        elif choice == 4:
            birthplace = input("What would you like the new birthplace to be: ")
            data = {u'birthplace' : birthplace}
            db.collection(u'family').document(u'viliami').update(data)

        elif choice == 5:
            currentplace = input("What would you like the new currentplace to be: ")
            data = {u'currentplace' : currentplace}
            db.collection(u'family').document(u'viliami').update(data)
        
        elif choice == 6:
            print('See you later!')
            break
        else:
            print('Pick a number between between 1 and 6 please.')


def delete_document():
    while True:

        choice = input("ARE YOU SURE YOU WANT TO DELETE THIS DOCUMENT? Yes or No")
        if choice.lower() == "yes":
            choice = input("You sure you sure?")
            if choice.lower() == "yes":
                db.collection(u'family').document(u'viliami').delete()
        
        elif choice.lower == "no":
            print("See you later!")
            break
        else:
            print("See you later!")
            break

def query():
    results = db.collection(u'family').where(u'age', u'>', 17).get()
    
    for i in results:
        print(u'{} => {}'.format(i.id, i.to_dict()))





def main():
    while True:

        while True:
            try:
                choice = int(input("What would you like to do, create a document = 1, delete a document = 2, update a document = 3, show and example query = 4, or leave = 5: "))
                    
                if isinstance(choice, int) == True:
                    break
            except:
                    print("Please use numbers only.")

        if choice == 1:
            add_document()
            
        
        elif choice == 2:
            delete_document()
            
        
        elif choice == 3:
            update_document()
            
        
        elif choice == 4:
            query()
        
        elif choice == 5:
            print("Have fun!!")
            break
            

main()


    