# ōbtener imagen base
FROM --platform=linux/amd64 python:3.11.4-slim-bullseye

#Definir variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#DEFINIR DIRECTRORIO DE TRABAJO
WORKDIR /code


#INSTALACION DE DEPENDENCIAS

COPY ./requerimientos.txt .
RUN pip install -r requerimientos.txt
#COPIAR PROYECTO
COPY . .
