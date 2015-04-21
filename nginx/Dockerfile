FROM nginx

ENV PROJECT yapws.com

mkdir /home/www/${PROJECT}/

add . /home/www/${PROJECT}/

run rm /etc/nginx/sites-enabled/default
run ln -s /home/www/${PROJECT}/configs/nginx.conf /etc/nginx/sites-enabled/

