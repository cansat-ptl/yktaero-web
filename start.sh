#!/bin/bash

echo Activating venv
source ./venv/bin/activate

echo Starting server
python3 prod.py
