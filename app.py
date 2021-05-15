from flask import Flask, jsonify, make_response, request, render_template
from flask_cors import CORS
import pickle
import numpy as np
import os


def predictions(req):
    data = req.form or req.get_json(force=True)
    param1 = data["sepalLength"]
    param2 = data['sepalWidth']
    param3 = data['petalLength']
    param4 = data['petalWidth']
    predict_on = np.array([[param1, param2, param3, param4]])
    y_predict = imp_model.predict(predict_on)
    print("Prediction:", int(y_predict[0]))
    return(y_predict[0])


imp_model = pickle.load(open("model.pkl", 'rb'))

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == 'POST':
        # return jsonify(results = int(predictions(request)))
        # return render_template('index.html', results = int(predictions(request)))

        if request.form:
            return render_template('index.html', results=int(predictions(request)))
        else:
            return jsonify(results=int(predictions(request)))

    else:
        return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # return jsonify(results = int(predictions(request)))

        if request.form:
            return render_template('index.html', results=int(predictions(request)))
        else:
            return jsonify(results=int(predictions(request)))

    else:
        # return ("Server is up and running on /predict ...")
        return render_template('index.html', results="undefined")


# app.run()
if __name__ == '__main__':
    app.run(debug=False if os.environ.get("PORT") else True,
            port=int(os.environ.get("PORT") or 8080))  # 5000)
