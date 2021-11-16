from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def code():
    code_value = request.args.get("code", "no code")
    return "The code is: {}".format(code_value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
