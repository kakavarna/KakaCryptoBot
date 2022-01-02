#MODULE IMPORTS
import sys
import json
import mariadb
import util

queryString = "SELECT * from cmcdata"
queryResult = util.execute_query(queryString)
for row in queryResult:
    print(row)

##connect to  mariadb
#jsonreader = open('config.json')
#config = json.load(jsonreader)

#dbuser = config['dbUser']
#dbpwd = config['dbPassword']
#try: conn = mariadb.connect(
#    host='vin-node2',port=3306,user=dbuser,password=dbpwd,database='kakacryptodata'
#)
#except mariadb.Error as e:
#    print(f"Error connecting to MariaDB Platform: {e}") 

#cur = conn.cursor()

#cur.execute(
#    "SELECT * from cmcdata")
#print("complete")

#conn.close()
