# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from flask import Flask, render_template, request
from client_id import client_id
import logging
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='templates')


@app.route('/')
def init():
    return render_template('tata.html')

@app.route('/click_me')
def click_me():
    remote_ip = request.remote_addr
    import  pdb; pdb.set_trace()
    return 'Bye ZeOmega'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)
