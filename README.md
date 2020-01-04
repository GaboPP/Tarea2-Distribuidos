Sebastian Jara 201573523-9
Gabriel Astorga 201573591-3

** Comandos:

    -'exit': salir del chat y finalizarlo
    -'__list': otener lista de clientes
    -'__messages': obtener tus mensajes
    -'__change': cambiar de cliente al q le mandas mensajes (luego poner su puerto, se pueden ver con el comando de list)

Actividad 1:

-Se levanta con los comandos:

    1: docker-compose up --build -d 
    2: encontrar el id del contenedor con: docker ps
    3: docker attach [OPTIONS] [CONTAINER] para enviar mensaje con cliente, 
    4: luego se pueden revisar los logs con: docker exec -it  [CONTAINER] bash

Actividad 2

-Se levanta con el comando:
    * docker-compose up --build -d 

-recordar installar rabbitmq con:
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

- para agregar n clientes el local se debe ejecutar el script de cliente, así:
    python client.py [puerto] --como el 50050 por ejemplo

    y para agregar un cliente en docker debería ser así:
    -client1:
        build:
            context: ./client
            dockerfile: Dockerfile_client
            args:
            id_client: [puerto]
        command: python3 -u client.py [puerto]
        depends_on: 
            [server]
        container_name: client_name
        ports:
            - [puerto]:[puerto]
        volumes:
            - .:/usr/src/app/cliente_name

- No pudimos solventar los errores que arroja docker al inicializar, por favor ver nuestro correcto desarrollo de la tarea en localhost (reemplazando la ip default de docker: 192.168.99.100 ctrl-f2 en VSC)