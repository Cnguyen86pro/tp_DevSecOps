#Les imports
import dotenv
import os
import requests
import logging
from hide import hide
import datetime
import logging
import time

#Chargements des variables d'environnement
dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
API_URL = os.getenv('API_URL')

#Configuration pour les logs
now = datetime.datetime.now().strftime('%Y-%m-%d')
log_filename = f'logs/{now}.log'
json_filename = f'reports/{now}-App.json'

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
    ]
)

url = f'{API_URL}/status?{API_TOKEN}'
headers = {'Authorization': f'Bearer {API_TOKEN}'}

try:
    if not API_TOKEN:
        raise ValueError('Token vide')
    
    r = requests.get(url, headers=headers, timeout = 5)
    logging.info(f'HTTP response from {hide(r.url, API_TOKEN)} with Status: {r.status_code}')

    #Récupérer les informations
    result = []
    json = r.json()

    result.append(
    {
        'app': json['app'],
        'status': json['status'],
        'response_time': json['response_time'],
        'timestamp': json['timestamp'],
    })

    with open(json_filename, 'w') as file:
        file.write('result\n')


except requests.exceptions.HTTPError as e:
    logging.error(f'HTTP error: {hide(str(e), API_TOKEN)}')

except requests.exceptions.RequestException as e:
    logging.error(f'Network error on {hide(url, API_TOKEN)}')