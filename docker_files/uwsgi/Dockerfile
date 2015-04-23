FROM muttex/uwsgi_ubuntu_p3

#This dir will be mapped at runtime 
RUN mkdir -p /home/www/

RUN mkdir -p /var/pip_requir
ADD ./requirements.txt /var/pip_requir/requirements.txt
RUN pip3 install -r /var/pip_requir/requirements.txt

RUN sudo ln -s /home/www/configs/uwsgi.ini /etc/uwsgi/vassals/
