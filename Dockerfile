FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_simple_chat
WORKDIR /django_simple_chat
ADD requirements.txt /django_simple_chat/
RUN pip install -r requirements.txt
ADD . /django_simple_chat/