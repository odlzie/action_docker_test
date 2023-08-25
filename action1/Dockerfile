# Container image that runs your code
FROM python:3.10
WORKDIR .

ADD ./requirements.txt .
# Install a dependency here directly into our app source dir
RUN pip3 install -r requirements.txt

ADD ./action1/ ./action1

CMD ["python3", "./action1/hello_world.py"]
#ENTRYPOINT ["python"]
