import requests
import json

url = "https://vllm-hf-v1.eastus2.inference.ml.azure.com/v1/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer xxxxxxxxxxxxxx"
}
data = {
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "prompt": "San Francisco is a",
    "max_tokens": 200,
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

json_formatted_str = json.dumps(response.json(), indent=4)
print(json_formatted_str)
