import mysql.connector

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="Aaron",
    password="Aaron07!",
    database="LaPlateforme"
)

# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter la requête pour calculer la capacité totale des salles
cursor.execute("SELECT SUM(capacite) FROM salle")

# Récupérer le résultat
capacite_totale = cursor.fetchone()[0]

# Afficher le résultat
print(f"La capacité de toutes les salles est de : {capacite_totale}")

# Fermer le curseur et la connexion
cursor.close()
conn.close()
