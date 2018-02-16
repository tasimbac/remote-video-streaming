#!/bin/bash

sudo apt-update && 
sudo apt-get install -y httpd && 
wget -O /var/www/html/index.html https://s3-eu-west-1.amazonaws.com/uct-demo/index.html /var/www/html/