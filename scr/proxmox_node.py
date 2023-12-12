from proxmoxer import ProxmoxAPI
from scr.components import *

#Удаление ебучих уведомлений в консоли
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxmox = ProxmoxAPI ('192.168.0.250', user = 'root@pam', password = 'print(Razer&ProxmoxX3)', verify_ssl = False, service='PVE')

def proxmox_nodes():
    proxDict = {}
    counetr = 0
    for node in proxmox.nodes.get():
        if(node['status']!='offline') :
            proxDict.update({ counetr : {
                'node_id': node['node'],
                'node_status': node['status'],
                'node_uptime': node['uptime'],
                'node_core_load': percentConvert(node['cpu']),
                'node_core': node['maxcpu'],
                'node_ram_moment': bInGbConvert(node['mem']),
                'node_ram_total': bInGbConvert(node['maxmem']),
                'node_os_disk_total': bInGbConvert(node['maxdisk']),
                'node_os_disk_moment': bInGbConvert(node['disk'])
            }})
        else:
            proxDict.update({ counetr : {
                'node_id': node['node'],
                'node_status': node['status'],
            }})
        counetr +=1
    proxDict[-1] = counetr - 1
    return proxDict

def proxmox_names():
    proxDict = {}
    counetr = 0
    for node in proxmox.nodes.get():
        
        proxDict.update({ counetr : {
            'node_id': node['node'],
            'node_status': node['status']
        }})
        counetr +=1
    return proxDict

f = proxmox_nodes()
print(f)