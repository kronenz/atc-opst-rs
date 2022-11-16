# from flask import Flask
# from controller.metric.controller_vm import vm_bp
# from controller.metric.controller_host import host_bp

# app = Flask(__name__)

# app.register_blueprint(vm_bp)
# app.register_blueprint(host_bp)

from flask import current_app, Blueprint
from flask import jsonify

#hardware.cpu.load.15min	process	host ID	CPU load in the past 15 minutes
#hardware.cpu.load.1min	process	host ID	CPU load in the past 1 minute
#hardware.cpu.load.5min	process	host ID	CPU load in the past 5 minutes
#hardware.cpu.util	%	host ID	cpu usage percentage
#hardware.system_stats.cpu.idle	%	host ID	CPU idle percentage
from controller.metric import host_service as hs

host_bluepoint = Blueprint('metric_host_test', __name__, url_prefix='/metric/bphost')
rs = hs.host_service()

@host_bluepoint.route("/cpu15min")
def get_cpu_load_15min():
    auth_token = current_app.sdk_connection.auth_token
    data = rs.get_cpu_load_15min(auth_token)
    return jsonify(data) 