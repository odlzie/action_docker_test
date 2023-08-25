# Container image that runs your code
FROM python:3.10
WORKDIR .

COPY ./requirements.txt .
# Install a dependency here directly into our app source dir
RUN pip3 install -r requirements.txt

COPY action1/ /action1

CMD ["python3", "./action1/hello_world.py"]
#ENTRYPOINT ["python"]
