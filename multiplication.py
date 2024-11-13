# Demander à l'utilisateur d'entrer un nombre
nombre = int(input("Entrez un nombre pour voir sa table de multiplication : "))

# Créer une liste pour stocker les résultats
table = []

# Calculer les 10 premiers résultats et les stocker dans la liste
for i in range(1, 11):
    resultat = nombre * i
    
    # Vérifier si le résultat est un multiple de 3
    if resultat % 3 == 0:
        table.append(f"{resultat}*")  # Ajouter une astérisque pour les multiples de 3
    else:
        table.append(str(resultat))

# Afficher la liste des résultats
print(f"\nTable de multiplication de {nombre} :")
print(", ".join(table))

print("\nNote : Les nombres suivis d'une astérisque (*) sont des multiples de 3.")
# print(table)