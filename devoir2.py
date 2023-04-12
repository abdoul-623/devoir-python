salaire = 5000000
prenom = "Abdoul kader"
nom = " Camara"
a = salaire * 2
b = salaire ** 2
c = salaire / 2
d = salaire % 3
print("_____________________LE RESULTAT_____________________")
print('le double du salaire est :', a)
print('le carré du salaire est :', b)
print('la moitié du salaire est :', c)
print("le reste du salaire après l'avoir divisé par trois est :", d)
if salaire > 5000000:
    print('Excellent travailleur')
elif salaire > 2000000:
    print('Bon travailleur')
elif salaire > 1000000:
    print('Travailleur Moyen')
elif salaire >= 1000 and salaire <= 1000000:
    print('Contractuel')
else:
    print('Ce salaire ne répond à aucun des critères mentionnés')
print('Prénom et Nom :', prenom + nom)
print("J'ai traité cet exercice avec succès")
