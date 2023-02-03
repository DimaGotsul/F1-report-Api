from src.resorses.resours import built_report, page_driver
from flask_restful import Resource, abort


def abort_if_todo_doesnt_exist(drivers_id):
    if drivers_id not in page_driver().keys():
        abort(404, message="Todo {} doesn't exist".format(drivers_id))


class Report(Resource):
    def get(self):
        """     This is method for getting all report
                ---
                produces:
                  - application/json
                  - application/xml
                responses:
                  200:
                    description: All report  """
        return built_report()


class Report_id(Resource):
    def get(self, id):
        """     This is method for getting info about certain drivers in race
        ---
        parameters:
          - in: path
            name: id
            type: string
            required: true
        produces:
        - application/json
        - application/xml
        responses:
          200:
            description: A single user item
          """
        report = built_report()
        abort_if_todo_doesnt_exist(id)
        return report[id]


class Drivers(Resource):
    def get(self):
        """     This is method for getting all drivers
        ---
        produces:
        - application/json
        - application/xml
        responses:
          200:
            description: All report  """
        return page_driver()


class Driver_id(Resource):
    def get(self, id):
        """
        This is method for getting info about certain drivers
        ---
        parameters:
          - in: path
            name: id
            type: string
            required: true
        produces:
          - application/json
          - application/xml
        responses:
          200:
            description: A single user item
          """
        drivers = page_driver()
        abort_if_todo_doesnt_exist(id)
        return drivers[id]
