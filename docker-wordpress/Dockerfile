FROM ubuntu:16.04

WORKDIR /root
RUN apt-get update && apt-get -yqq install php7.0-opcache php7.0-fpm php7.0 php7.0-common php7.0-gd php7.0-mysql php7.0-imap php7.0-cli php7.0-cgi \
    && apt-get -y install php-auth php7.0-mcrypt mcrypt imagemagick libruby php7.0-curl php7.0-intl php7.0-pspell php7.0-recode php7.0-sqlite3 \
    && apt-get -y install php7.0-xmlrpc php7.0-xsl php-imagick php-gettext php7.0-zip php7.0-mbstring php7.0-opcache \
    && apt-get -y install nginx wget \
    && rm -f /var/www/html/*

RUN wget https://wordpress.org/wordpress-5.1.1.tar.gz && tar -xvf wordpress-5.1.1.tar.gz -C /var/www/html && rm -f /etc/nginx/sites-enabled/default \
    && mkdir -p /run/php && echo "daemon off;" >>/etc/nginx/nginx.conf && mkdir -p /var/www/html/wordpress/wp-content/uploads \
    && chmod -R 777 /var/www/html/wordpress/wp-content/uploads \
    && sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 200M/g' /etc/php/7.0/fpm/php.ini

ADD wordpress.conf /etc/nginx/sites-enabled
ADD start.sh .

VOLUME /var/www/html
EXPOSE 80 9000

CMD /bin/bash  start.sh
