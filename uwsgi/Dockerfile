FROM muttex/uwsgi_ubuntu_p3


RUN mkdir -p /home/www/

RUN pip3 install virtualenv

WORKDIR /home/www/

RUN virtualenv -p /usr/bin/python3 env
RUN ["/bin/bash", "-c", "source /home/www/env/bin/activate"]


#This dir will be mapped at runtime 
RUN mkdir -p /home/www/project

RUN pip3 install -r /home/www/configs/requirements.txt

ADD ./configs/ /home/www/configs

RUN sudo ln -s /home/www/configs/uwsgi.ini /etc/uwsgi/vassals/