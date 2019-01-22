# Development

1. Create an app

    ```
    python manage.py startapp [your-app-name]
    ```
2. Create a view

3. Create **urls.py** in your app folder
    
    Add these lines to it
    ```
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.[function_name_in_views classe], name='[define-name]')
    ]
    ```

4. Update urlpattern with your path and add include in the project's **urls.py** file
    
    ```
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('[url-pattern]', include('[your-app-name].urls'))
    ]
    ```