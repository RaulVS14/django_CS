# Development - Admin

1. Create database
    
    Detect changes
    ```
    python manage.py makemigrations
    ```
    
    Update database to apply changes
    ```
    python manage.py migrate
    ```
    
2. Create superuser

    ```
    python  manage.py createsuperuser
    ```