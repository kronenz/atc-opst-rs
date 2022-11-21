import json
import yaml

from controller.metric import request_service as req

class cluster_service():
    cluster = None
    rs = req.req_service()
    def __init__(self):
         with open('cluster.yaml') as f:
            self.cluster = yaml.load(f, Loader=yaml.FullLoader)

    def get_cluster_list(self, auth_token):
        result_data = self.rs.request_post_cluster_id('vm_cpu', auth_token)  
        
        base_list = []

        for key_item in result_data: #키별 반복
            cluster_id = key_item['group']['cluster_id']
            if cluster_id == None:
                pass
            else:    
                base_list.append(cluster_id)

        return base_list

    def get_cluster_all(self, list, auth_token):
        """vm클러스터 id 목록 과 하위 데이터를 모두 반환해주는 함수

        Args:
            list (strubg): cluster_id ex):

        Returns:
            dict: 'cluster_id' : {data} 구조
        """
        cluster_list = self.get_cluster_list(auth_token)

        ##request cluster data

        result_data = {}
        for item in list:
            print('')

        return result_data