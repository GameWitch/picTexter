from OCR import ocr_read
from Translate import translate
import os
from flask import Flask, render_template, request


app = Flask(__name__)
UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":

        allowed_files = []
        for file in request.files.getlist("files"):
            if allowed_file(file.filename):
                allowed_files.append(file)

        if allowed_files:
            img_srcs = []
            for img in allowed_files:
                img.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, img.filename))
                img_srcs.append(UPLOAD_FOLDER + img.filename)

            trans_lang = request.form["translate"]
            language = request.form["language"]
            text_list = [ocr_read(file, language) for file in allowed_files]

            trans_list = [translate(text, trans_lang) for text in text_list]
            return render_template("index.html", text_list=trans_list, msg="Arguably a Success!", imgs=img_srcs)
        else:
            return render_template("index.html", msg="No Allowed Files")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
