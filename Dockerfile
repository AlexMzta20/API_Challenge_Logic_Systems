# Se utiliza la imagen oficial de Python 3.10.4 basada en Alpine 3.15
FROM python:3.10.4-alpine3.15

# Se establece la variable de entorno PYTHONUNBUFFERED en 1 para asegurar que 
# la salida de Python se envíe directamente al terminal sin ser almacenada en búfer
ENV PYTHONUNBUFFERED 1

# Se establece el directorio de trabajo del contenedor en /app
WORKDIR /app

# Se actualiza el índice de paquetes y se instalan las dependencias necesarias para el proyecto
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

# Se copia el archivo requirements.txt al directorio de trabajo del contenedor
COPY ./requirements.txt ./

# Se instalan las dependencias del proyecto especificadas en requirements.txt
RUN pip install -r requirements.txt

# Se copian todos los archivos del directorio actual al directorio de trabajo del contenedor
COPY ./ ./

# Se expone el puerto 8000 del contenedor
EXPOSE 8000

# Se ejecuta el script django.sh al iniciar el contenedor
CMD [ "sh", "/app/django.sh" ]
