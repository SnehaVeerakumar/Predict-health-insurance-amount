from flask import Flask, request, url_for, redirect, render_template,Response
from flask import *
import pickle
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense
from adjustText import adjust_text
import math

app = Flask(__name__, template_folder='Code/frontend', static_folder='Code/frontend/static')

model = pickle.load(open( "dnn_model.pkl", "rb" ))

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/form')
def form():
    return render_template('form.html')
app.secret_key = "abc"  
@app.route('/forecast')
def forecast():
    return render_template('forecast.html')
app.config['file_upload'] = 'Dataset'
@app.route('/forecasted', methods=['POST','GET'])
def forecasted():
    if request.form['action'] == 'Upload':
        if request.method == 'POST':
            file = request.files['file']
            file.save(os.path.join(app.config['file_upload'],"data.csv"))
            flash("File uploaded.")  
            return redirect("forecast")
        return render_template('forecast.html')
    elif request.form['action'] == 'Forecast':
        data = pd.read_csv('Dataset/data.csv')
        expense = pd.DataFrame(data['Amount'])
        scaler = StandardScaler()
        scaled_expense=scaler.fit_transform(expense)
        train_size = 36
        lookback=12
        train_amount = scaled_expense[0:train_size,:]
        test_requests = scaled_expense[train_size-lookback:,:]

        def create_rnn_dataset(data1,lookback=1):
            data_x,data_y = [],[]
            for i in range(len(data1) - lookback -1):
                a=data1[i:(i+lookback),0]
                data_x.append(a)
                data_y.append(data1[i+lookback,0])
            return np.array(data_x),np.array(data_y)
        
        train_x,train_y = create_rnn_dataset(train_amount,lookback)
        train_x = np.reshape(train_x,(train_x.shape[0],1, train_x.shape[1]))
        tf.random.set_seed(3)
        ts_model=Sequential()
        ts_model.add(LSTM(256, input_shape=(1,lookback)))
        ts_model.add(Dense(1))
        ts_model.compile(loss="mean_squared_error",optimizer="adam",metrics=["mse"])
        ts_model.fit(train_x, train_y,  epochs=5, batch_size=1, verbose=1)
        test_x, test_y = create_rnn_dataset(test_requests,lookback)
        test_x = np.reshape(test_x,(test_x.shape[0],1, test_x.shape[1]))
        ts_model.evaluate(test_x, test_y, verbose=1)
        predict_on_train= ts_model.predict(train_x)
        predict_on_test = ts_model.predict(test_x)
        predict_on_train = scaler.inverse_transform(predict_on_train)
        predict_on_test = scaler.inverse_transform(predict_on_test) 
        curr_input= test_x[-1,:].flatten()
        predict_for = 12

        for i in range(predict_for):
            this_input = curr_input[-lookback:] # X = Last no.of.samples
            this_input = this_input.reshape((1,1,lookback))
            this_prediction = ts_model.predict(this_input) #Predict next data point
            curr_input = np.append(curr_input,this_prediction.flatten())
        
        # Last "predict_for" of curr_input contains all new predictions
        predict_on_future=np.reshape(np.array(curr_input[-predict_for:]),(predict_for,1))
        # Inverse scale
        predict_on_future=scaler.inverse_transform(predict_on_future)

        data['Date'] = pd.to_datetime(data['Date'])
        dfd = data['Date'] + pd.DateOffset(months=predict_for)
        d1 = dfd.dt.to_period('M')
        d1 = d1.iloc[2:]
        d1.astype(str)

        total_size = len(predict_on_train) + len(predict_on_test) + len(predict_on_future)

        #Training data predictions
        predict_train_plot = np.empty((total_size,1))
        predict_train_plot[:, :] = np.nan
        predict_train_plot[0:len(predict_on_train), :] = predict_on_train

        #Test data predictions
        predict_test_plot = np.empty((total_size,1))
        predict_test_plot[:, :] = np.nan
        predict_test_plot[len(predict_on_train):len(predict_on_train)+len(predict_on_test), :] = predict_on_test

        # Future forecast dataset
        predict_future_plot = np.empty((total_size,1))
        predict_future_plot[:, :] = np.nan
        predict_future_plot[len(predict_on_train)+len(predict_on_test):total_size, :] = predict_on_future

        df = np.concatenate((predict_on_train, predict_on_test,predict_on_future))

        plt.figure(figsize=(20,10)).suptitle("Plot Predictions for Training, Test & Forecast Data", fontsize=20,)
        plt.xticks(np.arange(len(d1)),d1,rotation=30)
        plt.plot(predict_train_plot)
        plt.plot(predict_test_plot)
        plt.plot(predict_future_plot)
        plt.xlabel("Date")
        plt.ylabel("Amount")
        texts = []
        for i, v in enumerate(df):
                if(i >=len(predict_on_train)+len(predict_on_test)):
                        texts.append(plt.text(math.floor(i), v+25, "%d" %v, ha="center"))
        adjust_text(texts, only_move={'points':'y', 'texts':'xy'})
        plt.savefig('code/frontend/static/img/forecast.png', transparent=True)
        return render_template('forecasted.html')
    
@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/download')
def download():
    with open("Dataset/monthlyExpense.csv") as fp:
        csv = fp.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=sample.csv"}) 
    

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
    app.run(host='0.0.0.0', port=5000)
