from flask import Flask
from flask import request
from flask import jsonify

import machine_learning as ml

import pandas as pd


app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return """<h1>Machine Learning Server</h1>
              <p1><span style="font-weight:bold">Performing following machine learning algorithms:</<span></p1>
               <ol>
                  <li>Logistic Regression</li>
                  <li>Linear Discriminant Analysis</li>
                  <li>K Neighbors Classifier</li>
                  <li>Decision Tree Classifier</li>
                  <li>Gaussian NB</li>
                  <li>Support Vector Machine</li>  
               </ol>  
              <p>Finally for each model compute:</p> 
              <li> Accuracy</li> 
              <li> Precision</li> 
              <li> Recall</li> 
              <li> F1 score</li>"""

@app.route("/perform_ml", methods=['POST'])
def perform_ml():
    post_data = request.get_json()
    ## Use of meta data keys e.g. post_data['date start']
    dataset = pd.DataFrame.from_dict(post_data['payload'], orient='columns')
    model_info = ml.perform_analysis(dataset)
    return jsonify(model_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)