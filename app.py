from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # render home template
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.form
    # do something with the data 
    print(data)
    processed_data = data
    # render result template with processed data
    return render_template('result.html', data=processed_data)
