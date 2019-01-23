# Development - Media

1. Add media paths into project's **settings.py** file
    
    ```
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    ```
2. For development settings add this line in the project's urls.py file:
    ```
    if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```