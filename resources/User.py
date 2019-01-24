from flask import request, jsonify
from flask_restful import Resource
from model import redis_cache, UserModel


from ast import literal_eval


class UserResource(Resource):
    
    def get(self):

        platform = request.args['platform']
        if redis_cache.exists(platform):
            response_object = redis_cache.__getitem__(platform)
            response_object = literal_eval(response_object.decode('utf8'))
        else:          
            uid = UserModel.query.filter_by(platform=platform).count()
            uuid = UserModel.query.with_entities(UserModel.user_id).filter_by(platform=platform).distinct().count()
            all_user = UserModel.query.count()
            platform_share = round(100 * uid / all_user, 2)

            if uid and uuid:
                response_object = {
                    'data': {
                        'platform_users': uid,
                        'unique_users': uuid,
                        'percentage_share': platform_share
                    }
                }
                redis_cache.__setitem__(platform, response_object)
            else:
                response_object = {'status': 'error'}
        return jsonify(response_object)

