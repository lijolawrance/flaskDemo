from flask import Flask, jsonify, request
from flask_restful import Api, Resource


def checkPostedData(posted_data, function_name):
    if function_name == "add" or function_name == "subtract" or function_name == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # Missing parameter
        else:
            return 200
    elif function_name == "division":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"]) == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        json_data = request.get_json()
        status_code = checkPostedData(json_data, "subtract")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = json_data['x']
        y = json_data['y']
        z = x + y
        return_json = [
            {
                'Message': z,
                'Status Code': 200
            }
        ]
        return jsonify(return_json)


class Subtract(Resource):
    def post(self):
        json_data = request.get_json()
        status_code = checkPostedData(json_data, "add")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = json_data['x']
        y = json_data['y']
        z = x - y
        return_json = [
            {
                'Message': z,
                'Status Code': 200
            }
        ]
        return jsonify(return_json)


class Multiply(Resource):
    def post(self):
        json_data = request.get_json()
        status_code = checkPostedData(json_data, "multiply")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = json_data['x']
        y = json_data['y']
        z = x * y
        return_json = [
            {
                'Message': z,
                'Status Code': 200
            }
        ]
        return jsonify(return_json)


class Divide(Resource):
    def post(self):
        json_data = request.get_json()
        status_code = checkPostedData(json_data, "division")
        if status_code != 200:
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = json_data['x']
        y = json_data['y']
        z = x / y
        return_json = [
            {
                'Message': z,
                'Status Code': 200
            }
        ]
        return jsonify(return_json)
