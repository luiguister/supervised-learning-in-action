import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response
from app.identify import model_predict, multiple_model_predict
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'mysecretfortesting'
app.config['SESSION_TYPE'] = 'filesystem'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.form.get('action1') == 'Analizar':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                target_path = os.path.join('src', 'app', app.config['UPLOAD_FOLDER'], filename)
                file.save(target_path)

                prediction = model_predict(target_path)
                file_animal_tuples = [(filename, prediction)]
                resp = make_response(render_template('identify.html', file_animal_tuples=file_animal_tuples))
                return resp
        elif request.form.get('action2') == 'Aleatoreo':
            import random
            dirpath = os.path.join('src', 'app', 'static', 'testdata')

            filenames = random.sample(os.listdir(dirpath), 5)
            files = [os.path.join(dirpath, fname) for fname in filenames]

            animal_tuples = multiple_model_predict(files)

            files = [os.path.join('testdata', fname) for fname in filenames]
            # print(files)
            file_animal_tuples = list(zip(files, animal_tuples))
            # print(file_animal_tuples)

            resp = make_response(render_template('identify.html', file_animal_tuples=file_animal_tuples))
            return resp
        
    return render_template('identify.html')

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)