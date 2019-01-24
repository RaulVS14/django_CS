# Development - Email

1. Setting up locally

    1. Run a simple SMTP server
        ```
        python -m smtpd -n -c DebuggingServer localhost:1025
        ```
    2. Configure settings in project's **settings.py** file
        
        ```
        EMAIL_HOST = 'localhost'
        EMAIL_PORT = 1025
        ```
2. Setting up Gmail

    1. Open .bash_profile file in home folder and add environment variables
        ```
        ~$: nano .bash_profile
        ```
    
        ```
        export EMAIL_USER='my_db_user'
        export EMAIL_PASS='my_db_pass_123!'
        ```
    
    2. Add configuration
        ```
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'stmp.gmail.com'
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
        EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
        ```
        EMAIL_HOST_USER and EMAIL_HOST_PASSWORD are read from env variables