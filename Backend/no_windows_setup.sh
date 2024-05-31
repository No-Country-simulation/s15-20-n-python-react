#!/bin/bash

# Crear el entorno virtual
python3 -m venv ../.venv

# Activar el entorno virtual
source ../.venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt

# Hacer las migraciones
python manage.py makemigrations
python manage.py migrate