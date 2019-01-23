# Development - Forms

1. Use existing User Creation form

    1. Import the form from django auth forms
        ```
        from django.contrib.auth.forms import UserCreationForm
        ```
    2. Inside view
    
        ```
        form = UserCreationForm()
        ```
    3. Check if the form is valid
        ```
        form.is_valid()
        ```
    4. To pass the POST request data into the form
        ```
        form = UserCreationForm(request.POST)
        ```
    5. Save form data to model
        ```
        form.save()
        ```
2. Create your own form
    1. Create the file named **forms.py** in your app folder
    
    2. Import necessary modules
        ```
        from django import forms
        from django.contrib.auth.models import User # model to use in your form
        from django.contrib.auth.forms import UserCreationForm # class extended
        ```
    
    2. Create form class (other form classes can be extended)
        ```
        
        class UserRegisterForm(UserCreationForm):
        ```
    3. Define fields
        ```
        email = forms.EmailField()
        ```
    4. Create Meta class for the Form class - this will handle data
        ```
        class Meta:
            model = User # model to save form data to
            fields = ['username', 'email', 'password1', 'password2'] # fields to display
        ```