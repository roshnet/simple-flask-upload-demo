from flask import (
    Flask,
    render_template,
    request
)
import os

app = Flask(__name__)
app.config['DEBUG'] = True

UPLOAD_FOLDER = 'static/images'


@app.route('/')
def home():
    return render_template("upload.html")


@app.route('/upload', methods=['POST'])
def upload():
    if not request.method == 'POST':
        return render_template("upload.html")

    image = request.files['image']
    save_to_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(save_to_path)
    return render_template("upload.html",
                           image=image.filename)
