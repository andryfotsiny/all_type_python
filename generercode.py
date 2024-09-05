import requests

api_key = 'AIzaSyAjnReVbpinmTsCKPGeg70I2FevX3F5qxk'
api_url = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'

headers = {
    'Content-Type': 'application/json',
    'x-goog-api-key': api_key,
}

data = {
    'contents': [
        {
            'role': 'user',
            'parts': [
                {'text': 'Generate HTML code for a responsive navigation bar with links to Home, About, Services, and Contact.'}
            ]
        }
    ]
}

response = requests.post(api_url, headers=headers, json=data)

if response.status_code == 200:
    generated_code = response.json().get('candidates')[0]['content']['parts'][0]['text']
    print(generated_code)
else:
    print(f'Error: {response.status_code} - {response.text}')
