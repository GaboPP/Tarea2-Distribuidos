from concurrent import futures
import time, grpc
from datetime import datetime

import mensaje_pb2
import mensaje_pb2_grpc

class mensajeServicer(mensaje_pb2_grpc.SenderServicer, mensaje_pb2_grpc.Client_messagesServicer, mensaje_pb2_grpc.Clients_listServicer):

    def __init__(self):
        self.id = 0
        self.list_clients = []
        # Init logs
        log = open('log.txt', 'w')
        log.write('---------------------Logs------------------------\n')
        log.close()
        #Init Dicc Messages
        self.dicc_messages = {}

    def get_time(self):
        now = datetime.now()
        date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) if now.minute > 10 else str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':0' + str(now.minute)
        return date
    def recept_message(self, request, context):
        print(request)
        #Variables
        self.id += 1
        now = datetime.now()

        if request.msg == '__connection__' and request.id not in self.list_clients:
            self.list_clients.append(request.id)
        else:
            # enviar request
            self.send_message(request)

            #log mensaje
            self.log_message(request)
            #registrar mensaje de cliente
            if (request.id in self.dicc_messages):
                self.dicc_messages[request.id].append(request) 
            else:
                self.dicc_messages[request.id] = [request]
        #Responder
        response = mensaje_pb2.Message_request()
        response.id, response.msg, response.time = 1, '🗸 Received', str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute)
        return response

    def send_message(self, request):
        message, id_cliente_emisor, time, id_cliente_receptor = request.msg, request.id, request.time, str(request.id_dest)
        
        channel = grpc.insecure_channel('192.168.99.100:' + id_cliente_receptor)
        stub = mensaje_pb2_grpc.SenderStub(channel)

        Message_request = mensaje_pb2.Message_request( msg=message, time=self.get_time())
        response = stub.recept_message(Message_request)
    
    def clients_list(self, Client, context):
        for client in self.list_clients:
            response = mensaje_pb2.Client()
            response.id = client
            yield response

    def client_message(self, Client, context):
        for message in self.dicc_messages[Client.id]:
            print(message)
            yield message

    def log_message(self, request):
        log = open('log.txt', 'a')
        log.write('| Id: ' + str(self.id) + '\n')
        log.write('| Client: ' + str(request.id) + '\n')
        log.write('| Mensaje: ' + request.msg + '\n')
        log.write('| Timestamp: ' + request.time + '\n')
        log.write('-------------------------------------------------\n')
    

if __name__ == "__main__":
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    MServicer = mensajeServicer()
    mensaje_pb2_grpc.add_SenderServicer_to_server(MServicer, server)
    mensaje_pb2_grpc.add_Clients_listServicer_to_server(MServicer, server)
    mensaje_pb2_grpc.add_Client_messagesServicer_to_server(MServicer, server)

    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)