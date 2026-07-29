FROM python:3.14.4-alpine3.23

WORKDIR /app

COPY src /app

COPY --chmod=444 requirements.txt /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-dev \
    pkgconfig \
    curl

RUN pip install --no-cache-dir -r requirements.txt mysqlclient

EXPOSE 5000

CMD ["python", "app.py" ]