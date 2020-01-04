import time, pika, sys, json
import threading
from datetime import datetime

class client_queue:
    def __init__(self, queue, queue_server='server'):

        self.queue = str(queue)
        self.queue_server = str(queue_server)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.99.100'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_server)

    def run(self, s, pool):
        with s:
            self.name = threading.currentThread().getName()
            pool.makeActive(self.name)

        print('servidor ' + str(self.queue))
        self.receive_msgs()
    def get_time(self):
        now = datetime.now()
        date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) if now.minute > 10 else str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':0' + str(now.minute)
        return date
    def receive_msgs(self):
        # suscribirse a los mensajes que llegan mediante la f(x) callback
        channel = self.connection.channel()
        channel.queue_declare(queue=self.queue)
        channel.basic_consume( queue=self.queue, on_message_callback=self.callback)
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            pool.makeInactive(self.name)
    # función callback, recibe los mensajes
    def callback(self, ch, method, properties, body):
        request = json.loads(body.decode("utf-8"))
        msg = request['msg'] if (type(request) is dict) else json.dumps(request)
        time = request['time'] if 'time' in request else ''
        print(f'                               {msg} {time} <<<')
        ch.basic_ack(delivery_tag=method.delivery_tag)
    def close_connection(self):
        self.connection.close()

class client:

    def __init__(self, queue, queue_server='server'):
        self.queue = str(queue)
        self.queue_server = str(queue_server)
        self.commands = ['__change']
        
        # por defecto todos les envían al 1 a no ser que seas el 1
        if self.queue == '1':
            self.queue_dest = '2'
        else:
            self.queue_dest = '1'

        self.connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.99.100'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_server)

    def run(self, s, pool):
        with s:
            name = threading.currentThread().getName()
            pool.makeActive(name)

        # init connection:
        self.connect()

        print("soy el cliente", self.queue)
        client_input = ''
        try:
            while client_input != "exit":
                client_input = input(" ")
                if client_input not in self.commands:
                    self.send_message(client_input)
                elif '__change' == client_input:
                    new_receiver = input("Nombre nuevo destinatario: ")
                    self.queue_dest = str(new_receiver)
                    
        except KeyboardInterrupt:
            self.close_connection()
            pool.makeInactive(name)
    def connect(self):
        channel = self.connection.channel()
        channel.queue_declare(queue=self.queue_server)
        channel.basic_publish( exchange='', routing_key=self.queue_server, body=json.dumps({'msg': '__connect__', 'queue_from': self.queue}))

    def get_time(self):
        now = datetime.now()
        date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) if now.minute > 10 else str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':0' + str(now.minute)
        return date
    # función callback, recibe los mensajes
    def callback(self, ch, method, properties, body):
        request = json.loads(body.decode("utf-8"))
        msg = request['msg']
        time = request['time'] if 'time' in request else ''
        print(f'                               {msg} {time} <<<')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def send_message(self, msg):

        channel = self.connection.channel()
        channel.queue_declare(queue=self.queue_server)
        print(self.queue_dest)
        channel.basic_publish( exchange='', routing_key=self.queue_server, body=json.dumps({'msg': msg, 'queue_dest': self.queue_dest, 'queue_from': self.queue, 'time': self.get_time()}))

    def close_connection(self):
        self.connection.close()

class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    

if __name__ == "__main__":
    queue = sys.argv[1]

    C = client(queue)
    C_q = client_queue(queue)

    #threadpool
    pool = ThreadPool()
    s = threading.Semaphore(2)
    t1 = threading.Thread(target=C.run, name='input', args=(s, pool))
    t2 = threading.Thread(target=C_q.run, name='messages', args=(s, pool))

    t1.start()
    t2.start()