from flask import Flask, request, jsonify
from llm.rag import retrieve_profiles, generate_profiles

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match_profiles():
    job_description = request.json['job_description']
    retrieved_profiles = retrieve_profiles(job_description)
    generated_profiles = generate_profiles(retrieved_profiles)
    return jsonify(generated_profiles)

if __name__ == '__main__':
    app.run(debug=True)
