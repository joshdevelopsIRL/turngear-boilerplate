FROM python:3.12.3-alpine3.19

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ./server.sh
