#Socket client example in python

import socket   #for sockets
import requests

def consumeGETRequestSync():

    url = 'http://184.173.18.156/api/session/?api_key=a1500be66cd74841b6987dc2d1db81d4'

    # call get service with headers and params
    response = requests.get(url)
    return str(response.text)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",8000))
s.listen(2)
(client,(ip,port)) = s.accept()
while True:
        data = consumeGETRequestSync()
        if not data: break
        #print "Sending data t client"
        client.send(data)

client.close()
