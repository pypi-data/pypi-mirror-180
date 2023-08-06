
# the upstream component nginx needs to connect to
upstream backend {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8000;
}

# configuration of the server
server {
    # substitute your machine's IP address or FQDN
    server_name ${DOMAIN};
    charset     utf-8;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
    # max upload size
    client_max_body_size 75M;
    error_log ${DOMAIN}-error.log warn;

    # Django media
#     location /media  {
#         alias /var/www/medux/media;
#     }

    location /static {
        alias /var/www/medux/static;
    }
}
