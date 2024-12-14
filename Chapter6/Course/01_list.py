leisure = ['swim', 'dance', 'sing']  # Création d'une liste
print(leisure)
# Longueur d'une liste
print(len(leisure))  # 3
# Test de présence d'un élément
print('basketball' in leisure)  # False
print('dance' in leisure)   # True
print('DANCE' in leisure)   # False
# Index d'un élément
print(leisure.index('swim'))    # 0
# Accéder aux éléments d'une liste
print(leisure[1])   # dance
# Modifier la valeur d'un élément de liste
leisure[0] = 'ski'
print(leisure)  # ['ski', 'dance', 'sing']
# Ajouter un élément à une liste
leisure.append('game')
print(leisure)  # ['ski', 'dance', 'sing', 'game']
# Insérer un élément ailleurs qu'à la fin
leisure.insert(3, 'climb')
print(leisure)
# Enlever un élément de liste
leisure.remove('climb')
print(leisure)
# Enlever un élément ailleurs avec son index
leisure.pop(1)
print(leisure)
# Vider une liste
leisure.clear()
print(leisure)
# Concaténer deux listes
month = ['Janvier', 'Février', 'Mars']
season = ['Automne', 'Hiver', 'Printemps', 'Eté']
various_times = month + season
print(various_times)
# Étendre une liste
month.extend(season)
print(month)
print('--------------------')
# Créer une tranche de liste
rainbow = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
print(len(rainbow))
print(rainbow[1:4])
print(rainbow[3:])
print(rainbow[:5])
print(rainbow[-5:-2])