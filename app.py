from flask import Flask, render_template, request
import json
from urllib.request import urlopen
from pprint import pprint
from datetime import date


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'denver'

    api_key = ''
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key + '&units=imperial'

    source = urlopen(url).read()


    list_of_data = json.loads(source)

    pprint(list_of_data)
    today = date.today()
    d1 = today.strftime("%A %b %d")

    data = {
        "city": str(list_of_data['name']),
        "icon": str(list_of_data['weather'][0]['icon']),
        "high": int(list_of_data['main']['temp_max']),
        "low":  int(list_of_data['main']['temp_min']),
        "description": str(list_of_data['weather'][0]['description']
        ),
        "humidity": int(list_of_data['main']['humidity']),
        "wind": int(list_of_data['wind']['speed'])
    }


    return render_template('index.html', data=data, d1=d1)


if __name__ == "__main__":
    app.run(debug=True)
