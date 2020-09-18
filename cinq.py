from time import sleep

import serial.tools.list_ports
from serial import Serial

from construction_gcode import Build_Gcode
from construction_parametre import Build_conf


def find_anet():
    print("serchaing for Anet V8 on serial ports...")
    ports = list(serial.tools.list_ports.comports())

    if len(ports) == 0:
        print("no Anet found!")
        raise IOError
    elif len(ports) == 1:
        print("One Anet found")
        our_anet = 0
    else:
        print("multiple device found")
        i = 0
        for p in ports:
            print("	[", i, "] ", p, sep='')
            i += 1
        while True:
            try:
                our_anet = int(input(">>> "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                if (our_anet < 0) or (len(ports) <= our_anet):
                    print("Sorry, that device does not exist")
                    continue
                break
    return ports[our_anet][0]


def send_1Gcode(path, devices):
    to_anet_file = open(path, 'r')
    lignes = to_anet_file.readlines()
    i = 0
    for ligne in lignes:
        i += 1
        ligne = ligne.replace('\n', '')
        print(ligne)
        # sleep(2)
        ligne = ligne.encode()
        ligne += b'\r'
        # sleep(1)
        devices.write(ligne)
    to_anet_file.close()
    j = 0
    while i != j:
        raw_line = ""
        while raw_line != b'ok\n':
            raw_line = devices.readline()
            print(raw_line)
            sleep(0.5)
        j += 1


if __name__ == "__main__":
    port_anet = find_anet()
    print(port_anet)
    path = '/home/pi/Juke_box/Gcode/'
    device = Serial(port=port_anet, baudrate=115200)

    while True:
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

        # while devices.readline()!='ok\n' :
        #	sleep(1)
