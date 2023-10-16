FROM python:3.8

ENV TZ=Asia/Bishkek
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /source
WORKDIR /source
COPY requirements.txt /source/
RUN pip install -r requirements.txt

COPY . /source
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8888

