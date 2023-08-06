[Unit]
Description=medux uvicorn daemon
After=network.target

[Service]
Environment=DJANGO_SETTINGS_MODULE=medux.settings
User=$MEDUX_USER
Group=$MEDUX_USER
WorkingDirectory=/var/www/medux
ExecStart=/var/www/medux/.venv/bin/gunicorn medux.asgi:application -w 2 -k uvicorn.workers.UvicornWorker --log-file -

[Install]
WantedBy=multi-user.target