FROM ubuntu:16.04
RUN apt update
RUN apt install -y python3-pip

# The edia user is also used in the apache conf file.
RUN useradd -u 1500 -ms /bin/bash edia
RUN mkdir -p /var/www/beach-backend

WORKDIR /var/www/beach-backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3" ]
CMD [ "backend.py" ]

RUN chown -R edia:edia .

