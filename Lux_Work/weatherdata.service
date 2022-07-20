[Unit]
Description=Weather api updates
After=multi-user.target

[Service]
Execstart=/usr/bin/python3 -u /home/kenzi/Desktop/Project1/Lux_Work/get_weather_API_intoSQL.py
WorkingDirectory=/home/kenzi/Desktop/Project1
StandardOutput=inherit
StandardError=inherit
Restart=always
RestartSec=60
User=kenzi

[Install]
WantedBy=multi-user.target