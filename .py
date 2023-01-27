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
    def subir_des_dommages(self,ouf_dommage):
        self.vie -= ouf_dommage


class Héros(NPC):
    def __init__(self):
        super().__init__()
    def attack(self, cible):
        attackdé = random.randint(1,20)
        if attackdé == 20:
            cible.subir_des_dommages = random.randint(1, 8)
            cible.subir_des_dommages(dégat_dommage)
        elif attackdé == 1:
            dégat_dommage = 0
        elif 19> attackdé <2 and cible.classe_darmure < attackdé:
            dégat_dommage = random.randint(1, 6)
            cible.subir_des_dommages(random.randint(1, 6))
        else:
            print('tu as foiré ton attaque')

    def subr_des_dommages(self, ouf_dommage):
        return



