from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import calculator as calc

app = Flask(__name__)

api = Api(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Lijo sends Hello World!'


@app.route('/add_nums', methods=['POST'])
def add_nums():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y
    ret_JSON = [
        {
            "z": z
        }
    ]
    return jsonify(ret_JSON)


@app.route('/me2')
def call_me():  # put application's code here
    json_data = {
        "Name": "Lijo Lawrance",
        "Age": 38,
        "Phones": [
            {
                "phoneName": "Nokia",
                "phonenumber": 21290
            },
            {
                "phoneName": "Moto",
                "phonenumber": 213290
            }

        ]

    }
    return jsonify(json_data)


api.add_resource(calc.Add, "/add")
api.add_resource(calc.Subtract, "/subtract")
api.add_resource(calc.Multiply, "/multiply")
api.add_resource(calc.Divide, "/divide")
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
