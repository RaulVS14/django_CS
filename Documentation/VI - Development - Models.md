# Development - Models

1. For this you can use **models.py** in your app folder

2. Create a class

    ```
    from django.db import models
    
    class [your-class-name](models.Model):
        [... Add your class fields ...]
    ```
3. You can use imported models module to define field values
    ```
    models.CharField() - characters field, short text field
    models.TextField() - long form text
    models.ImageField() - field for image takes default value of a filename
    models.models.OneToOneField() - appoints the field Models are connected on
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
    
7. Setting relation type constriction for model
    ```
    models.OneToOneField(User, on_delete=models.CASCADE)
    ```

8. Change models objects display name by adding __str__ function

    ```
        def __str__(self):
            return "Model " + [some-descriptive-value]
    ```
    
9. Register models for admin page:
    1. Import Model to app's **admin.py**
        ```
        from [app].models import [Model]
        ```
    2. Register model
        ```
        admin.site.register([Model])
    
        ```
## Class based Views
1. Template path
    ```
    # <app>/<model>_<viewtype>.html
    ```
2. Instead of decorators, mixins are used
    1. Import mixins
        ```
        from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
        ```
    2. Extend view class with mixin class
        ```
        class PostCreateView(LoginRequiredMixin, CreateView):
        ```