from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def simple_sum():

    a = request.args.get('a',type = int)
    b = request.args.get('b',type = int)

    return jsonify(res=a+b)

app.run()
