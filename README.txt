Sebastian Jara 201573523-9
Gabriel Astorga 201573591-3

Actividad 1:

-Se levanta con los comandos:

    1: docker-compose up --build -d 
    2: encontrar el id del contenedor con: docker ps
    3: crear una imagen (snapshot) desde el  container filesystem con: docker commit <\id> mysnapshot
    4: explorar el filesystem como bash con: docker run -t -i mysnapshot /bin/bash
    5: ls y vim para ver los logs
    6: docker rmi mysnapshot (--force) para borrar el snapshot

Actividad 2

-Se levanta con el comando:
    * docker-compose up --build -d 

-recordar installar rabbitmq con:
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

- No pudimos solventar los errores que arroja docker al inicializar, por favor ver el correcto desarrollo de la tarea en localhost