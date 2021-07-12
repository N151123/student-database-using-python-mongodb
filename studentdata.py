from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB 
client = MongoClient('localhost:27017')
db = client.StudentData


# Function to insert data into mongo db 
def insert():
    try:
        studentId = input('Enter Student id :')
        studentName = input('Enter Name :')
        studentAge = input('Enter age :') 
        studentBranch = input('Enter Branch :') 
        db.Students.insert_one( { "id": studentId, "name":studentName, "age":studentAge, "branch":studentBranch }) 
        print('\nInserted data successfully\n')
    except Exception as e:
        print(str(e))

# function to read records from mongo db 
def read(): 
    try: 
        studentCol = db.Students.find() 
        print('\n All data from StudentData Database \n') 
        for student in studentCol: 
            print(student) 
    except Exception as e: 
        print(str(e))

# Function to update record to mongo db 
def update(): 
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n') 
        age = input('\nEnter age to update\n') 
        branch = input('\nEnter branch to update\n') 
        db.Students.update_one( {"id": criteria}, { "$set": { "name":name, "age":age, "branch":branch } } ) 
        print("\nRecords updated successfully\n")
    except Exception as e:
        print(str(e))

# Function to delete record from mongo db 
def delete(): 
    try: 
        criteria = input('\nEnter student id to delete\n') 
        db.Students.delete_many({"id":criteria}) 
        print('\nDeletion successful\n') 
    except Exception as e: 
        print(str(e))


def main():
     while(1): 
        # chossing option to do CRUD operations
        selection = input('\nSelect 1-insert, 2-update, 3-read, 4-delete , q-quit\n')
        
        if selection == '1': 
            insert() 
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        elif selection == 'q':
            break
        else: 
            print('\n INVALID SELECTION \n')

if __name__=="__main__":
    main()
            
