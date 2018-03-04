FROM ubuntu:16.04
RUN apt update
RUN apt -y install apache2 libapache2-mod-wsgi-py3 python3-pip

# The edia user is also used in the apache conf file.
RUN useradd -u 1500 -ms /bin/bash edia
RUN mkdir /var/www/erik-test-backend

WORKDIR /var/www/erik-test-backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
COPY ./apache2/erik-test-backend.conf /etc/apache2/sites-enabled/erik-test-backend.conf

ENTRYPOINT [ "python3" ]
CMD [ "backend.py" ]

#RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN chown -R edia:edia .

#CMD [ "apachectl", "-D", "FOREGROUND" ]

