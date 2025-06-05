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
api_token = os.getenv('API_TOKEN')
api_url = os.getenv('API_URL2')

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

url = f'{api_url}status?{api_token}'
headers = {'Authorization': f'Bearer {api_token}'}

try:
    if not api_token:
        raise ValueError('Token vide')
    
    r = requests.get(url, headers=headers, timeout = 5)
    logging.info(f'HTTP response from {hide(r.url, api_token)} with Status: {r.status_code}')

    #Récupérer les informations
    json = r.json()
    with open(json_filename, 'w') as file:
        file.write(f'{json}\n')


except requests.exceptions.HTTPError as e:
    logging.error(f'HTTP error: {hide(str(e), api_token)}')

except requests.exceptions.RequestException as e:
    logging.error(f'Network error on {hide(url, api_token)}')