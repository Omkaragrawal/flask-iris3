from flask import Flask, jsonify, make_response, request, render_template
import pickle
import numpy as np
import os


imp_model = pickle.load(open("model.pkl", 'rb'))


def prediction(req):
    data = req.form or req.get_json(force=True)
    param1 = data["sepalLength"]
    param2 = data['sepalWidth']
    param3 = data['petalLength']
    param4 = data['petalWidth']
    predict_on = np.array([[param1, param2, param3, param4]])
    y_predict = imp_model.predict(predict_on)
    print(y_predict[0])
    return(int(y_predict[0]))


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form:
            return(render_template('index.html', results=prediction(request)))
        else:
            return jsonify(results=prediction(request))
    else:
        return render_template('index.html', results=None)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        if request.form:
            return(render_template('index.html', results=prediction(request)))
        else:
            return jsonify(results=prediction(request))
    else:
        return render_template('index.html', results=None)


# app.run()
if __name__ == '__main__':
    app.run(debug=False if os.environ.get("PORT") else True,
            port=int(os.environ.get("PORT") or 8080))  # 5000)
