#FROM python:3.9.12-slim-buster
FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]