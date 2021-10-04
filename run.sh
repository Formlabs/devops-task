#!/bin/bash

# Assumes an existing virtualenv at .venv
source .venv/bin/activate
gunicorn --bind 0.0.0.0:8080 -w 2 helloapp.app:app
