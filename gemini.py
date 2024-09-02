import requests

# Remplacez par votre clé API Gemini
api_key = 'AIzaSyAjnReVbpinmTsCKPGeg70I2FevX3F5qxk'

# URL de l'API pour générer le texte (mise à jour avec un point de terminaison fictif)
api_url = 'https://api.gemini.com/text-generation'

# Les en-têtes pour inclure la clé API
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Le prompt pour générer le dialogue en français
data = {
    'prompt': 'dialogue français',
    'language': 'fr',  # Assurez-vous que l'API supporte la langue spécifiée
    'max_tokens': 100  # Ajustez le nombre de tokens selon vos besoins
}

# Faire la requête POST à l'API
response = requests.post(api_url, headers=headers, json=data)

# Vérifiez si la requête a réussi
if response.status_code == 200:
    # Extraire le texte généré depuis la réponse JSON
    generated_text = response.json().get('text', 'Aucun texte généré')
    print(f"Dialogue en français :\n{generated_text}")
else:
    print(f"Erreur lors de l'appel à l'API : {response.status_code}")
    print(response.text)
