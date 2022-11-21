import yaml
import pprint
import json
from concurrent.futures import ThreadPoolExecutor

from controller.metric import request_api as ra

form_data = {

}


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


    def request_post_cluster_id(self,key, auth_token):
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
        self.reqPath = 'aggregates?granularity={}&groupby=cluster_id'
        self.reqPath = self.reqPath.format(granularity)
        resultJson = self.rapi.post_with_x_auth(self.reqPath, auth_token, jsonBody)
        return resultJson

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
            json:  JsonResponse 값
        """
        item = self.host[key]
        jsonBody = item['body']
        granularity = item['granularity']
        self.reqPath = self.reqPath.format(granularity) + '&start=' + start_time
      
        resultJson = self.rapi.post_with_x_auth(self.reqPath, auth_token, jsonBody)

        return resultJson

    def get_url(self, args):
        resultJson = self.rapi.post_with_x_auth(args[0], args[1], args[2])
        for item in resultJson:
            item['name'] = args[3]

        return resultJson

    def request_post_multi(self,key_list, auth_token, start_time):
        """수집시점과 함꼐 request_name 목록과 인증토큰을 입력하면 해당 요청에 필요한 jsonBody를 불러와 post요청후
            ThreadPoolExecutor로 REST API 요청후 JsonResponse값 List

        Args:
            key_list (list): 동시 요청하고 싶은 요청명 목록
            auth_token (string): 오픈스택 admin 인증토큰값
            start_time (time): ex ) 2022-11-16T06:35:00 None을 입력하면 처리하지 않는다.

        Returns:
            json:  JsonResponse 값
        """
        list_of_requests = []
        for ob in key_list:
            item = self.host[ob]
            jsonBody = item['body']
            granularity = item['granularity']

            if start_time is None:
                self.reqPath = self.reqPath.format(granularity)
            else:
                self.reqPath = self.reqPath.format(granularity) + '&start=' + start_time
                
            list_of_requests.append((self.reqPath, auth_token,jsonBody, ob))

        with ThreadPoolExecutor(max_workers=10) as pool:
            response_list = list(pool.map(self.get_url,list_of_requests))
 
        return response_list

        
    def request_post_multi_proejct_all(self,key_list, auth_token, start_time):
        """수집시점과 함꼐 request_name 목록과 인증토큰을 입력하면 해당 요청에 필요한 jsonBody를 불러와 post요청후
            ThreadPoolExecutor로 REST API 요청후 JsonResponse값 List

        Args:
            key_list (list): 동시 요청하고 싶은 요청명 목록
            auth_token (string): 오픈스택 admin 인증토큰값
            start_time (time): ex ) 2022-11-16T06:35:00 None을 입력하면 처리하지 않는다.

        Returns:
            json:  JsonResponse 값
        """
        list_of_requests = []
        for ob in key_list:
            item = self.host[ob]
            jsonBody = item['body']
            granularity = item['granularity']

            if start_time is None:
                self.reqPath = self.reqPath.format(granularity) + '&groupby=project_id'
            else:
                self.reqPath = self.reqPath.format(granularity) + '&groupby=project_id' + '&start=' + start_time
                
            list_of_requests.append((self.reqPath, auth_token,jsonBody, ob))

        with ThreadPoolExecutor(max_workers=10) as pool:
            response_list = list(pool.map(self.get_url,list_of_requests))
 
        return response_list
