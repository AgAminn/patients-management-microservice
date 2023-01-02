FROM python:3.9-alpine3.15 as dev
RUN mkdir /app/
WORKDIR /app/

RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN pip install --upgrade pip


COPY ./src/requirements.txt /app/requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

COPY ./src/ /app/
ENV FLASK_APP=app.py

CMD ["python3", "app.py"]