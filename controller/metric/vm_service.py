from controller.metric import request_service as rs
from concurrent.futures import ThreadPoolExecutor
from itertools import groupby
from controller.metric import post_elk as pe
import json
import yaml
import requests

class vm_service():
    rs = None
    poste = None
    cldata = None
    def __init__(self):
        self.rs = rs.req_service('vm_req_body.yaml')
        self.poste = pe.post_elk()
        with open('cluster.yaml') as f:
            self.cldata = yaml.load(f, Loader=yaml.FullLoader)

    def get_cpu(self, auth_token):
        return self.rs.request_post('vm_cpu', auth_token)

    def get_vcpus(self, auth_token):
        return self.rs.request_post('vm_vcpus', auth_token)

    def get_memory(self, auth_token):
        return self.rs.request_post('vm_memory', auth_token)

    def get_mem_usage(self, auth_token):
        return self.rs.request_post('vm_memory.usage', auth_token)

    def get_net_in_bytes(self, auth_token):
        return self.rs.request_post('vm_network.incoming.bytes', auth_token)

    def get_net_in_packets_error(self, auth_token):
        return self.rs.request_post('vm_network.incoming.packets.error', auth_token)

    def get_net_in_packets_drop(self, auth_token):
        return self.rs.request_post('vm_network.incoming.packets.drop', auth_token)

    def get_net_in_packets(self, auth_token):
        return self.rs.request_post('vm_network.incoming.packets', auth_token)

    def get_net_out_bytes(self, auth_token):
        return self.rs.request_post('vm_network.outgoing.bytes', auth_token)

    def get_net_out_packtes_drop(self, auth_token):
        return self.rs.request_post('vm_network.outgoing.packets.drop', auth_token)

    def get_net_out_packtes_error(self, auth_token):
        return self.rs.request_post('vm_network.outgoing.packets.error', auth_token)

    def get_net_out_packtes(self, auth_token):
        return self.rs.request_post('vm_network.outgoing.packets', auth_token)

    def get_disk_root_size(self, auth_token):
        return self.rs.request_post('vm_disk.root.size', auth_token)

    def get_disk_ephemeral_size(self, auth_token):
        return self.rs.request_post('vm_disk.ephemeral.size', auth_token)

    def get_disk_device_allocation(self, auth_token):
        return self.rs.request_post('vm_disk.device.allocation', auth_token)

    def get_disk_device_capacity(self, auth_token):
        return self.rs.request_post('vm_disk.device.capacity', auth_token)

    def get_disk_device_usage(self, auth_token):
        return self.rs.request_post('vm_disk.device.usage', auth_token)

    def get_disk_device_read_bytes(self, auth_token):
        return self.rs.request_post('vm_disk.device.read.bytes', auth_token)

    def get_disk_device_read_latency(self, auth_token):
        return self.rs.request_post('vm_disk.device.read.latency', auth_token)

    def get_disk_device_read_requests(self, auth_token):
        return self.rs.request_post('vm_disk.device.read.requests', auth_token)

    def get_disk_device_write_bytes(self, auth_token):
        return self.rs.request_post('vm_disk.device.write.bytes', auth_token)

    def get_disk_device_write_latency(self, auth_token):
        return self.rs.request_post('vm_disk.device.write.latency', auth_token)

    def get_disk_device_write_requests(self, auth_token):
        return self.rs.request_post('vm_disk.device.write.requests', auth_token)

    def get_network_all(self, auth_token):

        key_list = []
        key_list.append('vm_network.incoming.bytes')
        key_list.append('vm_network.incoming.packets')
        key_list.append('vm_network.incoming.packets.drop')
        key_list.append('vm_network.incoming.packets.error')
        key_list.append('vm_network.outgoing.bytes')
        key_list.append('vm_network.outgoing.packets')
        key_list.append('vm_network.outgoing.packets.drop')
        key_list.append('vm_network.outgoing.packets.error')

        result_list = self.rs.request_post_multi(key_list, auth_token, None)

        base_dict = {}

        for key_item in result_list: #키별 반복
            for item in key_item:
                measure_name = item['name']
                original_resource_id = item['group']['original_resource_id']
                measure_item = item['measures']

                if not original_resource_id in base_dict:
                    base_dict[original_resource_id]={}
                base_dict[original_resource_id][measure_name]=measure_item
                    

        return base_dict

    def get_network_all_proejct(self, auth_token):
        rsin = rs.req_service('vm_req_body_project_id.yaml')
        key_list = []
        key_list.append('vm_network.incoming.bytes')
        key_list.append('vm_network.incoming.packets')
        key_list.append('vm_network.incoming.packets.drop')
        key_list.append('vm_network.incoming.packets.error')
        key_list.append('vm_network.outgoing.bytes')
        key_list.append('vm_network.outgoing.packets')
        key_list.append('vm_network.outgoing.packets.drop')
        key_list.append('vm_network.outgoing.packets.error')

        result_list = rsin.request_post_multi_proejct_all(key_list, auth_token, None)

        base_dict = {}

        for key_item in result_list: #키별 반복
            for item in key_item:
                measure_name = item['name']
                project_id=item['group']['project_id']
                original_resource_id = item['group']['original_resource_id']
                measure_item = item['measures']

                if not project_id in base_dict:
                    base_dict[project_id]={}
                if not original_resource_id in base_dict[project_id]:
                    base_dict[project_id][original_resource_id]={}
                base_dict[project_id][original_resource_id][measure_name]=measure_item

        return base_dict


   
    def get_cluster_cpu(self, auth_token):
        result_data = self.rs.request_post_cluster_id('vm_cpu', auth_token)  
        
        base_dict = {}

        for key_item in result_data: #키별 반복
            cluster_id = key_item['group']['cluster_id']
            if cluster_id == None:
                pass
            else:    
                measure_item = key_item['measures']

                if not cluster_id in base_dict:
                    base_dict[cluster_id]={}

                base_dict[cluster_id]=measure_item

        return base_dict

    def cluster_cpu_data_elk_bulk(self, auth_token):
        """sample_doc={"cluster_id":6422c4f4-9246-4b8a-9ee6-70bfd9afa59c,
           "cpu_use":0.224999,
           "@timestamp":"2022-11-21T06:56:00+00:00"}
            샘플 데이터 구조
        Args:
            auth_token (string): 인증 토큰
        """
        result_data = self.get_cluster_cpu(auth_token)
        send_list = []

        for key in result_data.keys(): # project 반복 
        
            aggregated = result_data[key]['measures']['aggregated'][-3:]

            for index in range(len(aggregated)):
                _doc = {"@timestamp": aggregated[index][0],
                "cpu_use":aggregated[index][2],
                "cluster_id": key}
                send_list.append(_doc)

        send_str = ''
        meta_str = '{"index": {"_index": "vm_cluster_cpu_sample"}}'
        for item in send_list:
            if send_str == '':
                send_str = meta_str + '\n' + json.dumps(item) 
            else:
                send_str = send_str + '\n' + meta_str + '\n' + json.dumps(item) 

        send_str = send_str + '\n'
        print(send_str)
        print('post_bulk_vm_cluster_cpu_sample')
        return self.poste.post_bulk('vm_cluster_cpu_sample', auth_token, send_str)


    def net_data_elk_bulk(self, auth_token):
        """sample_doc={"tx_byte":234.123,
           "tx_packet":24623.2141,
           "tx_drop":1.0,
           "tx_error":1.0,
           "rx_byte":312.532,
           "rx_packet":123.4512,
           "rx_drop":0.0,
           "rx_error":0.0,
           "@timestamp":1668941442,
           "port_id":"a3777ca0-a3",
           "vm_id":"2f70f301-b039-42cc-b043-1ed47011e1a8"}

            샘플 데이터 구조
        Args:
            auth_token (_type_): _description_

        Returns:
            _type_: _description_
        """
        result_data = self.get_network_all_proejct(auth_token)
        send_list = []

        for key in result_data.keys(): # project 반복 
            for inkey in result_data[key].keys(): # vm 반복
                item = result_data[key][inkey]
                strlist = inkey.split('-')
                vm_id = strlist[2] + "-" + strlist[3] + "-" + strlist[4] + "-" + strlist[5] + "-" + strlist[6]
                port_id = strlist[7].replace('tap', '') + "-" + strlist[8]

                in_bytes = item['vm_network.incoming.bytes']['measures']['aggregated'][-3:]
                in_packets = item['vm_network.incoming.packets']['measures']['aggregated'][-3:]
                in_drop = item['vm_network.incoming.packets.drop']['measures']['aggregated'][-3:]
                in_error = item['vm_network.incoming.packets.error']['measures']['aggregated'][-3:]
                out_bytes = item['vm_network.outgoing.bytes']['measures']['aggregated'][-3:]
                out_packets = item['vm_network.outgoing.packets']['measures']['aggregated'][-3:]
                out_drop = item['vm_network.outgoing.packets.drop']['measures']['aggregated'][-3:]
                out_error = item['vm_network.outgoing.packets.error']['measures']['aggregated'][-3:]

                for index in range(len(in_bytes)):
                    _doc = {"tx_byte": in_bytes[index][2],
                    "tx_packet":in_packets[index][2],
                    "tx_drop":in_drop[index][2],
                    "tx_error":in_error[index][2],
                    "rx_byte": out_bytes[index][2],
                    "rx_packet":out_packets[index][2],
                    "rx_drop": out_drop[index][2],
                    "rx_error": out_error[index][2],
                    "@timestamp":in_bytes[index][0],
                    "port_id": port_id,
                    "vm_id": vm_id}
                    send_list.append(_doc)

        send_str = ''
        meta_str = '{"index": {"_index": "vm_resource_sample"}}'
        for item in send_list:
            if send_str == '':
                send_str = meta_str + '\n' + json.dumps(item) 
            else:
                send_str = send_str + '\n' + meta_str + '\n' + json.dumps(item) 

        send_str = send_str + '\n'
        print('post_bulk_vm_resource_sample')
        return self.poste.post_bulk('vm_resource_sample', auth_token, send_str)

    def get_cluster_list(self, auth_token):
        result_data = self.rs.request_post_cluster_id('vm_cpu', auth_token)  
        
        base_list = []

        for key_item in result_data: #키별 반복
            cluster_id = key_item['group']['cluster_id']
            if cluster_id == None or cluster_id == '6422c4f4-9246-4b8a-9ee6-70bfd9afa59c':
                pass
            else:    
                base_list.append(cluster_id)

        return base_list

    def get_cluster_all(self, auth_token):
        """vm클러스터 id 목록 과 하위 데이터를 모두 반환해주는 함수

        Args:
            list (strubg): cluster_id ex):

        Returns:
            dict: 'cluster_id' : {data} 구조
        """
        cluster_list = self.get_cluster_list(auth_token)
        
        cluster = self.cldata['cluster']
        api = cluster['api']
        ip = api['ip']
        port = str(api['port'])
        first_data = {}
        work_data = {}
        for clst in cluster_list:
            reqlist = []
            if clst == '6422c4f4-9246-4b8a-9ee6-70bfd9afa59c':
                pass
            else:                # 작업목록 생성
                clst_path = 'http://' + ip + ':' + port + '/smart-cluster/' + clst
                policy_path = 'http://' + ip + ':' + port + '/smart-cluster/' + clst + '/scaling-policy'
                nodes_path = 'http://' + ip + ':' + port + '/smart-cluster/' + clst + '/nodes'
                work_data[clst] = [clst_path, policy_path, nodes_path] #작업목록 추가

        for key in work_data.keys():
            url_list = work_data[key]
            for url in url_list:
                reqlist.append((url, key))
            
        result_list =  self.rs.req_cluster_multi(reqlist)

        key_cur = ''
        idxcnt = 0

        for item in result_list:
            cluster_id = item[1]
            in_item = item[0]
            if cluster_id != key_cur:
                key_cur = cluster_id
                first_data[cluster_id] = {}
                
            if idxcnt == 0:
                first_data[cluster_id]['main'] = in_item
            elif idxcnt == 1:
                first_data[cluster_id]['policy'] = in_item
            elif idxcnt == 2:
                first_data[cluster_id]['nodes'] = in_item
                idxcnt = 0

            idxcnt = idxcnt + 1
            
        return first_data