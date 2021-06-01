import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests
import math
from datetime import date

appp= Flask(__name__)
@appp.route('/')

def home():
	return render_template('index.html')


@appp.route('/predict', methods=['POST'])

def predict():
	try:
		if(request.form.get(["Stock"][0])=='REL'):

			params = {
				'function': 'TIME_SERIES_DAILY',
				'symbol': 'RELIANCE.BSE',
				'outputsize' :'full',
				'apikey' : 'your-api-key'
				#   'query': 'New York'
			}

			api_result = requests.get('https://www.alphavantage.co/query', params)
			api_response = api_result.json()
			arr = list(api_response['Time Series (Daily)'].values())
			Open = float(arr[0]['1. open'])
			high = float(arr[0]['2. high'])
			low = float(arr[0]['3. low'])
			close = float(arr[0]['4. close'])
			volume = float(arr[0]['5. volume'])


			o_c = Open - close
			h_l = high - low

			sum_21 = 0.0
			for i in range(21):
				sum_21 = sum_21 + float(arr[i]['4. close'])	
			
			avg_21 = round(sum_21/21,6)

			sum_7 = 0.0
			for i in range(7):
				sum_7 = sum_7 + float(arr[i]['4. close'])
			avg_7 = round(sum_7/7,6)

			sum_sd = 0
			for i in range(7):
				sum_sd = sum_sd + (float(arr[i]['4. close']) - avg_7)**2
			sd_7 = round(math.sqrt(sum_sd/7),6)

			input = [[volume,o_c,h_l,avg_7,avg_21, sd_7]]
			REL_model= pickle.load(open('C:\\Users\\user\\Desktop\\Projects\\Minor Project - 2\\Deployment\REL model.pkl','rb'))
			prediction= round(REL_model.predict(input)[0],2)



			return render_template('index.html', prediction_text='Prediction of next day Closing Price of Reliance Industries Ltd after date {} is Rs.{}'.format(list(api_response['Time Series (Daily)'].keys())[0],prediction))

		elif(request.form.get(["Stock"][0])=='PFZ'):
			params = {
				'function': 'TIME_SERIES_DAILY',
				'symbol': 'PFE',
				'outputsize' :'full',
				'apikey' : 'your-api-key'
				#   'query': 'New York'
			}

			api_result = requests.get('https://www.alphavantage.co/query', params)
			api_response = api_result.json()
			arr = list(api_response['Time Series (Daily)'].values())
			Open = float(arr[0]['1. open'])
			high = float(arr[0]['2. high'])
			low = float(arr[0]['3. low'])
			close = float(arr[0]['4. close'])
			volume = float(arr[0]['5. volume'])


			o_c = Open - close
			h_l = high - low

			sum_21 = 0.0
			for i in range(21):
				sum_21 = sum_21 + float(arr[i]['4. close'])	
			
			avg_21 = round(sum_21/21,6)

			sum_7 = 0.0
			for i in range(7):
				sum_7 = sum_7 + float(arr[i]['4. close'])
			avg_7 = round(sum_7/7,6)

			sum_sd = 0
			for i in range(7):
				sum_sd = sum_sd + (float(arr[i]['4. close']) - avg_7)**2
			sd_7 = round(math.sqrt(sum_sd/7),6)

			input = [[volume,o_c,h_l,avg_7,avg_21, sd_7]]
			PFZ_model= pickle.load(open('C:\\Users\\user\\Desktop\\Projects\\Minor Project - 2\\Deployment\PFZ model.pkl','rb'))
			prediction= round(PFZ_model.predict(input)[0],2)

			return render_template('index.html', prediction_text='Prediction of next day Closing Price of Pfizer Inc. after date {} is ${}'.format(list(api_response['Time Series (Daily)'].keys())[0],prediction))
		elif(request.form.get(["Stock"][0])=='none'):
			return render_template('index.html', prediction_text='Please Select a Stock to predict')
		else:
			return render_template('index.html', prediction_text='Unable to predict for now..Sorry for inconvenience')
	except:
		return render_template('index.html', prediction_text='Please Check your Internet Connection')


if __name__== "__main__":
	appp.run()
