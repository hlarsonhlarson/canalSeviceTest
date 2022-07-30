FROM python:latest

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY * ./

RUN pip install -r requirments.txt

EXPOSE 5432


CMD ["bash", "docker-entrypoint.sh"]
