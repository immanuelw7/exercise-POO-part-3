import random

def dés():
    roulade_dés = [random.randint(1, 6) for i in range(4)]
    roulade_dés.sort(reverse=True)
    return sum(roulade_dés[:3])



class NPC:
    def __init__(self):
        self.force = dés()
        self.agilité = dés()
        self.constitution = dés()
        self.intelligence = dés()
        self.sagesse = dés()
        self.charisme = dés()
        self.classe_darmure = random.randint(1, 12)
        self.nom = str
        self.race = str
        self.espece = str
        self.vie = random.randint(1,20)
        self.profession = str

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


class kobold(NPC):
    def __init__(self):
        super().__init__()
    def attack(self, cible):
        return
    def subir_des_dommages(self,dégat_dommage):
        return


class Héros(NPC):
    def __init__(self):
        super().__init__()
    def attack(self, cible):
        return
    def subir_des_dommages(self, dégat_dommage):
        return


