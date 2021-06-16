import urllib

import export as export
from flask import Flask, request, Response, json
from flask_github_webhook import GithubWebhook

from django.contrib import admin

import os
import json
from github_webhook import Webhook
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pymongo import MongoClient
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
import ssl
import urllib.request
class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection =MongoClient("mongodb+srv://ad199ad:12345@mongodb.qkjms.mongodb.net/mongoDB?retryWrites=true&w=majority",ssl=True,ssl_cert_reqs='CERT_NONE')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()



# Issue the serverStatus command and print the results


app=Flask(__name__)
webhook=GithubWebhook(app)



@app.route('/github',methods=['POST'])
def api_gh_message():
    if request.headers['content-Type'=='applicaion/json']:
         myinfo= json.dumps(request.json)

    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection["mongoDB"]
        collection = database["registrations"]
        collection.insert_one(myinfo)

if __name__ =='__main__':
    app.run(debug=True )

#add update for test