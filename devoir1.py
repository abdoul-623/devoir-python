age = 41
salaire = 2000000
marier = True
nb_enfant = 1
Plus2_enf = 0.05
Moins2_enf = 0.003
Moins40_ans = 0.001
Salaire_plus_de_40ans = []

if salaire > 10000:
    if salaire > 2000000 and age > 40:
        if marier == True:
            if nb_enfant > 2:
                salaire_net = (salaire * (1 + Plus2_enf))
                print("Selaire de cet employé est :", salaire_net)
            else:
                salaire_net = (salaire * (1 + Moins2_enf))
                print("Selaire de cet employé est :", salaire_net)
#ajout des salaires des employés ayant plus de 40ans dans la liste
        Salaire_plus_de_40ans.append(salaire_net)
    elif age < 40 and salaire > 2000000:
        salaire_net = (salaire * (1 + Moins40_ans))
        print("Selaire de cet employé est :", salaire_net)
    else:
        salaire_net = salaire
        print(salaire)
#dictionnaire contennant mes informations
mes_infos = {
                'nom' : 'Camara',
                'prenom' : 'Abdoul Kader',
                'age' : 21,
                'sexe' : 'Masculin',
            }
#informations suppémentaires dans le dictionnaire
mes_infos["niveau"] = "L2"
mes_infos["taille"] = 1.84
mes_infos["poids"] = "82Kg"
#suppression de mon nom dans le dictionnaire avant son affichage
mes_infos.pop("nom")
print('les infos me concernant :', mes_infos)
#nettoyage du dictionnaire
mes_infos.clear()
print("après nettoyage le dictionnaire se présente comme suit :", mes_infos)
#suppression du dictionnaire
del mes_infos
print("Salaire des employés ayant plus de 40ans :", Salaire_plus_de_40ans)
