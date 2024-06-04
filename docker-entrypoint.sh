#!/bin/sh

alembic upgrade head
cd src && fastapi run main.py --port 8001