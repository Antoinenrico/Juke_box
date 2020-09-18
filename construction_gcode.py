# construction Gcode vinyl


# def Build_Gcode(PlatX, PlatY, TankX, TankY, number_V, path):
def Build_Gcode(pathconf, path, number_V):

    liste = []
    fichier_conf = open(pathconf, 'r')
    lignes = fichier_conf.readlines()
    # print(lignes)
    # print('\n')
    for ligne in lignes:
        # print(ligne)
        # ligne = ligne.split('#')
        ligne = ligne[0:ligne.find('#')]
        liste.append(ligne)
        # print(ligne)
    # print(lignes)
    fichier_conf.close()
    # print(liste)
    K = int(liste[0])  # coefficient de coordonnée par numero de vinyles
    J = int(liste[1])  # coordonnée de decallage pour attraper vinyles
    L = int(liste[2])  # coordonnée de levage
    M = int(liste[3])  # coordonnée au dessus platine
    P = int(liste[4])  # coordonnée decalage un fois vinyles sur plat
    PlatX = int(liste[5])
    PlatY = int(liste[6])
    TankX = int(liste[7])
    TankY = int(liste[8])

    path += str(number_V) + '.txt'
    print(path)
    to_anet_file = open(path, 'w')
    chaineG = 'G0'
    chaineY = 'Y00'
    chaineX = 'X00'
    chaineF = '\n'
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # G0Y00X00

    chaineY = 'Y' + str(TankY+J)  # pour etre en face du rangement
    chaineX = 'X' + str(TankX+K*number_V)  # bonne hauteur
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # Go en face rangement

    chaineY = 'Y' + str(TankY)  # pour etre en face du vinymes
    chaineX = 'X' + str(TankX+K*number_V)  # On bouge pas
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # Go sous vinyles

    chaineY = 'Y' + str(TankY)  # On bouge pas
    chaineX = 'X' + str(TankX+K*number_V+L)  # on lève
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # Go lever

    chaineG = 'G0'
    chaineY = 'Y00'
    chaineX = 'X00'
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # G0Y00X00 init

    chaineY = 'Y' + str(PlatY)  # coordonnées lateral platine
    chaineX = 'X' + str(PlatX+M)  # coordonnées verticale platine +coeff
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # Go au dessus platine

    chaineY = 'Y' + str(PlatY)  # On bouge pas
    chaineX = 'X' + str(PlatX)  # on descend
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # Go poser vinyles

    chaineY = 'Y' + str(PlatY-P)  # On laisse le vinyle en place
    chaineX = 'X' + str(PlatX)  # on bouge pas
    # Go laisser vinyle en place
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)

    chaineG = 'G0'
    chaineY = 'Y00'
    chaineX = 'X00'
    to_anet_file.write(chaineG+chaineY+chaineX+chaineF)  # G0Y00X00 init

    print("OK FIN CONSTRUCTION GCODE " + str(number_V))
    to_anet_file.close()


if __name__ == "__main__":
    path = '/home/pi/Gcode/Gcode'
    pathconf = '/home/pi/Gcode/conf.txt'
    Build_Gcode(pathconf, path, 1)
