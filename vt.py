#!/usr/bin/env python3
from io import BytesIO
from gzip import GzipFile
from io import StringIO
from subprocess import call
import zmq

context = zmq.Context()

subscriber = context.socket(zmq.XSUB)
#subscriber.connect("tcp://pubsub.ndovloket.nl:7658")
subscriber.connect("tcp://pubsub.besteffort.ndovloket.nl:7664")

#subscriber.send(chr(0x01) + "/CXX/KV6posinfo") # 0x01 = subscribe, 0x00 = unsubscribe
#subscriber.send(chr(0x01) + "/RIG/NStreinpositiesInterface5") # 0x01 = subscribe, 0x00 = unsubscribe
subscriber.send((chr(0x01) + "/RIG/NStreinpositiesInterface5").encode('utf-8'))

x=0

while True:

        multipart = subscriber.recv_multipart()
        address = multipart[0]
        #contents = ''.join(multipart[1:])
        contents = b''.join(multipart[1:])
        #contents = GzipFile('','r',0,StringIO(contents)).read()
        contents = GzipFile('', 'r', 0, BytesIO(contents)).read().decode('utf-8')
        filename="tmp/data.xml"
        file = open(filename,"w")
        file.write(contents)
        file.close()
        #call(["vt_process.php"])
        


subscriber.close()
context.term()
