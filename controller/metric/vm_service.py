from controller.metric import request_service as rs
from concurrent.futures import ThreadPoolExecutor
from itertools import groupby

class vm_service():
    rs = None
    def __init__(self):
        self.rs = rs.req_service('vm_req_body.yaml')

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

    def post_url(args):
        return req

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




