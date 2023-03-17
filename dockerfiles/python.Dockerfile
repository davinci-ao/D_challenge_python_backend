FROM python:latest

RUN pip install --upgrade pip
RUN pip install flask-marshmallow
RUN pip install flask-cors
#CMD ["python", "./main.py"]
