FROM python:3.12-bookworm as python-base

WORKDIR /app
COPY . /app

RUN chmod +x ./docker-entrypoint.sh
RUN pip install -r requirements.txt

EXPOSE 8001
ENTRYPOINT ["./docker-entrypoint.sh"]