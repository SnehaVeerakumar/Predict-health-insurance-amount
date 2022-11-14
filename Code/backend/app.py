from flask import Flask, request, url_for, redirect, render_template
import pickle

import numpy as np

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')

Pkl_Filename = "tunedRandomForest.pkl" 
with open(Pkl_Filename, 'rb') as file:  
    model = pickle.load(file)
@app.route('/')

def landing():
    return render_template('landing.html')

@app.route('/form')
def form():
    return render_template('form.html')



@app.route('/predict', methods=['POST','GET'])
def predict():
    variables = [float(x) for x in request.form.values()]
    print(variables)
    value = np.array(variables).reshape((1,6))
    print(value)
    pred = model.predict(value)[0]
    print(pred)

    
    if pred < 0:
        return render_template('predict.html', pred='Error in calculation,Try again.')
    else:
        return render_template('predict.html', pred='{0:.3f}'.format(pred))

if __name__ == '__main__':
    app.run(debug=True)