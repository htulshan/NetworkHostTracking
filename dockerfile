FROM ubuntu:latest

RUN mkdir app
RUN mkdir app/dockerfiles
WORKDIR /app

RUN apt update -y
RUN apt upgrade -y

COPY dockerfiles/nginx_install_default dockerfiles/nginx_install_default
RUN apt install nginx -y < dockerfiles/nginx_install_default
RUN apt install python3 python3-pip gunicorn -y


COPY requirements requirements
RUN pip3 install -r requirements
RUN cp -r /usr/local/lib/python3.8/dist-packages/ntc_templates /root/ntc-templates

COPY dockerfiles/nginx_default_config dockerfiles/nginx_default_config
RUN cat dockerfiles/nginx_default_config > /etc/nginx//sites-available/default

COPY dockerfiles/entry_point.sh /
RUN chmod +x /entry_point.sh

COPY . .

ENTRYPOINT ["/entry_point.sh"]

