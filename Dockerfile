FROM python:3.7-alpine

MAINTAINER Anders Dahl "andersoldahl@gmail.com"

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]