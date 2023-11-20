import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    # Get values from the form and convert them to appropriate types
    age = int(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']

    # Create a DataFrame with the input features
    data = {'age': [age], 'sex': [sex], 'bmi': [bmi], 'children': [children], 'smoker': [smoker], 'region': [region]}
    x = pd.DataFrame(data)
    prediction = model.predict(x)

    # Round the prediction to two decimal places
    output = round(prediction[0], 2)

    return render_template('index.html', prediction='Le montant annuel des charges pour ce nouveau client est de '
                                                         '${}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
