
# Constante speed m/h
KMH_TO_MPH = 1.609

# Demander vitesse km/h
speed_kmh = float(input('Veuillez entrer une vitesse en km/h : '))

# Convertir la vitesse
speed_mh = speed_kmh / KMH_TO_MPH

# Afficher le résultat
print(f'{speed_kmh} km/h équivaut à {speed_mh:.2f} m/h')
print(f"{speed_kmh} km/h équivaut à {round(speed_mh, 2)} m/h")