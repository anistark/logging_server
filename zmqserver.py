import zmq
import models
context = zmq.Context.instance()

sock = context.socket(zmq.REP)
sock.connect('tcp://localhost:8080')


def message_action(message):
    print('Message Received')
    print(message)
    models.insert_log(message)
    return 'message parsed'


while True:
    more = True
    parts = []
    while more:
        parts.append(sock.recv())
        more = sock.getsockopt(zmq.RCVMORE)
    response = message_action(parts)
    sock.send(response)
