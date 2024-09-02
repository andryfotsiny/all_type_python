import requests
import json

# Remplacez par votre clé API
api_key = 'AIzaSyAjnReVbpinmTsCKPGeg70I2FevX3F5qxk'

# URL de l'API pour générer le contenu
api_url = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'

# Les en-têtes pour inclure la clé API et spécifier le type de contenu
headers = {
    'Content-Type': 'application/json',
    'x-goog-api-key': api_key
}

# Le corps de la requête (données JSON) pour générer un dialogue en français
data = {
    'contents': [
        {
            'role': 'user',
            'parts': [
                {'text': 'Simule une conversation en français entre deux personnes discutant de la cuisine française.'}
            ]
        }
    ]
}

# Faire la requête POST à l'API
response = requests.post(api_url, headers=headers, json=data)

# Vérifiez si la requête a réussi
if response.status_code == 200:
    # Extraire la réponse JSON
    response_json = response.json()
    # Afficher le contenu généré
    dialogue = response_json['candidates'][0]['content']['parts'][0]['text']
    print(f"Dialogue en français :\n{dialogue}")
else:
    print(f"Erreur lors de l'appel à l'API : {response.status_code}")
    print(response.text)
