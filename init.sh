#sudo rm /etc/nginx/sites-available/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo nginx - reload
