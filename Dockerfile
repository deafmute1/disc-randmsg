FROM python:3.11

RUN mkdir /app
COPY / /app
RUN pip install -r /app/requirements.txt 

ENTRYPOINT [ "python", "/app/src/main.py" ]



