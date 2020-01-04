import pika, time, json
from datetime import datetime

class server:

    def __init__(self, queue = "server"):
        self.id = 0
        self.queue = queue
        self.commands = ['exit', '__list', '__messages', '__connect__']
        self.list_clients = []
        self.dicc_messages = {}
        
        # Init logs
        log = open('log.txt', 'w')
        log.write('---------------------Logs------------------------\n')
        log.close()

        self.connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.99.100 '))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)
        # self.channel.queue_delete(queue="server")

        # suscribirse a los mensajes que llegan mediante la f(x) callback
        self.channel.basic_consume( queue=self.queue, on_message_callback=self.callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    # función callback, recibe los mensajes
    def callback(self, ch, method, properties, body):
        self.id +=1
        msg = json.loads(body.decode("utf-8"))
        print(" [x] Received %r" % msg)
        
        if msg['msg'] not in self.commands:
            print(msg['msg'])

            #log mensaje
            self.log_message(msg)

            #registrar mensaje de cliente
            if (msg['queue_from'] in self.dicc_messages):
                self.dicc_messages[msg['queue_from']].append(msg) 
            else:
                self.dicc_messages[msg['queue_from']] = [msg]

            #reenviar
            self.send_message(body, msg['queue_dest'])
        elif msg['msg'] == '__list':
            print(msg['msg'])
            self.clients_list(msg, msg['queue_from'])
        elif msg['msg'] == '__messages':
            print(msg['msg'])
            self.client_message(msg, msg['queue_from'])
        elif msg['msg'] == '__connect__':
            print(msg['msg'])
            self.register_client(msg['queue_from'])
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def register_client(self, client):
        self.list_clients.append(client)

    def send_message(self, msg, queue_dest):
        channel = self.connection.channel()
        channel.queue_declare(queue = queue_dest)

        channel.basic_publish(exchange='', routing_key=queue_dest, body=msg)

    def log_message(self, request):
        #la cola guarda y dps envia lo que faltba por enviarse.
        log = open('log.txt', 'a')
        log.write('| Id: ' + str(self.id) + '\n')
        log.write('| Client: ' + str(request['queue_from']) + '\n')
        log.write('| Mensaje: ' + request['msg'] + '\n')
        log.write('| Timestamp: ' + request['time'] + '\n')
        log.write('-------------------------------------------------\n')

    def clients_list(self, msg, queue_from):
        msg['msg'] = json.dumps(self.list_clients)
        del msg['time']
        self.send_message( bytes(json.dumps(msg), "utf-8"), queue_from)

    def client_message(self, msg, queue_from):
        if queue_from in self.dicc_messages:
            messages = [message['msg'] for message in self.dicc_messages[queue_from]]
            response = bytes(json.dumps(messages), "utf-8")
        else:
            response = bytes(json.dumps({'msg': 'sin mensajes :('}), "utf-8")
        print(response)
        self.send_message( response, queue_from)

    def close_connection(self):
        self.connection.close()

servidor = server()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    servidor.close_connection()