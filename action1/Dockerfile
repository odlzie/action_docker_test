## Container image that runs your code
#FROM python:3.10
#ADD . /app
#WORKDIR /app

## Install a dependency here directly into our app source dir
## RUN pip install -r requirements.txt

#CMD ["python3", "hello_world.py"]
##ENTRYPOINT ["echo pwd"]

FROM python:3.10-alpine AS base
WORKDIR /app
#COPY requirements.txt /app
#RUN pip install -r requirements.txt

FROM base as src
COPY . /app

FROM src as prod
ENTRYPOINT ["python3"]
CMD ["./action1/hello_world.py"]
