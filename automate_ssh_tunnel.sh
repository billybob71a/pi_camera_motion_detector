This document describes how to do an automated reverse SSH tunnel with my Raspberry PI 3

First of all, you must have Systemd installed.

Second, go into :
/etc/systemd/system

and create a file :

tunnel.sh

sudo nano tunnel.service

[Unit]
Description=Keep tunnel open to visor for web server
After=network.target

[Service]
Environment="AUTOSSH_GATETIME=0"
ExecStart=/usr/bin/autossh -M 20001 -i /home/pi/.ssh/id_rsa root@107.172.11.137 -p 22 -N -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R *:8080:localhost:80 -R 2201:localhost:22
ExecStop=/usr/bin/pkill autossh
Restart = always
[Install]
WantedBy=multi-user.target


Save the file

sudo systemctl daemon-reload

sudo systemctl enable tunnel.service

sudo systemctl start tunnel.service

This method is much better than just adding an script into the suco crontab -e, because I found that the connection does not always reconnect back
on  reboot with crontab -e.

The good thing about systemd is that it does the pkill for the autossh.

Otherwise, the ssh tunnel might linger on in the server side causing trouble for an immediate subsequent connection such as someting that may happen during a reboot with cron job.




