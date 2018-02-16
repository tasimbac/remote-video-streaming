#!/bin/bash

sudo systemctl start httpd &&
sudo update-rc.d httpd start
