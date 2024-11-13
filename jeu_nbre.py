# Jeu du nombre
# Importe le module random pour générer des nombres aléatoires
import random

# Fonction énoncer le niveau de la difficulté
def menu_difficulte():
    print('\nJeu du nombre')
    print('\n===== CHOIX DE LA DIFFICULTÉ =====')
    print('1. Facile (0 à 10)')
    print('2. Moyen (0 à 100)')
    print('3. Difficile (0 à 1000)')
    print('4. Quitter')
    print('===================================')

# Fonction pour play une partie
def play(min, max):
    secret_number = random.randint(min, max)
    print(f"\nDevinez le nombre entre {min} et {max}")

# Initialisation du compteur de coups   
    coups = 0  

# Boucle : jusqu'à que le joueur trouve le nombre
    while True:
        essai = input("Votre réponse : ")
        # Si la réponse contient une chaîne de caractères au lieu d'un nombre
        if not essai.isdigit():
            print("Veuillez entrer un nombre valide.")
            continue
        # Incrémentation du compteur à chaque essai valide
        coups += 1  
        essai = int(essai)
        if essai < secret_number:
            print("C'est plus !")
        elif essai > secret_number:
            print("C'est moins !")
        else:
            print(f"Bravo ! Vous avez trouvé le nombre {secret_number}.")
            print(f"Vous avez réussi en {coups} coups.")
            # Retourne le nombre de coups joués
            return coups  
            break
def menu_principal():
    total_coups = 0
    parties_jouees = 0

# Boucle principale du menu
def menu_principal():
    while True:
        menu_difficulte()
        choix = input("Choisissez votre niveau de difficulté (1-4) : ")

        if choix == '1':
            play(0, 10)
        elif choix == '2':
            play(0, 100)
        elif choix == '3':
            play(0, 1000)
        elif choix == '4':
            print("Merci d'avoir joué. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


# Lancer le menu
if __name__ == "__main__":
    menu_principal()