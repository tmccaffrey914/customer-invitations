FROM docker.io/library/python:latest
WORKDIR /app
COPY . .

RUN pip install .

CMD [ "create-invite-list", "https://s3.amazonaws.com/intercom-take-home-test/customers.txt"]
