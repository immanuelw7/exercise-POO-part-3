#Enoch Immanuel Wang - 401
#Fait le 30 javier 2022
#importer les modules
import random
#on créée une fonction pour faire rouler dés
def des():
    roulade_des = [random.randint(1, 6) for i in range(4)]
    roulade_des.sort(reverse=True)
    return sum(roulade_des[:3])


#on créée la classe de NPC
class NPC:
    #initialisation
    def __init__(self):
        self.force = des()
        self.agilité = des()
        self.constitution = des()
        self.intelligence = des()
        self.sagesse = des()
        self.charisme = des()
        self.classe_darmure = random.randint(1, 12)
        self.nom = str
        self.race = str
        self.espece = str
        self.vie = random.randint(1,20)
        self.profession = str
#créé une fonction pour les caractéristiques et les affichers
    def affichagedecaractéristique(self):
        print('nom:',self.nom)
        print('race:',self.race)
        print('espece:',self.espece)
        print('vie:',self.vie)
        print('profession:',self.profession)
        print('force',self.force)
        print('agilité:',self.agilité)
        print('consititution:',self.constitution)
        print('intelligence:',self.intelligence)
        print('sagesse:',self.sagesse)
        print('charisme:',self.charisme)
        print('classe darmure:',self.classe_darmure)

#crééer une classe pour le Kobold qui est un NPC
class kobold(NPC):
    #initialisation
    def __init__(self):
        super().__init__()
    #créer une fonction pour attaquer
    def attack(self, cible):
        return
    #crééer une fonction pour recevoir les dommages
    def subir_des_dommages(self,ouf_dommage):
        self.vie -= ouf_dommage

#créer une classe pour un Héro qui est un NPC
class Heros(NPC):
    #initialisation
    def __init__(self):
        super().__init__()
    #une fonction pour attaquer
    def attack(self, cible):
        #rouler un dé de 20 faces
        attackde = random.randint(1,20)
        #condition, si le dé est égale à 20
        if attackde == 20:
            #on va lui faire des dégats d'un autre dée rouler de 1 à 8
            cible.subir_des_dommages(random.randint(1, 8))
        #si le dé rouler est plus grand que 2 et plus petit que 9, et plus grand que son armure,
        elif 19>=attackde>=2 and cible.classe_darmure < attackde:
            #on va lui faire des dégats d'un autre dée rouler de 1 à 8
            cible.subir_des_dommages(random.randint(1, 6))
    #créer une fonction pour recevoir les dommages
    def subir_des_dommages(self, ouf_dommage):
        #return rien
        return
