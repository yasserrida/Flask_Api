# FLASK API

## Project setup
```
python3 -m venv .myvirtualenv
```
```
source .myvirtualenv/bin/activate
```
```
pip -r install requirements.txt
```

## Project Run Dev
```
flask run
```

## Service config
[Unit]                                                   
Description=uWSGI instance to serve flask project        
After=network.target                                     
                                                         
[Service]                                                
User=root                                                
Group=www-data                                           
WorkingDirectory=/var/www/flask_api                            
Environment="PATH=/var/www/flask_api/.env/bin"                 
ExecStart=/var/www/flask_api/.env/bin/uwsgi --ini app.ini      
                                                         
[Install]                                                
WantedBy=multi-user.target                               
