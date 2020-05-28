FROM ubuntu:latest

RUN mkdir app
WORKDIR /app

RUN apt update -y
RUN apt upgrade -y

COPY nginx_install_default nginx_install_default
RUN apt install nginx -y < nginx_install_default
RUN apt install python3 python3-pip gunicorn -y


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN cp -r /usr/local/lib/python3.8/dist-packages/ntc_templates /root/ntc-templates

COPY nginx_default_config nginx_default_config
RUN cat nginx_default_config > /etc/nginx//sites-available/default

COPY entry_point.sh /
RUN chmod +x /entry_point.sh

COPY . .

ENTRYPOINT ["/entry_point.sh"]

