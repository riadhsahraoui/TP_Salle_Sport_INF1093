class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.duree = duree
        self.prix = prix
        self.actif = actif

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def succursale(self):
        return self.__succursale

    @succursale.setter
    def succursale(self, value):
        self.__succursale = value

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, value):
        if value > 0:
            self.__duree = value
        else:
            print("Durée invalide.")

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, value):
        if value > 0:
            self.__prix = value
        else:
            print("Prix invalide.")

    @property
    def actif(self):
        return self.__actif

    @actif.setter
    def actif(self, value):
        if str(value).lower() in ["oui", "non"]:
            if str(value).lower() == "oui":
                self.__actif = "Oui"
            else:
                self.__actif = "Non"
        else:
            print("Actif doit être Oui ou Non.")

    def afficher(self):
        print(self.numero, self.nom, self.succursale,
              str(self.duree) + " mois",
              str(self.prix) + "$/mois",
              "Actif:", self.actif)
class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier

    def afficher(self):
        super().afficher()
        print("Casier:", self.casier)
        print("----------------------------------------")


class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach

    def afficher(self):
        super().afficher()
        print("Coach personnel:", self.coach)
        print("----------------------------------------")


m1 = MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "Oui")
m2 = MembreStandard(2, "Marc Bouchard", "Est", 6, 40, "Non", "Non")
m3 = MembrePremium(3, "Sophie Nguyen", "Centre-ville", 12, 80, "Oui", "Oui")
m4 = MembrePremium(4, "Karim Haddad", "Ouest", 24, 75, "Oui", "Non")

membres = [m1, m2, m3, m4]


def sauvegarder_membres(membres):
    f = open("membres.txt", "w", encoding="utf-8")
    for m in membres:
        if isinstance(m, MembreStandard):
            type_m = "STANDARD"
            extra = m.casier
        else:
            type_m = "PREMIUM"
            extra = m.coach

        ligne = type_m + ";" + str(m.numero) + ";" + m.nom + ";" + m.succursale + ";" \
                + str(m.duree) + ";" + str(m.prix) + ";" + m.actif + ";" + extra + "\n"
        f.write(ligne)
    f.close()


def charger_membres():
    membres = []
    try:
        f = open("membres.txt", "r", encoding="utf-8")
        for ligne in f:
            t = ligne.strip().split(";")
            type_m = t[0]
            num = int(t[1])
            nom = t[2]
            suc = t[3]
            duree = int(t[4])
            prix = float(t[5])
            actif = t[6]
            extra = t[7]

            if type_m == "STANDARD":
                membres.append(MembreStandard(num, nom, suc, duree, prix, actif, extra))
            else:
                membres.append(MembrePremium(num, nom, suc, duree, prix, actif, extra))
        f.close()
    except:
        print("Fichier introuvable.")
    return membres


def afficher_membres_actifs(membres):
    for m in membres:
        if m.actif == "Oui":
            m.afficher()


def afficher_membres_premium(membres):
    for m in membres:
        if isinstance(m, MembrePremium):
            m.afficher()


def construire_index(membres):
    d = {}
    for m in membres:
        d[m.numero] = m
    return d


def rechercher_par_numero(index_membres, numero):
    if numero in index_membres:
        index_membres[numero].afficher()
    else:
        print("Numéro inexistant.")


def menu():
    membres = []
    index = {}

  


