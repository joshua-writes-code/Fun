"Un mélange de cartes"
# On tient dans une main les treize cartes de pique, face visibles et
# rangées dans un certain ordre. On prend la première carte et on la pose sur
# une table. On met la seconde carte à la fin du paquet tenu à la main.
# On prend la troisième carte et on la pose sur la carte déjà sur la table.
# On prend la quatrième carte à la fin du paquet tenu à la main. Et ainsi de suite,
# jusqu'a déposer toutes les cartes sur la table.

# Quel est l'ordre initial des treize cartes dans la main pour que l'ordre dans
# lequel les cartes apparaissent sur la table soit 2 (pour celle du dessus), 3, 4... dame, roi et as
# pour celle du dessous?

treize_cartes = ['2','3','4','5','6','7','8','9','10','V','D','R','A']
nouvel_ordre = []

while len(treize_cartes) != 1:
    nouvel_ordre=[treize_cartes[0]]+ nouvel_ordre
    treize_cartes.pop(0)
    nouvel_ordre=[nouvel_ordre[len(nouvel_ordre)-1]]+ nouvel_ordre[0:len(nouvel_ordre)-1]
nouvel_ordre=[treize_cartes[0]]+nouvel_ordre
print(nouvel_ordre)
