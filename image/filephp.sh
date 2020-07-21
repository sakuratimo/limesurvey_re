#!/bin/bash
chmod -w /var/www/html/application/controllers/admin/LimeSurveyFileManager.php
rm -f  /var/www/html/themes/admin/favicon.ico 
cp /usr/image/logo.png  /var/www/html/tmp/assets/d680af08
cp /usr/image/donate.png /var/www/html/themes/admin/Sea_Green/images
cp /usr/image/logo.png /var/www/html/tmp/assets/76dde73a
cp /usr/image/survey_list_header.png /var/www/html/tmp/assets/76dde73a
cp /usr/image/poweredby.png /var/www/html/tmp/assets/76dde73a

