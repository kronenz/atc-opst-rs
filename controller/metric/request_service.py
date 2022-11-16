import yaml
import pprint
import json

from controller.metric import request_api as ra

class req_service():
    rapi = ra.request_api()
    reqPath = 'aggregates?granularity={}&groupby=id&groupby=original_resource_id'
    host = None
    pp = None
    def __init__(self, yamlfile):
        """클래스 초기화시 처리명세가 담긴 yamlfile명을 입력하면
            해당 내용에 맞게 처리함 
        Args:
            yamlfile (_type_): jsonBody명세가 담긴 파일명
        """
        with open(yamlfile) as f:
            self.host = yaml.load(f, Loader=yaml.FullLoader)

    def request_post(self,key, auth_token):
        """request_name과 인증토큰을 입력하면 해당 요청에 필요한 jsonBody를 불러와 post요청후
            REST API 요청후 JsonResponse값 반환

        Args:
            key (string)): Ex) Host_hardware.cpu.load.15min
            auth_token (string): 오픈스택 admin 인증토큰값 

        Returns:
            json: JsonResponse 값
        """
        item = self.host[key]
        jsonBody = item['body']
        granularity = item['granularity']
        self.reqPath = self.reqPath.format(granularity)
        resultJson = self.rapi.post_with_x_auth(self.reqPath, auth_token, jsonBody)
        return resultJson

    def request_post_st(self,key, auth_token, start_time):
        """_summary_ 수집시점과 함꼐 request_name과 인증토큰을 입력하면 해당 요청에 필요한 jsonBody를 불러와 post요청후
            REST API 요청후 JsonResponse값 반환

        Args:
            key (string):  Ex) Host_hardware.cpu.load.15min
            auth_token (string): 오픈스택 admin 인증토큰값
            start_time (time): ex) 2022-11-16T06:35:00

        Returns:
            _type_: _description_
        """
        item = self.host[key]
        jsonBody = item['body']
        granularity = item['granularity']
        self.reqPath = self.reqPath.format(granularity) + '&start=' + start_time
        print(jsonBody)
        print(self.reqPath + "|| " + auth_token + "||")
        resultJson = self.rapi.post_with_x_auth(self.reqPath, auth_token, jsonBody)
        print(resultJson)
        return resultJson