# Deployment - Setting up server

1. SSH into your server
    
    ```
    ssh root@[your.ip.for.machine]
    ```
    
2. Install software updates

    ```
    apt-get update && apt-get upgrade
    ```

3. Set hostname
    
    ```
    hostnamectl set-hostname django-server
    ```
    
4. Set hostname in hosts file

    ```
    sudo nano /etc/hosts
    ```
    Add line
    ```
    [your.ip.for.machine] [hostname]
    ```

5. Create limited user

    ```
    adduser [your-username]
    ```
    
    And follow the instructions for setting password
    
6. Add user to `sudo` group

    ```
    adduser [your-username] sudo
    ```
    
7. Log in as a new user

    ```
    ssh [your-username]@[your.ip.for.machine]
    ```

8. Setup SSH authentication

    1. Create ssh folder on server 

        ```
        mkdir -p ~/.ssh
        ```
    2. Create ssh keys on your computer
    
        ```
        ssh-keygen -b 4096
        ```
    3. Copy ssh pub key to server
        
        ```
        scp ~/.ssh/id_rsa.pub [your-username]@[your.ip.for.machine]:~/.ssh/authorized_keys
        ```
    4. Log in with user and enter password
    
        ```
        ssh [your-username]@[your.ip.for.machine]
        ```
    5. Set permissions for .ssh directory in the machine
    
        ```
        sudo chmod 700 ~/.ssh/
        ```
        
        ```
        sudo chmod 600 ~/.ssh/*
        ```
        
    6. Test ssh key
        ```
        ssh [your-username]@[your.ip.for.machine]
        ```
        It shouldn't ask for password
        
    7. Remove passwords logins
        
        Edit the sshd_config file on the machine
    
        ```
        sudo nano /etc/ssh/sshd_config
        ```
        
        Change following fields to shown values:
        ```
        PermitRootLogin no
        ```
        ```
        PasswordAuthentication no
        ```
        
        and save
    8. Restart ssh service
    
        ```
        sudo systemctl restart sshd
        ```
9. Setup firewall
    1. Install UFW
        ```
        sudo apt-get install ufw
        ```
    2. Allow outgoing traffic
        
        ```
        sudo ufw default allow outgoing
        ```
    3. Deny incoming
    
        ```
        sudo ufw default deny incoming
        ```
    4. Add ssh exception to incoming rule
        ```
        sudo ufw allow ssh
        ```
    5. Allow necessary ports
    
        ```
        sudo ufw allow [your-port]
        ```
    6. Setup firewall
    
        ```
        sudo ufw enable
        ```
        answer 'yes' on prompt
10. Create `requirements.txt` file

    1. Run following command
    
        ```
        pip freeze > requirements.txt
        ```
    2. If it's not in your project folder, copy it there from where you created it to
    
11. Copy project file to server

    ```
    scp -r /path/to/django_project [your-username]@[your.ip.for.machine]:~/
    ```

12. Install pip

    ```
    sudo apt-get install python3-pip
    ```
13. Install virtual environment

    ```
    sudo apt-get install python3-venv
    ```
    or
    
    get Conda installation file
    ```
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh > Miniconda3-latest-Linux-x86_64.sh
    ```
    and install it with bash
    ```
    Miniconda3-latest-Linux-x86_64.sh
    ```
14. Create virtual environment
    ```
    python3 - m venv django_project/
    ```
    or on Conda in the django_project folder
    ```
    conda create -n [environment-name] python=3
    ```
15. Activate virtual environment

    enter the folder

    ```
    source venv/bin/activate
    ```
    or on Conda
    ```
    source activate django_project
    ```
    
16. PIP install requirements

    
    ```
    pip install -r requirements.txt
    ```
    
17. Modify **settings.py** file in project folder to new values:
    ```
    ALLOWED_HOST = ['[your.ip.for.machine]']
    ```
    and
    ```
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    ```
18. Collect static files

    ```
    python manage.py collectstatic
    ```
19. Run django instance

    ```
    python manage.py runserver 0.0.0.0:[your-port]
    ```
20. Install web-server on machine
    Example:
    ```
    sudo apt-get install apache2
    ```
   
21. Install wsgi(web server gateway interface) on machine

    ```
    sudo apt-get install libapache2-mod-wsgi-py3
    ```
22. Configure web server
    ```
    cd /etc/apache2/sites-available/
    ```
    
    Copy config file for base
    ```
    sudo cp 000-default.conf django_project.conf
    ```
    
    ```
    Alias /static /home/[your-username]/[django_project]/static
    <Directory /home/[your-username]/[django_project]/static>
        Require all granted
    </Directory>
    
    Alias /media /home/[your-username]/[django_project]/media
    <Directory /home/[your-username]/[django_project]/media>
        Require all granted
    </Directory>
    
    <Directory /home/[your-username]/[django_project]/[django_project]>
        <Files wsgi.py>
            Require all granted
        </Files
    </Directory>
    
    WSGIScriptAlias / /home/[your-username]/[django_project]/[django_project]/wsgi.py
    WSGIDaemonProcess [django_app_name] python-path=/home/[your-username]/[django_project] python-home=[path-to-virtual-env]
    WSGIProcessGroup [django_app_name]
    ```
    
23. Enable site

    ```
    sudo a2ensite django_project
    ```

25. Disable default config

    ```
    sudo a2dissite 000-default.conf
    ```

26. Give rights to webserver to access database

    ```
    sudo chown :www-data [django_project]/db.sqlite3
    ```
    
    ```
    sudo chmod 664 [django_project]/db.sqlite3
    ```
    
    ```
    sudo chown :www-data [django_project]/
    ```

    ```
    sudo chmod 775 [django_project]/
    ```
    
27. Do the same for media folder

    ```
    sudo chown -R :www-data [django_project]/media/
    ```
    
    ```
    sudo chmod -R 775 [django_project]/media
    ```

28. Create configuration file if you can't add env variables

    ```
    sudo touch /etc/[django_project]/config.json
    ```
    
    Take the secret key from **settings.py**
    
    ```
    sudo nano /etc/[django_project]/config.json
    ```
    Add this into the file
    ```
    {
        "SECRET_KEY": "[your-secret-django-key]"
        "EMAIL_USER": "",
        "EMAIL_PASS":""
    }
    ```
    Load in the config file
    ```
    with open('/etc/[django_project]/config.json') as config_file:
        config = json.load(config_file)
    ```
    Set following values
    ```
    SECRET_KEY = config['SECRET_KEY']
    ```
    
    ```
    DEBUG=False
    ```
    
    ```
    EMAIL_HOST_USER = config.get('EMAIL_USER')
    EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')
    ```
29. Change firewall
    ```
    sudo ufw delete allow 8000
    ```
    
    ```
    sudo ufw allow http/tcp
    ```
30. Restart web server
    ```
    sudo service apache2 restart
    ```
31. You can also check deployment [Django Deployment Checklist](https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/)