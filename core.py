from flask import render_template, Flask, jsonify
from scr.proxmox_node import *

app = Flask(__name__)

@app.route("/")
def index():
    node = proxmox_names()
    return render_template("proxmox.html", node=node)


@app.route('/update', methods=['POST'])
def update():
    f = proxmox_nodes()
    print(f)
    return f