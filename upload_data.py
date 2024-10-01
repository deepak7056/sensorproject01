from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url"
import urllib.parse

escaped_username = urllib.parse.quote_plus("deepak70561")
escaped_password = urllib.parse.quote_plus("S@gbha70561")
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.e1sdj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connect to server
client = MongoClient(uri)

#create database name and colection name
DATABASE_NAME = "deepak"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("D:\sensorproject\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)