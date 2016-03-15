sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-enabled/default?
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/nginx restart
#sudo /etc/init.d/gunicorn restart
#gunicorn -b 0.0.0.0:8080 hello &
