from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['candidate_db']
profiles_collection = db['profiles']

df = pd.read_csv('../data/cleaned_candidate_data.csv')

# Ensure that the profiles collection is empty before indexing
profiles_collection.delete_many({})

# Insert profiles into MongoDB
profiles_collection.insert_many(df.to_dict('records'))

print("Indexing complete.")
