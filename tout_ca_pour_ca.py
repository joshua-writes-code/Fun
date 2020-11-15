"Tout ça pour ça..."
# On pose sur une table les dix cartes de pique numérotées de 1 à 10,
# face visibles et rangées dans cet ordre. Pour mélanger ces cartes,
# on procède de la façon suivante : on prend la première carte du paquet,
# on me au-dessus la seconde carte, puis par dessous la troisième, par-dessus
# le tout la quatrième, et ainsi jusqu'à la dernière carte.
# Il se trouve qu'après un certain nombre de mélanges de ce type,
# on retrouve l'ordre initial des dix cartes. Combien de fois faut-il donc
# répéter ce battement de cartes?

dix_cartes_de_pique = [pique for pique in range(1,11)]
nouvel_ordre = []
compteur = 0

while nouvel_ordre != [pique for pique in range(1,11)]:
    nouvel_ordre = []
    nouvel_ordre = [dix_cartes_de_pique[0]] + nouvel_ordre
    dix_cartes_de_pique.pop(0)
    while len(dix_cartes_de_pique) != 1:
        nouvel_ordre = [dix_cartes_de_pique[0]] + nouvel_ordre
        dix_cartes_de_pique.pop(0)
        nouvel_ordre = nouvel_ordre + [dix_cartes_de_pique[0]]
        dix_cartes_de_pique.pop(0)
    nouvel_ordre = [dix_cartes_de_pique[0]] + nouvel_ordre
    dix_cartes_de_pique.pop(0)
    compteur = compteur + 1
    dix_cartes_de_pique = nouvel_ordre.copy()

print(compteur)
