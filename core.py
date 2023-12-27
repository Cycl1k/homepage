from flask import render_template, Flask
from proxmox import *
from link import links
from components import *


app = Flask(__name__)

@app.route("/")
def index():
    node = proxmox_node_names()
    vm = proxmox_vm_names()
    lxc = proxmox_lxc_names()
    link = links('link/link.json')
    return render_template("base.html", node=node, vm=vm, lxc=lxc, link=link)


@app.route('/update_node', methods=['POST'])
def update_node():
    f = proxmox_nodes()
    return f

@app.route('/update_vm', methods=['POST'])
def update_vm():
    f = proxmox_vm()
    return f

@app.route('/update_lxc', methods=['POST'])
def update_lxc():
    f = proxmox_lxc()
    print(f)
    return f