import copy

liste_etuidant = ["Abdoul", "Kader", "Camara", "Mariama", "Mabinty", "Mamata", "M'mah", "Maciré"]
print("le premier élément de cette liste est :", liste_etuidant[0])
print("le dernier élément de cette liste est :", liste_etuidant[-1])
print("le quatrième élément de cette liste est :", liste_etuidant[3])
liste_etuidant.sort()
print("liste triée :", liste_etuidant)
del liste_etuidant[3]
print("suppression du 4e élément", liste_etuidant)
liste_vide = copy.deepcopy(liste_etuidant)
print("copie effectuée dans la listee vide", liste_vide)
liste_etuidant.clear()
liste_vide.clear()
print("après nettoyage on obtient:", "liste_vide -->", liste_vide, "||", "liste_étudiants -->", liste_etuidant)
