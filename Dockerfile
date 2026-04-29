FROM python:3.14.4-alpine3.23

RUN addgroup -S pbjgroup && adduser -S pbjuser -G pbjgroup

WORKDIR /app

COPY src /app

COPY --chmod=444 PBJ-Report.csv /app

RUN pip install -r requirements.txt 

EXPOSE 5000

USER pbjuser

CMD ["python", "app.py" ]