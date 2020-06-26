#def des imports
import random

# def des fonctions 



# def de variable 
Energy = int(input("De combien d'énergie dispose le train ? :  "))
trainDepart = 0
Container = []
trainway = []
serviceStation = []
pikUp = True
longWay = int(input("longueur de la voie"))
maxEnergy = int(input("Energie max"))
maxCharge = int(input("charge max"))
statutParty = "ok"
map = ["-"] * longWay
consumption = 1
blocEnergy = int(input("Combien de bloc d'énergie seront disposés ? : "))
blocEnergyMax = int(input("Combien d'énergie il y a au max ? : "))


for i in range(len(blocEnergy)) :
    serviceStation.append(random.randint(1,10))

# def du main 

# condition de fin de jeu

while Energy > 0 :
    continue
    if maxEnergy = 0 :
    print("C'est perdu le train est en panne")
    break 
print