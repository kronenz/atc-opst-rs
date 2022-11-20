import requests
import json
import yaml
import pprint

class post_elk:
    ip_address = 0
    port = 0
    base_url = ''

    def __init__(self):
        with open('elk.yaml') as f:
            yamlLoad = yaml.load(f, Loader=yaml.FullLoader)
            server = yamlLoad['server']
            api = server['api']
            self.ip_address = str(api['ip'])
            self.port = str(api['port'])
            self.base_url = 'http://' + self.ip_address + ':' + self.port + '/'

    def post_bulk(self, name, auth_token, jsonList):
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


        headers={           
                            # it's a requirement
                            'Content-Type': 'application/x-ndjson'
                        }
        url = self.base_url + name + "/_bulk"
        print(url)
        r=requests.post(url,headers=headers, data=jsonList)
        return (json.loads(r.text))
