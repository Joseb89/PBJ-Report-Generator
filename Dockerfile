FROM python:3.14.4-alpine3.23

RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-dev \
    pkgconfig

RUN pip install --no-cache-dir mysqlclient

WORKDIR /app

COPY src /app

COPY --chmod=444 requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 5000

CMD ["python", "app.py" ]