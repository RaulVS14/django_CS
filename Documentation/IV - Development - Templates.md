# Development - Templates
1. Create templates folder under your app folder
2. Create folder with the same name as your app in the templates folder

    Structure should be same in your app folder
    ```
    [your-app]
    |-[templates]
      |-[your-app]
    ```
3. Add app to into the list of installed apps, so django would know to look into the app folder for templates directory
    
    For that add app configuration to project's **settings.py** file.
    
    First copy class name from the**apps.py** file in the app folder
    
    Then add it to **settings.py** in the INSTALLED_APPS section
    
    ```
    INSTALLED_APPS = [
    '[your-app-name].apps.[class-name]'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]
    ```
    
    Side note: This helps django to find Models as well that are created in the app folder
    
4. Create your templates

5. Create your base template and add block

    ```
    {% block content %}{% endblock %}
    ```
6. Extend that base in your other templates by wrapping your template content in block tags:

    ```
    {% extends "blog/base.html" %}
    {% block content %}
        [your templates content]
    {% endblock content %}
    ```
    
7. To use static files in base template add this line in the beginning of the file

    ```
    {% load static %}
    ```
    That enables you to create links to the files
    ```
    {% static '[path-to-your-static-file-in-static-folder]' %}
    ```
    
8. For other links that have entry in **urls.py** you can use 
    
    ```
    {% url "[path-name]" %}
    ```
    ##### Example:
    
    ```
    {% url "blog-home" %}
    ```