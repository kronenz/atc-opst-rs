from flask import current_app
from flask import jsonify
import pprint
from flask_restx import Namespace, Resource, marshal 

pp = pprint.PrettyPrinter()


from controller.metric import vm_service as vs
rs = vs.vm_service()

vm_bp = Namespace('vm')

@vm_bp.route("/cpu")
class get_cpu(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cpu(auth_token)
        return jsonify(data)

@vm_bp.route("/cluster/cpu") # 클러스터별 cpu 사용량 조회
class get_cluster_cpu(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cluster_cpu(auth_token)
        return data

@vm_bp.route("/clusterlist") # 클러스터별 cpu 사용량 조회
class get_cluster_list(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cluster_list(auth_token)
        return data


@vm_bp.route("/vcpus")
class get_vcpus(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_vcpus(auth_token)
        return jsonify(data)

@vm_bp.route("/memory")
class get_memory(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_memory(auth_token)
        return jsonify(data) 

@vm_bp.route("/mem_usage")
class get_mem_usage(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_mem_usage(auth_token)
        return jsonify(data)  

@vm_bp.route("/net_in_bytes")
class get_net_in_bytes(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_in_bytes(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_in_packets_error")
class get_net_in_packets_error(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_in_packets_error(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_in_packets_drop")
class get_net_in_packets_drop(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_in_packets_drop(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_in_packets")
class get_net_in_packets(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_in_packets(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_out_bytes")
class get_net_out_bytes(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_out_bytes(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_out_packets")
class get_net_out_packets(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_out_packets(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_out_packets_drop")
class get_net_out_packets_drop(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_out_packets_drop(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_out_packtes_error")
class get_net_out_packets_error(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_out_packets_error(auth_token)
        return jsonify(data) 

@vm_bp.route("/net_out_packtes")
class get_net_out_packtes(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_net_out_packtes(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_root_size")
class get_disk_root_size(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_root_size(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_ephemeral_size")
class get_disk_ephemeral_size(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_ephemeral_size(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_allocation")
class get_disk_device_allocation(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_allocation(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_capacity")
class get_disk_device_capacity(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_capacity(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_usage")
class get_disk_device_usage(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_usage(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_read_bytes")
class get_disk_device_read_bytes(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_read_bytes(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_read_latency")
class get_disk_device_read_latency(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_read_latency(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_read_requests")
class get_disk_device_read_requests(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_read_requests(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_write_bytes")
class get_disk_device_write_bytes(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_write_bytes(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_write_latency")
class get_disk_device_write_latency(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_write_latency(auth_token)
        return jsonify(data) 

@vm_bp.route("/disk_device_write_requests")
class get_disk_device_write_requests(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_disk_device_write_requests(auth_token)
        return jsonify(data) 

@vm_bp.route("/network_all")
class get_network_all_requests(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_network_all(auth_token)
        return data 

@vm_bp.route("/network_all_proejct")
class get_network_all_requests(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_network_all_proejct(auth_token)
        return data 

@vm_bp.route("/cluster_all")
class get_cluster_all(Resource):
    def get(self):
        auth_token = current_app.sdk_connection.auth_token
        data = rs.get_cluster_all(auth_token)
        return data