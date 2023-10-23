# API_Challenge_Logic_Systems
API Rest Framework

Se realizó una API muy sencilla en la cual se realizan acciones como GET, PULL, DELETE, etc. Esta API añade programadores en el endpoint "/api/v1/programmer", 
así como la documentación de esta API se encuentra en el endpoint "/docs", con la cual podemos visualizar más a profundidad en sobre las funciones que tiene la API creada.

# Docker-sample
## Documentación
En este apartado encontrarás la documentación sobre el uso de la API, además de comandos extra los cuales se podrían utilizar para levantar el proyecto

En Git bash y compilación:
Clonamos el repositorio de GitHub en una carpeta:

```shell
   git clone https://github.com/AlexMzta20/API_Challenge_Logic_Systems.git 
```

Cuando se descargue el proyecto lanzamos el comando para compilar y levantar el proyecto:

```shell
   docker build -t nombre_de_la_imagen .
```

En el comando anterior compilamos la imagen, además con el comando -t después le podemos asignar un 
nombre a nuestra imagen, seguido de la ubicación, si ya nos encontramos en la ubicación entonces solo colocamos un punto.

```shell
   docker run -d -p 8000:8000 nombre_de_la_imagen
```

Si queremos levantar la imagen usamos el comando run, seguido de dos banderas que representan -d: para que lo 
haga en segundo plano -p: para definir el puerto
Una vez corriendo el contenedor podemos revisar que esté arriba con el comando:

```shell
   docker ps
```

Si queremos revisar todos los servicios en nuestro sistema colocamos:

```shell
   docker ps -a
```

Ahora bien para detener nuestra aplicacion, despues de ubicarla con el comando "ps", seleccionamos el ID del servicio y lo colocamos con:

```shell
   docker stop id_container
```

Algunos comandos extra para conocer las imágenes y/o volúmenes que tenemos en el sistema:

```shell
   docker image ls

   docker volume ls
```

Finalmente, para eliminar alguna imagen, volumen o contenedor solo debemos utilizar el comando rm antes del ID a eliminar.

```shell
   docker volume rm id_volume

   docker image rm id_image

   docker rm id_container
```

# Docker-compose comandos
Para el caso de docker-compose, los comandos son bastante similares, comenzando por el de compilación.

Primero debemos compilar el proyecto con docker-compose y el archivo no tiene algun nombre específico utilizamos:

Primero debemos compilar el proyecto con docker-compose:

```shell
   docker-compose build
```

Una vez compilado el proyecto, lo tenemos que levantar:

```shell
   docker-compose up
```

Si queremos salir de los logs, usamos el siguiente comando:

```shell
   Ctrl + C
```

Levantarlo sin logs utilizamos -d:

```shell
   docker-compose up -d
```

Si necesitamos terminar algún servicio usamos:

```shell
   docker-compose down
```

Para conocer cual es el estado y listado de los contenedores usamos:

```shell
   docker-compose ps
```

Finalmente, si usamos un compose con nombre distinto, para utilizar los comandos previos debemos colocar la bandera -f y luego debemos colocar el nombre del compose.

```shell
   docker-compose -f nombre_compose build

   docker-compose -f nombre_compose up

   docker-compose -f nombre_compose down
```
