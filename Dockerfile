FROM centos:8

RUN yum install sudo -y

RUN yum install httpd -y

RUN yum install php -y

COPY sample.html /var/www/html

CMD /usr/sbin/httpd -DFOREGROUND

EXPOSE 8080
