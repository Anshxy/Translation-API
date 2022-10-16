from googletrans import Translator #Version: googletrans==3.1.0a0
from flask import Flask
import json

app = Flask(__name__)

def translation(text, d=None):

    t = Translator()

    if d is None:
        d='en'

    tr = t.translate(str(text), dest=d )

    print(tr)

    return tr.text, #tr.src, tr.dest

app

@app.route('/<incoming_text>')
def profile(incoming_text):
    tr = translation(incoming_text)

    a = {"translated": tr}

    data_ = json.dumps(a)

    return data_


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')