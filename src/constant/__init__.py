import os
from urllib.parse import quote_plus

AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "deepak"
MONGO_COLLECTION_NAME = "waferfault"
passkey="S@gbha70561"
username = "deepak70561"
# Escape the username and password using urllib.parse.quote_plus
encoded_username = quote_plus(username)
encoded_password = quote_plus(passkey)
TARGET_COLUMN = "quality"
MONGO_DB_URL=f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.e1sdj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"