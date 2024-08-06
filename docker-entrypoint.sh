#!/bin/sh

alembic upgrade head
python3 gen_admin.py
fastapi run src/main.py --port 8001 --workers 3