import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.jsonify({'server': 'flask'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
