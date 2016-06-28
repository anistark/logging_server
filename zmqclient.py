import zmq
contextInstance = zmq.Context.instance()

sock = contextInstance.socket(zmq.REQ)
sock.bind('tcp://*:8080')

clientName = 'client 4'
logLevel = 'info'
message = 'message 4'

sock.send(clientName, zmq.SNDMORE)
sock.send(logLevel, zmq.SNDMORE)
sock.send(message)
response = sock.recv()
print(response)
