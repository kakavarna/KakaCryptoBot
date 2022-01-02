################################################################################################
#IMPORT MODULES
import sys
import json
import mariadb
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

################################################################################################
#GLOBAL VARS
jsonreader = open('config.json')
config = json.load(jsonreader)
__DBUSER__ = config['dbUser']
__DBPWD__ = config['dbPassword']
__CMCKEY__ = config['cmcKey']
__DISCORDKEY__ = config['token']
__PREFIX__ = config['prefix']
__CHANNEL__ = config['textChannel']

################################################################################################
#FUNCTIONS

#returns a db connection
def db_connect():
    try: conn = mariadb.connect(
        host='vin-node2',port=3306,user=__DBUSER__,password=__DBPWD__,database='kakacryptodata'
    )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None
    return conn

#Execute a single query
def execute_query(query):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    print("completed query")
    return result

def update_CMCdata():
    return None

def getLatest_CMCdata():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'2000',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': __CMCKEY__
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return None