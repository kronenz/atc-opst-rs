from flask import current_app
from flask import jsonify
import pprint
from flask_restx import Namespace, Resource, marshal 

pp = pprint.PrettyPrinter()

from controller.cluster import cluster_service as cs
from controller.metric import vm_service as cs
csservice = cs.cluster_service()

vm_bp = Namespace('cluster')

@vm_bp.route("/all")
class get_cluster_all(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = csservice.get_cluster_all(auth_token)
        return data