from datetime import datetime

import grpc
from concurrent import futures
import mensaje_pb2
import mensaje_pb2_grpc
import sys


class client:

    def __init__(self, id):
        self.id_port = int(id)

        # por defecto todos les envían al 50050 a no ser que seas el 50050
        if self.id_port == 50050:
            self.cliente_dest = 50049
        else:
            self.cliente_dest = 50050
        # open a gRPC channel
        self.channel = grpc.insecure_channel('192.168.99.100:50051')
        self.stub = mensaje_pb2_grpc.SenderStub(self.channel)
        self.stub_l = mensaje_pb2_grpc.Clients_listStub(self.channel)
        self.stub_m = mensaje_pb2_grpc.Client_messagesStub(self.channel)

    def get_time(self):
        now = datetime.now()
        date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) if now.minute > 10 else str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':0' + str(now.minute)
        return date

    def send_message(self, message):
        Message_request = mensaje_pb2.Message_request( id=self.id_port, msg=message, time=self.get_time(), id_dest=self.cliente_dest)
        response = self.stub.recept_message(Message_request)
        # print(response.msg, response.time)
        
    def recept_message(self, request, context):
        now = datetime.now()

        response = mensaje_pb2.Message_request()
        response.id, response.msg, response.time = 1, '🗸 Seen', str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute)

        print('                               ' + request.msg, request.time + ' <<<')
        return response
    def clients_list(self):
        Client = mensaje_pb2.Client( id=self.id_port)
        for cliente in self.stub_l.clients_list(Client):
            if cliente.id == self.cliente_dest:
                print('[*ACTUAL*]', cliente)
            else:
                print(cliente)

    def client_message(self):
        Client = mensaje_pb2.Client( id=self.id_port)
        print(('---------------------Tus mensajes------------------------'))
        for message in self.stub_m.client_message(Client):
            print('| Mensaje: ' + message.msg)
            print('| Timestamp: ' + message.time)
            print('-------------------------------------------------')
    def change_dest(self, id_port_dest):
        self.cliente_dest = int(id_port_dest)
    def connection(self):
        Message_request = mensaje_pb2.Message_request( id=self.id_port, msg='__connection__')
        response = self.stub.recept_message(Message_request)
        

if __name__ == "__main__":
    port = sys.argv[1]
    C = client(port)
    # create a gRPC server_client client
    server_client = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mensaje_pb2_grpc.add_SenderServicer_to_server(client(port), server_client)
    # listen on port
    server_client.add_insecure_port('[::]:' + port)
    server_client.start()

    commands = ['exit', '__list', '__messages', '__change']
    C.connection()
    client_input = ''   
    try:
        while client_input != "exit":
            client_input = input(" ")
            if client_input not in commands:
                C.send_message(client_input)
            elif client_input == '__list':
                C.clients_list()
            elif client_input == '__messages':
                C.client_message()
            elif client_input == '__change':         
                C.clients_list()
                client_input = input("Puerto nuevo destinatario: ")
                C.change_dest(client_input)
    except KeyboardInterrupt:
        server_client.stop(0)
