import numpy as np
from flask import Flask, request, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/crop-predict')
def crop_prediction():
  return render_template('predict.html')

@app.route("/crop-predict", methods = ['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("predict.html", prediction_text = "{}".format(listToString(prediction)))

def listToString(prediction): 
    str = "" 
    for label in prediction: 
        str += label  
    return str.title()

if __name__ == "__main__":
    app.run(debug=True)