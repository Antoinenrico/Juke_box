#! venv/bin/python
from time import sleep
from flask import (Flask, make_response, render_template, request)
from serial import Serial

from cinq import find_anet, send_1Gcode
from construction_gcode import Build_Gcode
from construction_parametre import Build_conf

# initialize Flask
app = Flask(__name__)


@app.route('/')
def index():  # 0.0.0.0:5000
    return render_template('index.html')


@app.route('/parametres')
def serve_parametres():
    return render_template('parametres.html')


@app.route('/api', methods=['POST'])
def serve_api():
    if request.form["sens"] == "init":
        try:
            port_anet = find_anet()
        except IOError:
            return make_response("Jukebox non trouvé!", 500) # erreur 500 = erreur interne du serveur
        print(port_anet)
        path = '/home/pi/Juke_box/Gcode/'
        device = Serial(port=port_anet, baudrate=115200)
        j = 0
        while device.inWaiting:
            raw_line = device.readline()
            print(raw_line)
            # Faire interruption sur 'message arrive'
            # ici on attend juste les 32 trames init, dirtysanchez
            j += 1
            # print(j)
            if j >= 31:
                break
        sleep(0.5)
        go = path + 'GcodeY.txt'
        path = '/home/pi/Juke_box/Gcode/Gcode'
        pathconf = '/home/pi/Juke_box/Gcode/conf.txt'
        Build_Gcode(pathconf, path, 1)
        Build_conf(pathconf, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        send_1Gcode(go, device)
        return make_response("Hello there", 200)

    if request.form["sens"] in ["gauche", "droite", "bas", "haut"]:
        print(request.form["sens"])
        return make_response(request.form["sens"], 501) # Erreur 501 = non implémenté



if __name__ == '__main__':
    app.run()
