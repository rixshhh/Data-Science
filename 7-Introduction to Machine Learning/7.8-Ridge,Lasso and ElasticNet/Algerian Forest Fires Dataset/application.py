from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## Import models
Lasso_cv = pickle.load(open('models/lasso_cv.pkl','rb'))
Scaler = pickle.load(open('models/scaler.pkl','rb'))


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predictData',methods=['GET','POST'])
def predict_Data():
    if request.method == 'POST':
        try:
            # Collect input data from the form
            Temp = float(request.form.get('Temp'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            DC = float(request.form.get('DC'))
            BUI = float(request.form.get('BUI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Create an array for the model
            input_data = np.array([[Temp, RH, Ws, Rain, FFMC, DMC, ISI,DC,BUI, Classes, Region]])

            # Scale it using the same scaler used during training
            scaled_data = Scaler.transform(input_data)

            # Predict using the trained model
            prediction = Lasso_cv.predict(scaled_data)

            result = round(prediction[0], 2)

            return render_template('home.html', result_text=f'🔥 Predicted Fire Weather Index (FWI): {result}')

        except Exception as e:
            return render_template('home.html', result_text=f'Error: {str(e)}')
    else:
        return render_template('home.html')
    

if __name__ == "__main__":
    app.run(debug=True)
