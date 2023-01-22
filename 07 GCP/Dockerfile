FROM python:3.7

WORKDIR /app

ADD ./model ./model
ADD server.py server.py
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "server:app" ]