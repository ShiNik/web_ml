from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import send_file
from flask import send_from_directory

from werkzeug.utils import secure_filename

from flask_package import app
from flask_package import db

from flask_package.database import FileContents, get_results, get_result

import requests

import pandas as pd
import os

@app.route('/')
@app.route('/home')
def home():
    ml_results = get_results()
    return render_template('home.jinja2', ml_results=ml_results)


@app.route('/ml_result/<int:result_id>')
def ml_result(result_id):
    result = get_result(result_id)
    if not result:
        return render_template('404.jinja2', message=f'A post with id {result_id} was not found.')
    return render_template('result.jinja2', result=result, title='Result')



@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory("./static/upload_db",
                               filename)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file_name = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

            file.save(file_path)
            if request.form['submit_button'] == 'Download':
            
                return redirect(url_for('download_file',
                                        filename=file.filename, title='Upload new File'))
            elif request.form['submit_button'] == 'Analysis':
                allmodels = []
                df = pd.read_csv(file_path)

                dataset = df.to_dict(orient='list')
                post_data = {'dataset ID': "makis", 'date start': "1", 'date end': "2", 'payload': dataset}
                #in docker set url to "http://ml:5002/perform_ml"
                #outside docker set url to "http://localhost:5002/perform_ml"
                url = "http://ml:5002/perform_ml" if app.config['RUNFROMDOCKER'] else "http://localhost:5002/perform_ml"

                respond  = requests.post(url, json=post_data)
                model_info = respond.json()

                for model_name, result in model_info.items():
                    allmodels.append(result)

                    # Saving Results of Uploaded Files  to Sqlite DB
                    newfile = FileContents(name=file.filename,data=file.read(),modeldata=result["results"], report=result["report"])
                    db.session.add(newfile)
                    db.session.commit()

                return render_template('analysis.html',file_name=file_name, file_path = file_path, df_table=df, model_info = allmodels) 
            else:
                pass # unknown

    return render_template('upload_file.html') 





 