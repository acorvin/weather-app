from flask import Flask, render_template, request
import json
from urllib.request import urlopen
from pprint import pprint

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'denver'

    api_key = ''
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

    source = urlopen(url).read()

    list_of_data = json.loads(source)

    data = {
        "city": str(list_of_data['name']),
        "temp": int(list_of_data['main']['temp'] - 273.15),
        "description": str(list_of_data['weather'][0]['description']),
    }

    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
