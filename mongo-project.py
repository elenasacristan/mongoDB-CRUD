
import pymongo
import os
import env

MONGODB_URI = os.environ.get("MONGODB_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        

def show_menu():
    print("")
    print("1. Add New Record")
    print("2. View Record")
    print("3. Edit Record")
    print("4. Remove Record")
    print("5. Exit")
    print("")

    option = input("Please select one option > ")
    return option

def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({"first":first.lower(), "last":last.lower()})
    except:
        print ("Error connecting")

    if not doc:
        print("")
        print ("Not record found!")
    
    return doc



def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter last dob > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair_color > ")
    nationality = input("Enter nationality > ")
    occupation = input("Enter occupation > ")
    print("")

    new_record = {"first":first.lower(), "last":last.lower(), "dob":dob, "gender":gender, "hair_color":hair_color, "nationality":nationality, "occupation":occupation}

    try:
        coll.insert_one(new_record)
        print("")
        print("Document Inserted!")
    except:
        print("Error accessing the database")

def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        

def edit_record():
    doc = get_record()
    if doc:
        print("")
        updated_record={}
        for k, v in doc.items():
            if k != "_id":
                updated_record[k] = input(k.capitalize() + "[" + v.capitalize() + "] >" )
                if updated_record[k]=="":
                    updated_record[k]=v
        try:
            coll.update_one(doc,{'$set':updated_record})
            print("")
            print("Record updated")
        except:
            print("Error connecting to the database")

def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        confirmation = input('Is this the record that you want to remove? Y/N >')

        if confirmation.lower()=="y":
            try:
                coll.delete_one(doc)
                print("")
                print("Record removed")
            except:
                print("")
                print("Record NOT removed. Error connecting to database")
        else:
            print("")
            print("Record NOT removed")


                        
    

def main_loop():
    while True:
        option = show_menu()
        print("")
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Wrong answer!, try again")

           
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()