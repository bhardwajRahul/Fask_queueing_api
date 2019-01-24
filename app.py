from flask import Blueprint
from flask_restful import Api
from resources.User import UserResource
from resources.Task import TaskResource, TaskIdResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route For user endpoints
api.add_resource(UserResource, '/users')

# #Route for File Upload endpoints
api.add_resource(TaskResource, '/upload')
api.add_resource(TaskIdResource, '/upload/<task_id>')
