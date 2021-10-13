from flask import Flask
from datetime import datetime as dt

app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    output = {'data': 'Hello Flask!'}
    return output


@app.route('/current_datetime', methods=['GET'])

def datetime():
    date_hour = dt.now().strftime('%d/%m/%Y %H:%M:%S %p')
    hour = dt.now().hour

    if hour < 12:
        message = "Bom dia!"
    elif hour < 18:
        message = "Boa tarde!"
    else:
        message = "Boa noite!"

    output = {'current_datetime': date_hour, 'message': message}

    return output
