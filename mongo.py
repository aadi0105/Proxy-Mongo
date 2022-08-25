import pymongo

if __name__=='__main__':
    print("welocme to pymongo")
    client = pymongo.MongoClient("mongodb://ip-172-31-46-205.us-east-2.compute.internal:27017/")
    print(client)
    db = client['harry']
    collection = db['abc']
    dictionary = {'name': 'aadi', 'marks':50}
    collection.insert_one(dictionary)
