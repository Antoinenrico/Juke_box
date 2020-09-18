#!venv/bin/python
from flask import Flask, render_template, url_for, copy_current_request_context, Response, request, jsonify, abort, stream_with_context,make_response
from time import time, sleep
import json

import serial.tools.list_ports
import logging 
from sys import stderr
from serial import Serial

from construction_gcode import Build_Gcode
from construction_parametre import Build_conf
from cinq import find_anet,send_1Gcode

# initialize Flask
app = Flask(__name__)


@app.route('/')
def index(): #0.0.0.0:5000
    return render_template('indexrico.html')

@app.route('/API',methods=['POST'])
def API(): #0.0.0.0:5000
    print("hello",request.form["sens"])
    if request.form["sens"] == "init" :
        port_anet = find_anet()
        print(port_anet)
        path='/home/pi/Juke_box/Gcode/'
        device = Serial(port=port_anet,baudrate=115200)
        j=0
        while device.inWaiting:
            raw_line= device.readline()
            print(raw_line)
			# Faire interruption sur 'message arrive'
			# ici on attend juste les 32 trames init, dirtysanchez
            j+=1
			#print(j)
            if j>=31:
                break
        sleep(0.5)
        go = path + 'GcodeY.txt'
        path='/home/pi/Juke_box/Gcode/Gcode'
        pathconf='/home/pi/Juke_box/Gcode/conf.txt'
        Build_Gcode(pathconf,path,1) 
        Build_conf(pathconf,0,0,0,0,0,0,0,0,0) 
        send_1Gcode(go,device)
        return make_response("Hello there",200)

    if request.form["sens"] == "gauche" or request.form["sens"] == "droite" or request.form["sens"] == "bas" or request.form["sens"] == "haut":
        print(request.form["sens"]) 
    
@app.route('/MENU',methods=['POST'])
def MENU(): #0.0.0.0:5000
    print("menu :")
    print(request.form["page"])
    if request.form["page"] == "start" :
        print('start')
        return render_template('indexrico.html')
    if request.form["page"] == "parametres" :
        print('parametres')
        return render_template('indexparametres.html')    

if __name__ == '__main__':
    app.run()
