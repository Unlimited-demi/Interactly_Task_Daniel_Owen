
from pymongo import MongoClient

import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['candidate_db']
profiles_collection = db['profiles']
resumes_collection = db['resumes']

# Insert candidate profiles
profiles_df = pd.read_csv('../data/candidate_data.csv')
profiles_collection.insert_many(profiles_df.to_dict('records'))

# Insert resumes
resumes_df = pd.read_csv('../data/resume.csv')
resumes_collection.insert_many(resumes_df.to_dict('records'))

print("MongoDB setup complete.")
