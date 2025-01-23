import pymongo

if __name__ == "__main__":
#--------------DB connection-------------.
    print("Welcome to the pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db =client['Sagar']
    collection = db['collectiondemo']
    

#------------------insert single / multilple entries in our collection---------

    # dictionary = {'name': 'Harry', 'marks': 50}
    # collection.insert_one(dictionary)   #insert a single record.
    # print(client.list_database_names())
    # print(db.list_collection_names())
    # manyentries = [
    # {"_id" : 1, "name": "Alice",
    # "age": 30,
    # "role": "Engineer"},
    # {"_id" : 2, "name": "Sagar",
    #     "age": 28,
    #     "role": "Developer"},
    # {"_id" : 3, "name": "Ankita",
    #     "age": 25,
    #     "role": "HR"}
    #     ]
    # collection.insert_many(manyentries)     #insert multiple records


#------------------------Find records in the collection--------------------------
    # fetchonedoc =  collection.find_one({'name':'Sagar'})      #it will find only one occurence
    # print(fetchonedoc)
    alldocs = collection.find({'age' : {"$gt": 25 }}, {'name': 0} )    #takes two args query (it could be a condition as well), projection. if the key is 0 then the output will ignore it and display other values in the collection document. bydefault all values are 1 including _id
    for items in alldocs:    #collection is the iterable obj so we need to use for loop to fetch the items.
        print(items)

    print(collection.count_documents({}))
    # print(dir(alldocs))

#-------------update one and many records------------
    # prev = {'name': 'Harry'}
    # nextt = {"$set": {'name': 'Tom'}}
    # update_record = collection.update_many(prev, nextt)
    # # collection.update_one(prev, nextt) 
    # print('Records updated :', update_record.modified_count)

#--------------delete one/ many records -------------------
    # record = {"_id":3}
    # collection.delete_one(record)
    # delrec = collection.delete_many(record)
    # print('Records deleted :', delrec.deleted_count)


