#!/bin/bash

echo Activating venv
source ./venv/bin/activate

echo Starting server
daphne yktaero.asgi:application -p 5000
