from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from datetime import datetime
from db_operations import *
import log


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
        base = os.path.basename(path)
        log.log_msg("Saving file to db: " + base)
        insert_into_database(base)
        file.save(path)
        return "File has been uploaded."
    data = get_all_pictures()
    pic_path = "static/files/"
    return render_template('index.html', form=form, data=data, pic_path=pic_path)

if __name__ == '__main__':
    app.run(debug = True, ssl_context = "adhoc")
