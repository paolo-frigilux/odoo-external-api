import sys
import json
import xmlrpc.client
 
url = "http://192.168.252.17:8069"
db = "Pruebas-Tickets"
username = 'fernanda.frigilux@gmail.com'
password = "fernandab"
API_KEY = "3541eefd6317e36193908348cbf700a33d6779ce"

if len(sys.argv) != 2:
    print("Uso:")
    print("./main.py {Nombre del archivo}")
    exit()

fpointer = open("./result-{}.json".format(sys.argv[1]), "w")

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

uid = common.authenticate(db, username, password, {})
fpointer.write(json.dumps(models.execute_kw(db, uid, password, 'product.product', 'search_read', [[['is_published', '=', True]]], {'fields': [], 'context' :{'lang': "es_ES"}, "limit": 3})))

print(f'Logged as {username} with UID: {uid}')
