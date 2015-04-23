FROM muttex/uwsgi_ubuntu_p3

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN mkdir -p /home/www/

RUN pip3 install virtualenv

WORKDIR /home/www/

RUN virtualenv -p /usr/bin/python3 env
RUN source /home/www/env/bin/activate


#This dir will be mapped at runtime 
RUN mkdir -p /home/www/project

ADD ./configs/ /home/www/configs
RUN pip install -r /home/www/configs/requirements.txt


RUN sudo ln -s /home/www/project/uwsgi.ini /etc/uwsgi/vassals/