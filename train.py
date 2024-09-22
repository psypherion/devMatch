import json
import os
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the JSON file containing the repository data
with open('db/repositories.json', 'r') as f:
    repo_data = json.load(f)

# Load the Falcon 7B model and tokenizer
model_name = "huggingface/falcon-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def process_files_in_repo(file_path):
    # List to hold the contents of the files
    file_contents = []
    
    # Iterate through the files in the given directory
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith(('.py', '.md', '.txt')):  # You can add more file types if needed
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    file_contents.append(content)
    
    return file_contents

def learn_from_files(file_contents):
    for content in file_contents:
        # Tokenize the content
        inputs = tokenizer(content, return_tensors='pt', truncation=True)
        # Generate output
        outputs = model.generate(**inputs)
        decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(decoded_output)  # or save/process the output as needed

# Process each repository
for repo in repo_data:
    repo_path = repo['file_path']
    if os.path.exists(repo_path):
        print(f"Processing repository: {repo['repo_name']} at {repo_path}")
        contents = process_files_in_repo(repo_path)
        learn_from_files(contents)
    else:
        print(f"Repository path does not exist: {repo_path}")
