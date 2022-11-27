import yaml
import pprint
import json
from concurrent.futures import ThreadPoolExecutor
import requests
from common import request_api as ra

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
        clsPath = 'aggregates?granularity={}&groupby=cluster_id'
        clsPath = clsPath.format(granularity)
        resultJson = self.rapi.post_with_x_auth(clsPath, auth_token, jsonBody)
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
        base_path = self.reqPath.format(granularity)
        print(base_path)
        resultJson = self.rapi.post_with_x_auth(base_path, auth_token, jsonBody)
        return resultJson

    def request_post_host(self,key, auth_token):
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
        base_path = 'aggregates?granularity={}&groupby=id'
        base_path = base_path.format(granularity)
        print(base_path)
        resultJson = self.rapi.post_with_x_auth(base_path, auth_token, jsonBody)
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
        base_path = reqPath = 'aggregates?granularity={}&groupby=id'
        base_path = base_path.format(granularity) + '&start='
        print(self.reqPath)
        base_path += start_time
        print(self.reqPath)
        resultJson = self.rapi.post_with_x_auth(base_path, auth_token, jsonBody)
        
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
        base_path = ''
        list_of_requests = []
        for ob in key_list:
            item = self.host[ob]
            jsonBody = item['body']
            granularity = item['granularity']

            if start_time is None:
                base_path = self.reqPath.format(granularity)
            else:
                base_path = self.reqPath.format(granularity) + '&start=' + start_time
                
            list_of_requests.append((base_path, auth_token,jsonBody, ob))

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
        base_path = ''
        list_of_requests = []
        for ob in key_list:
            item = self.host[ob]
            jsonBody = item['body']
            granularity = item['granularity']

            if start_time is None:
                base_path = self.reqPath.format(granularity) + '&groupby=project_id'
            else:
                base_path = self.reqPath.format(granularity) + '&groupby=project_id' + '&start=' + start_time
                
            list_of_requests.append((base_path, auth_token,jsonBody, ob))

        with ThreadPoolExecutor(max_workers=10) as pool:
            response_list = list(pool.map(self.get_url,list_of_requests))
 
        return response_list


    def get_cluster_url(self, args):
        url = args[0]
        result = requests.get(url)
        return (result.json(), args[1])

    def req_cluster_multi(self, urllist):
        with ThreadPoolExecutor(max_workers=10) as pool:
            response_list = list(pool.map(self.get_cluster_url, urllist))
        
        return response_list