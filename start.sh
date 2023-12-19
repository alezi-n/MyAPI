#!/bin/sh

# Este comando inicia o servidor Uvicorn apontando para o seu arquivo principal (main.py)
# Ele configura o host para 0.0.0.0 para que o aplicativo seja acessível externamente
# e usa a variável de ambiente $PORT fornecida pelo Railway para definir a porta.
exec uvicorn main:app --host 0.0.0.0 --port $PORT --reload
