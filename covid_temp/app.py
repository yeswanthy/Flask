from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

def get_data():
    with open('covid.json', 'r') as file:
        scrap = json.load(file)
    return scrap


@app.route('/')
def home():
    data = get_data()
    return render_template('home.jinja2', states=data)

@app.route('/<state_name>')
def state(state_name):
    data = get_data()
    state_data = data.get(state_name)
    return render_template('state.jinja2', state_data=state_data)


if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=5001)
