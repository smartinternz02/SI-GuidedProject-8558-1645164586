from flask import Flask,request, render_template
import numpy as np
import pandas as pd
import pickle

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
        model = pickle.load(open('CKD.pkl','rb'))
		
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
		
        input_features = [float(x) for x in request.form.values()]
        features_value = [np.array(input_features)]
        
        features_name = [bu,bga,ane,cad,pc,rbc,dbsm,ped]
        
        df=pd.DataFrame(features_value, columns=features_name)
    
    # predictions using the loaded model file
        output = model.predict(df)
    # showing the prediction results in a UI# showing the prediction results in a UI
        return render_template('result.html', prediction_text=output)

if __name__ == '__main__':
    # running the app
    app.run(debug=True)	