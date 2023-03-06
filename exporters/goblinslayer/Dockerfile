FROM python:3.8-slim-buster

COPY /exporters/goblinslayer/requirements.txt /exporters/goblinslayer/requirements.txt


RUN pip3 install -r /exporters/goblinslayer/requirements.txt

COPY . .
WORKDIR /exporters/goblinslayer

EXPOSE 9877 

CMD [ "python3","exporter.py"]