#Q.1- Write a python script to create a databse of students named Students.
import pymongo
# initiallize the MongoClient
client = pymongo.MongoClient()
# connecting to 'Students'
database = client['Students']
# creating the collection 'Students_data'
collection = database['Students_data']
print('table created ')

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
for i in range (10):
    name=input('Name ')
    marks=int(input('Marks '))

#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
# inserting one document
for i in range (10):
    collection.insert_one({'Name ':name, 'Marks ':marks})
print('Data inserted in table ')

#Q.4- Print the names of all the students who scored more than 80 marks.
print('Students who scored more then 80 marks ')
d=collection.find({'Marks':{"$gt" : 80}})
for i in d:
    print(i)
    
