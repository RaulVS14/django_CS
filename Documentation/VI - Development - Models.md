# Development - Models

1. For this you can use **models.py** in your app folder

2. Create a class

    ```
    class [your-class-name](models.Model):
        [... Add your class fields ...]
    ```
3. You can use imported models module to define field values
    ```
    models.CharField() - characters field, short text field
    models.TextField() - long form text
    models.DateTimeField() - date-time field, can take arguements
    
    Some date-time field arguements: 
    [
        auto_now=True(for everytime the object is changed),
        auto_now_add=True(adds timestamp when object created, but can't be updated after creation),
        default=timezone.now(requires line -> from django.utils import timezone )
    ] 
    
    models.ForeignKey - requires -> from django.contrib.auth.models import User (User, on_delete=[specify action, i.e. models.CASCAD])
    ```
4. Make migrations and migrate

    ```
    python manage.py makemigrations
    
    python manage.py migrate
    ```
5. To see the sql commands ran for migration use following command:

    ```
    python manage.py sqlmigrate [app-name] [migration-number]
    
    ```
6. Create entry in database

    ```
    from [app].models import [model]
    post = [model](field1='value',field2='value')
    post.save()
    ```
    
    or using existing model
    ```
    from [app].models import [model]
    from django.contrib.auth.models import User
    user = User.objects.get(id=1)
    user.[model]_set.create(field1='value',field2='value')
    
    # no save required because 'create' will also save
    ```