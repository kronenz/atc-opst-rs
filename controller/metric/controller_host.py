from flask import current_app
from flask import jsonify
import pprint
from flask_restx import Namespace, Resource, marshal 

pp = pprint.PrettyPrinter()

#hardware.cpu.load.15min	process	host ID	CPU load in the past 15 minutes
#hardware.cpu.load.1min	process	host ID	CPU load in the past 1 minute
#hardware.cpu.load.5min	process	host ID	CPU load in the past 5 minutes
#hardware.cpu.util	%	host ID	cpu usage percentage
#hardware.system_stats.cpu.idle	%	host ID	CPU idle percentage
from controller.metric import host_service as hs

rs = hs.host_service()

host_bp = Namespace('host')

@host_bp.route("/cpu15min")
class get_cpu_load_15min(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cpu_load_15min(auth_token)
        return jsonify(data) 

@host_bp.route("/cpu1min")
class get_cpu_load_1min(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cpu_load_1min(auth_token) 
        return jsonify(data)

@host_bp.route("/cpu5min")
class get_cpu_load_5min(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cpu_load_5min(auth_token)
        return jsonify(data)

@host_bp.route("/cpu_util")
class get_cpu_util(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cpu_util(auth_token) 
        return jsonify(data) 

@host_bp.route("/cpu_idle")
class get_cpu_idle(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cpu_idle(auth_token)
        return jsonify(data) 

@host_bp.route("/mem_buffer")
class get_mem_buffer(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_mem_buffer(auth_token)
        return jsonify(data) 

@host_bp.route("/mem_cached")
class get_mem_cached(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_mem_cached(auth_token) 
        return jsonify(data)

@host_bp.route("/mem_swap_avail")
class get_mem_swap_avail(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_mem_swap_avail(auth_token)
        return jsonify(data) 

@host_bp.route("/mem_swap_total")
class get_mem_swap_total(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_mem_swap_total(auth_token)
        return jsonify(data) 

@host_bp.route("/mem_total")
class get_mem_total(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_mem_total(auth_token) 
        return jsonify(data) 

@host_bp.route("/mem_used")
class get_mem_used(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_mem_used(auth_token)
        return jsonify(data) 

@host_bp.route("/net_in_bytes")
class get_net_in_bytes(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_in_bytes(auth_token)
        return jsonify(data) 

@host_bp.route("/net_out_bytes")
class get_net_out_bytes(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_out_bytes(auth_token) 
        return jsonify(data)  

@host_bp.route("/disk_size_total")
class get_disk_size_total(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_size_total(auth_token)
        return jsonify(data) 

@host_bp.route("/disk_size_used")
class get_disk_size_used(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_size_used(auth_token)
        return jsonify(data) 