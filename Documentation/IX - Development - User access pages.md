# IX - Development - User access pages

1. Import auth views module
    ```
    from django.contrib.auth import views as auth_views
    ```

2. Create new paths in the project's **urls.py** file
    ```
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    ```
3. Define user landing page afte login in the project's **settings.py** file

    ```
    LOGIN_REDIRECT_URL = 'blog-home'
    ```
4. Create the templates

5. Limit user access to views:

    1. Import **login_required** module
        ```
        from django.contrib.auth.decorators import login_required
        ```
    2. Add decorator to view
        ```
        @login_required
        def profile(request):
        ```
    3. Define the login url in project's **settings.py**
        ```
        LOGIN_URL = '[name-of-login-path]'
        ```