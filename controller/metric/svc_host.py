import yaml
import pprint
import json

from controller.metric import request_api as ra
rapi = ra.RequestAPI()

class HostService():
    reqPath = 'aggregates?granularity={}&groupby=id'
    host = None
    pp = None
    def __init__(self):
        with open('host_req_body.yaml') as f:
            self.host = yaml.load(f, Loader=yaml.FullLoader)
            
    def getCpuLoad15Min(self, auth_token):
        print('getCpuLoad15Min')
        item = self.host['Host_hardware.cpu.util']
        jsonBody = item['body']
        granularity = item['granularity']
        self.reqPath = self.reqPath.format(granularity)
        resultJson = rapi.post_with_x_auth(self.reqPath, auth_token, jsonBody)
        return resultJson