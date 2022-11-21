import requests
import json
import yaml
import pprint

class request_api:
    ip_address = 0
    port = 0
    base_url = ''

    def __init__(self):
        with open('metrics.yaml') as f:
            yamlLoad = yaml.load(f, Loader=yaml.FullLoader)
            metrics = yamlLoad['metrics']
            api = metrics['api']
            self.ip_address = str(api['ip'])
            self.port = str(api['port'])
            self.base_url = 'http://' + self.ip_address + ':' + self.port + '/v1/'

    def post_with_x_auth(self, path, auth_token, jsonBody):
        """접근경로와 인증토큰은 입력하면 REST API JSON resultf를 반환하는 함수
        http://hostip:port/v1/경로 에서 경로만 path에 입력하면 된다 기본 주소와 포트는 metrics.yaml 파일에서 가져와서 처리
        
        Args:
            path (string): api요청 경로
            auth_token (_type_): openstack admin auth token

        Raises:
            Exception: 토큰값이 비어있을 경우 예외 발생
        """

        if auth_token == '':
            raise Exception("auth_token is Empty. please set_token")

        url = self.base_url + path
        headers = {'X-Auth-Token': auth_token}
        r=requests.post(url, headers=headers, json=jsonBody)
        return (json.loads(r.text))
