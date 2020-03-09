from flask import Flask
from flask import request
from flask import jsonify

import machine_learning as ml

import pandas as pd


app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return "Ml manager"

@app.route("/perform_ml", methods=['POST'])
def perform_ml():
    post_data = request.get_json()
    ## Use of meta data keys e.g. post_data['date start']
    dataset = pd.DataFrame.from_dict(post_data['payload'], orient='columns')
    model_info = ml.perform_analysis(dataset)
    return jsonify(model_info)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80, debug=True)
    app.run(host='127.0.0.1', port=5002, debug=True)