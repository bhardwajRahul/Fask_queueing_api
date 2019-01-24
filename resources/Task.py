from flask import request, jsonify
from flask_restful import Resource
import redis
from rq import Queue, Worker, Connection
from config import WorkerConfig
from tasks import create_task

with Connection(redis.from_url(WorkerConfig.REDIS_URL)):
    queue = Queue(WorkerConfig.QUEUES)
    worker = Worker(WorkerConfig.QUEUES)


class TaskResource(Resource):

    def post(self):

        task_type = request.files.getlist("file")
        task = queue.enqueue(create_task, task_type)
        response_object = {
            'status': 'success',
            'data': {
                'task_id': task.get_id()
            }
        }
        return jsonify(response_object)


class TaskIdResource(Resource):

    def get(self, task_id):

        task = queue.fetch_job(task_id)
        if task:
            response_object = {
                'status': 'success',
                'data': {
                    'task_id': task.get_id(),
                    'task_status': task.get_status(),
                    'task_result': task.result
                }
            }
        else:
            response_object = {'status': 'error'}
        return jsonify(response_object)
