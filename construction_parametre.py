# construction conf Gcode vinyl 
#K = 10# coefficient de coordonnée par numero de vinyles
#J = 10# coordonnée de decallage pour attraper vinyles
#L = 10# coordonnée de levage
#M = 10# coordonnée au dessus platine
#P = 10# coordonnée decalage un fois vinyles sur plat
#PlatX = 10#
#PlatY = 10#
#TankX = 10#
#TankY = 10#



def Build_conf(pathconf,K,J,L,M,P,PlatX,PlatY,TankX,TankY):
		fichier_conf = open(pathconf,'w')
		END= '\n'
		START=str(K)
		MID='#K = coefficient de coordonnée par numero de vinyles'
		fichier_conf.write(START+MID+END)
		START=str(J)
		MID="#J =  coordonnée de decallage pour attraper vinyles"
		fichier_conf.write(START+MID+END)
		fichier_conf.write(str(L)+'#L =  coordonnée de levage'+END)
		fichier_conf.write(str(M)+'#M =  coordonnée au dessus platine'+END)
		fichier_conf.write(str(P)+'#P = coordonnée decalage un fois vinyles sur plat'+END)
		fichier_conf.write(str(PlatX)+'#PlatX ='+END)
		fichier_conf.write(str(PlatY)+'#PlatY ='+END)
		fichier_conf.write(str(TankX)+'#TankX ='+END)
		fichier_conf.write(str(TankY)+'#TankY ='+END)
		print("OK FIN CONSTRUCTION conf ")

		fichier_conf.close()
		
if __name__ == "__main__" :
	pathconf='/home/pi/Gcode/conf.txt'
	Build_conf(pathconf,0,0,0,0,0,0,0,0,0) 

