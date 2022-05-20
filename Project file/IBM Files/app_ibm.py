from flask import Flask,request, render_template
import numpy as np

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "9WKn2IB-NR6JLfkLXGqJdGvF2nD3DNVgDuqIwDs3gZsT"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/Prediction')
def prediction():
	return render_template('indexnew.html')

@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')

@app.route('/pred',methods=['POST','GET'])# route to show the predictions in a web UI
def pred():
    if request.method == 'POST':
		
        bu = request.form['blood_urea']
       # bu = int(bu)
        bga = request.form['blood glucose random']
       # bga = int(bga)
        ane = request.form['anemia']
        cad = request.form['coronary_artery_disease']
        pc = request.form['pus_cell']
        rbc = request.form['red_blood_cell']
        dbsm = request.form['diabetesmellitus']
        ped = request.form['pedal_edema']
		
        #input_features = [float(x) for x in request.form.values()]
        #features_value = [np.array(input_features)]
        
        features_name = [bu,bga,ane,cad,pc,rbc,dbsm,ped]
        
        payload_scoring = {"input_data": [{"fields": ['blood_urea','blood glucose random','anemia','coronary_artery_disease','pus_cell','red_blood_cells','diabetesmellitus','pedal_edema'], "values": [features_name]}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b6041104-cc44-4528-b32f-4ec0b5de8af2/predictions?version=2022-03-06', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        
        op = response_scoring.json()
        output = op['predictions'][0]['values'][0][0]
       
    # showing the prediction results in a UI# showing the prediction results in a UI
        return render_template('result.html', prediction_text=output)

if __name__ == '__main__':
    # running the app
    app.run(debug=False)	