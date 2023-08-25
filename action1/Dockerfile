# Container image that runs your code
FROM python:3.10
ADD . /app
WORKDIR /app

# Install a dependency here directly into our app source dir
#RUN pip install -r requirements.txt

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
#FROM gcr.io/distroless/python3-debian10
#COPY --from=builder /app /app
#WORKDIR /app

#ENV PYTHONPATH /app
CMD ["python", "./hello_world.py"]
#ENTRYPOINT ["python"]
