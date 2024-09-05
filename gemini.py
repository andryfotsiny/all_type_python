import tkinter as tk
import requests
import json

# Fonction pour envoyer une requête à l'API et afficher le résultat
def envoyer_requete():
    api_key = 'AIzaSyAjnReVbpinmTsCKPGeg70I2FevX3F5qxk'
    api_url = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'

    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': api_key
    }

    data = {
        'contents': [
            {
                'role': 'user',
                'parts': [
                    {'text': entree.get()}  # Récupère le texte saisi dans l'Entry
                ]
            }
        ]
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        dialogue = response_json['candidates'][0]['content']['parts'][0]['text']
        label_resultat.config(text=f"Résultat :\n{dialogue}")
    else:
        label_resultat.config(text=f"Erreur lors de l'appel à l'API : {response.status_code}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Interface Tkinter")

# Création d'un Label pour les instructions
label_instruction = tk.Label(fenetre, text="Entrez du texte :")
label_instruction.pack(pady=10)

# Création d'une Entry pour saisir le texte
entree = tk.Entry(fenetre, width=50)
entree.pack(pady=10)

# Création d'un Button pour envoyer la requête
bouton_envoyer = tk.Button(fenetre, text="Envoyer", command=envoyer_requete)
bouton_envoyer.pack(pady=10)

# Création d'un Label pour afficher le résultat
label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.pack(pady=10)

# Lancement de la boucle principale de l'interface
fenetre.mainloop()
