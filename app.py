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

    api_key = '1a2a53786528a614d77ac2fe9d43dd7f'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

    source = urlopen(url).read()

    list_of_data = json.loads(source)

    pprint(list_of_data)

    data = {
        "city": str(list_of_data['name']),
        "temp": int(list_of_data['main']['temp'] - 273.15),
        "description": str(list_of_data['weather'][0]['description']),
    }

    return render_template('index.html', data=data)

# data = res.json()

# temp = data['main']['temp']

# celcius = int(temp - 273.15)


if __name__ == "__main__":
    app.run(debug=True)
