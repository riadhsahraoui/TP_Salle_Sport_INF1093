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


