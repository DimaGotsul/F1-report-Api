from simplexml import dumps
from flask import Flask, make_response
from flask_restful import Api
from flasgger import Swagger
import swag
import json

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    response = make_response(json.dumps({'response': data}), code)
    response.headers.extend(headers or {})
    return response


@api.representation('application/xml')
def output_xml(data, code, headers=None):
    response = make_response(dumps({'response': data}), code)
    response.headers.extend(headers or {})
    return response


api.add_resource(swag.Report, '/report')
api.add_resource(swag.Report_id, '/report/<string:id>')
api.add_resource(swag.Drivers, '/drivers')
api.add_resource(swag.Driver_id, '/drivers/<string:id>')

if __name__ == '__main__':
    app.run(debug=True, port=2000)
