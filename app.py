from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from ds_comp.prediction import *

app = Flask(__name__)


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_text/', methods=['POST', 'GET'])
def upload_image():
    # if request.method == 'POST':
    #     # checking for file
    #     if 'file' not in request.files:
    #         print('no file')
    #         return redirect('/')
    #     file = request.files['file']
    #     if file.filename == '':
    #         print('no selected file')
    #         return redirect('/')
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    text = request.form['text']
    processed_text = text.lower()

    print(processed_text)
    obj = Prediction(processed_text)
    prediction = obj.make_pred()

    print(prediction)
    # if rice is predicted:
    # prediction = 'rice'

    return render_template('index.html', prediction=prediction, text=processed_text)


# return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
