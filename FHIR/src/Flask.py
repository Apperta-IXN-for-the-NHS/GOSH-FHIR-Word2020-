# Patient Health Records Generator

# I developed a web application in Flask which uses a Python API for creating and
# updating Microsoft Word. I also used FHIR Parser which made it easier for me to
# access the information that I needed from HL7 FHIR.

# Sabina-Maria Mitroi - 18.03.2020


from flask import Flask, render_template, request
import main

app = Flask(__name__, static_folder='static')


# Homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route('/gen_doc', methods=['GET', 'POST'])
def gen_doc():
    text = request.form["text"]
    dropdown = request.form["dropdown"]
    print(text)
    print(dropdown)
    main.save_doc(text, dropdown)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port = 677)