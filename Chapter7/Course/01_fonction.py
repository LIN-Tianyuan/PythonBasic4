"""
def greet():
    print("Salut, Terrien!")
"""


def greet(firstname, lastname):
    print("Bonjour," + firstname + " " + lastname + ".")


def season_pref(season="Eté"):
    print("Ma saison préférée : " + season)


def visit(*countries):
    for country in countries:
        print("J'ai visité ce pays: " + country +".")


def list_game(competitor_1, competitor_2, competitor_3):
    print("Concurrents du jour: " + competitor_1 + " " + competitor_2 + " " +competitor_3)


# greet("Leon", "Fan")
# season_pref("Automne")
# season_pref()
# visit("Venezuela", "Allemagne", "Finlande")
# list_game("Julien", "Anne", "Eva")
list_game('Anne', 'Julien', 'Eva')
list_game(competitor_2='Julien', competitor_3='Eva', competitor_1='Anne')


