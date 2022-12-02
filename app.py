from flask import Flask, request, url_for, redirect, render_template
import pickle
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder='Code/frontend', static_folder='Code/frontend/static')

Pkl_Filename = "dnn.pkl" 
with open(Pkl_Filename, 'rb') as file:  
    model = pickle.load(file)
@app.route('/')

def landing():
    return render_template('landing.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')


df = pd.read_csv('./Dataset/processedData.csv')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_training = scaler.fit_transform(df)

@app.route('/predict', methods=['POST','GET'])
def predict():
    arr = [float(x) for x in request.form.values()]
    print(arr)
    dummy = 0
    arr =  np.insert(arr, 6, dummy)
    print(arr)
    testval = pd.DataFrame((arr).reshape(1,7))
    testval = scaler.transform(testval)
    array = np.delete(testval,-1)
    print(array)
    pred = model.predict(array.reshape(1,6))
    print(pred)
    pred = pred + 0.017907
    pred = pred/0.0000159621
    pred
    print(pred)
    
    if pred < 0:
        return render_template('predict.html', pred='Error in calculation,Try again.')
    else:
        return render_template('predict.html', pred='{0:.3f}'.format(pred[0][0]))

if __name__ == '__main__':
    app.run(host='0.0.0.0')