from googleapiclient.discovery import build

# Remplacez par votre propre clé API
api_key = 'AIzaSyAjnReVbpinmTsCKPGeg70I2FevX3F5qxk'

# Créez le service Google Books
service = build('books', 'v1', developerKey=api_key)

# Exécutez une recherche
request = service.volumes().list(q='Python programming')
response = request.execute()

# Affichez les résultats
for item in response.get('items', []):
    title = item['volumeInfo'].get('title', 'No title')
    print(f'Title: {title}')
