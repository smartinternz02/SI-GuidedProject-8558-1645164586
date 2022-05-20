import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "9WKn2IB-NR6JLfkLXGqJdGvF2nD3DNVgDuqIwDs3gZsT"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ['blood_urea','blood glucose random','anemia','coronary_artery_disease','pus_cell','red_blood_cells','diabetesmellitus','pedal_edema'], "values": [[3.1,121.0,0,1,0,1.0,0.0,0.0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b6041104-cc44-4528-b32f-4ec0b5de8af2/predictions?version=2022-03-06', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())