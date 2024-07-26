from elasticsearch import Elasticsearch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Initialize Elasticsearch
es = Elasticsearch()

# Load the fine-tuned model
tokenizer = GPT2Tokenizer.from_pretrained('../models/fine_tuned_gpt2')
model = GPT2LMHeadModel.from_pretrained('../models/fine_tuned_gpt2')

def retrieve_profiles(job_description):
    response = es.search(
        index='candidates',
        body={
            'query': {
                'match': {
                    'Job Skills': job_description
                }
            }
        }
    )
    return [hit['_source'] for hit in response['hits']['hits']]

def generate_profiles(retrieved_profiles):
    input_text = "Matching profiles:\n" + "\n".join([str(profile) for profile in retrieved_profiles])
    inputs = tokenizer(input_text, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
