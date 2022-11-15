from controller.metric import request_service as rs

class host_service():
    rs = None
    def __init__(self):
        self.rs = rs.req_service('host_req_body.yaml')

    def get_cpu_load_15min(self, auth_token):
        return self.rs.request_post('hardware.cpu.load.15min', auth_token)

    def get_cpu_load_1min(self, auth_token):
        return self.rs.request_post('hardware.cpu.load.1min', auth_token)  

    def get_cpu_load_5min(self, auth_token):
        return self.rs.request_post('hardware.cpu.load.5min', auth_token)  

    def get_cpu_util(self, auth_token):
        return self.rs.request_post('hardware.cpu.util', auth_token)  

    def get_cpu_idle(self, auth_token):
        return self.rs.request_post('hardware.system_stats.cpu.idle', auth_token)  

    def get_mem_buffer(self, auth_token):
        return self.rs.request_post('hardware.memory.buffer', auth_token) 

    def get_mem_cached(self, auth_token):
        return self.rs.request_post('hardware.memory.cached', auth_token) 

    def get_mem_swap_avail(self, auth_token):
        return self.rs.request_post('hardware.memory.swap.avail', auth_token) 

    def get_mem_swap_total(self, auth_token):
        return self.rs.request_post('hardware.memory.swap.total', auth_token) 

    def get_mem_total(self, auth_token):
        return self.rs.request_post('hardware.memory.total', auth_token)  

    def get_mem_used(self, auth_token):
        return self.rs.request_post('hardware.memory.used', auth_token)  

    def get_net_in_bytes(self, auth_token):
        return self.rs.request_post('hardware.network.incoming.bytes', auth_token)  

    def get_net_out_bytes(self, auth_token):
        return self.rs.request_post('hardware.network.outgoing.bytes', auth_token)  

    def get_net_out_errors(self, auth_token):
        return self.rs.request_post('hardware.network.outgoing.errors', auth_token)  

    def get_disk_size_total(self, auth_token):
        return self.rs.request_post('hardware.disk.size.total', auth_token)  

    def get_disk_size_used(self, auth_token):
        return self.rs.request_post('hardware.disk.size.used', auth_token)                                                               