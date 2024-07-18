#!/bin/sh

alembic upgrade head
python3 gen_admin.py
cd src && fastapi run main.py --port 8001