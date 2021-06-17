
from flask import Flask, request, Response, json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json
import multiprocessing as processing
from pymongo import MongoClient

import threading


class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection =MongoClient("mongodb+srv://ad199ad:12345@mongodb.qkjms.mongodb.net/mongoDB?retryWrites=true&w=majority",ssl=True,ssl_cert_reqs='CERT_NONE')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


app=Flask(__name__)




@app.route('/github',methods=['POST'])
def api_github():
   if request.headers['content-Type']=='application/json':

       data=json.dumps(request.json)
       mongo = MongoDBConnection()
       with mongo:
           database = mongo.connection["mongoDB"]
           collection = database["registrations"]
           collection.insert_one(json.loads(data))
       return json.dumps(request.json)


def build_client_side():


    print("welcome to github pulls API ")
    print("in this project i use rest API from github(webhook) and uplode every pull data to Mongo data-base")
   # input("to see simple data from all the pulls press on any key")
    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection["mongoDB"]
        collection = database["registrations"]

    x = collection.find({}, {"action":"opened","number":1})
    print(x)
    for data in x:
        print(data)

    #input("to see more data from all the pulls and scrennshot press on any key")
    x = collection.find({}, {"action":"opened","number":1,"pull_request.url":1,"pull_request.title":1,"pull_request.created_at":1})
    for data in x:
        print(data)

    img = mpimg.imread('mongoDB.png')
    imgplot = plt.imshow(img)
    plt.show()




if __name__ =='__main__':
    build_client_side()
    print("the server will start now")
    app.run(debug=True)




