from proxmoxer import ProxmoxAPI
from components import *

#Удаление ебучих уведомлений в консоли
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxmox = ProxmoxAPI ('IP address', user = 'root@pam', password = 'password', verify_ssl = False, service='PVE')

def proxmox_cluster():
    print(proxmox.cluster.status.get())

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

def proxmox_vm():
    proxDict = {}
    counetr = 0
    for node in proxmox.nodes.get():
        for vm in proxmox.nodes(node['node']).qemu.get():                
            
            proxDict.update({counetr :{
                'vm_id': vm['vmid'],
                'vm_name': vm['name'],
                'vm_status': vm['status'],
                'vm_uptime': vm['uptime'],        
                'vm_vcpu': vm['cpus'],
                'vm_cpu_load': percentConvert(vm['cpu']),
                'vm_ram_total': bInGbConvert(vm['maxmem']),
                'vm_ram_moment': bInGbConvert(vm['mem']),
                'vm_disk_total': bInGbConvert(vm['maxdisk']),
                'vm_disk_moment': bInGbConvert(vm['disk']),
                'vm_net_in': vm['netin'],
                'vm_net_out': vm['netout']
            }})
            counetr +=1
          
    sorted_dict = dict(sorted(proxDict.items()))
    sorted_dict[-1] = counetr - 1  
    return sorted_dict

def proxmox_lxc():

    proxDict = {}
    counetr = 0

    for node in proxmox.nodes.get():
        for lxc in proxmox.nodes(node['node']).lxc.get():
            proxDict.update({counetr :{
                'lxc_id': lxc['vmid'],
                'lxc_name': lxc['name'],
                'lxc_status': lxc['status'],
                'lxc_uptime': lxc['uptime'],        
                'lxc_vcpu': lxc['cpus'],
                'lxc_cpu_load': percentConvert(lxc['cpu']),
                'lxc_ram_total': bInGbConvert(lxc['maxmem']),
                'lxc_ram_moment': bInGbConvert(lxc['mem']),
                'lxc_swap_total':  bInMbConvert(lxc['maxswap']),
                'lxc_swap_moment': bInMbConvert(lxc['swap']),
                'lxc_disk_total': bInGbConvert(lxc['maxdisk']),
                'lxc_disk_moment': bInGbConvert(lxc['disk']),
                'lxc_net_in': lxc['netin'],
                'lxc_net_out': lxc['netout']
            }})
            counetr +=1
    
    sorted_dict = dict(sorted(proxDict.items()))
    sorted_dict[-1] = counetr - 1
    return sorted_dict

def proxmox_node_names():
    proxDict = {}
    counetr = 0
    for node in proxmox.nodes.get():
        
        proxDict.update({ counetr : {
            'node_id': node['node'],
            'node_status': node['status']
        }})
        counetr +=1
    return proxDict

def proxmox_vm_names():
    proxDict = {}
    counetr = 0
    for node in proxmox.nodes.get():
        for vm in proxmox.nodes(node['node']).qemu.get():
        
            proxDict.update({ counetr : {
                'vm_id': vm['vmid'],
                'vm_name': vm['name']
            }})
            counetr +=1
    return proxDict

def proxmox_lxc_names():
    proxDict = {}
    counetr = 0
    for node in proxmox.nodes.get():
        for lxc in proxmox.nodes(node['node']).lxc.get():
        
            proxDict.update({ counetr : {
                'lxc_id': lxc['vmid'],
                'lxc_name': lxc['name']
            }})
            counetr +=1
    return proxDict

print(proxmox_lxc())
