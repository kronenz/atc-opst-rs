from flask import Flask
from flask_restx import Api  # Api 구현을 위한 Api 객체 import
from flask_cors import CORS
import openstack as openstack

# openstack.enable_logging(debug=True)
openstack.enable_logging()

from controller.metric import request_service as sh

def create_app():
    app = Flask(__name__)
    app.sdk_connection = openstack.connect(cloud='admin')
    CORS(app)

    api = Api(app)  # Flask 객체에 Api 객체 등록

    from controller.hello import namespace as hello

    api.add_namespace(hello, '/')

    from controller.autoscaling import namespace as autoscaling

    api.add_namespace(autoscaling, '/api')

    from controller.metric.controller_vm import vm_bp as vm
    # app.register_blueprint(controller_vm.vm_bp)
    api.add_namespace(vm, '/metric/vm')
    from controller.metric.controller_host import host_bp as host
    # app.register_blueprint(controller_host.host_bp)
    api.add_namespace(host, '/metric/host')

    print(app.url_map)
    print(app.sdk_connection.auth_token)
    return app
