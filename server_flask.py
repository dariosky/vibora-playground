import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.jsonify({'hello': 'world'})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)
