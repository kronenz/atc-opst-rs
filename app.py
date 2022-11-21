from flask import Flask
from flask_restx import Api  # Api 구현을 위한 Api 객체 import
from flask_cors import CORS
import openstack as openstack

# openstack.enable_logging(debug=True)
openstack.enable_logging()

from controller.metric import request_service as sh

from apscheduler.schedulers.background import BackgroundScheduler



from controller.metric import vm_service as vs

sdk_conn = openstack.connect(cloud='admin')
rs = vs.vm_service()

collection_interval=60 #1분에 한번 동작

def elk_bulk_sender():
    print('call elk_bulk_sender')
    token = sdk_conn.auth_token
    data = rs.net_data_elk_bulk(token)
    rs.cluster_cpu_data_elk_bulk(token)
    ##전송 코드

sched = BackgroundScheduler(daemon=True)
sched.add_job(elk_bulk_sender, 'interval', seconds=collection_interval)
sched.start()

def create_app():
    app = Flask(__name__)
    app.sdk_connection = sdk_conn
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
