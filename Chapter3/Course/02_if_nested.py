score = int(input("Veuillez entrer votre score: "))
if score > 60:
    print("Vous avez passé.")
    if score > 80:
        print("Vous êtes très bon.")
    else:
        print("Vous êtes juste dans la moyenne.")
else:
    print("Échec à la réussite.")
    if score > 30:
        print("If faut continuer à faire du bon travail.")
    else:
        print("De très mauvaise notes.")