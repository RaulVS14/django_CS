# Development - Signals

Signals are used to trigger certain actions when signals are triggered

1. Create **signals.py** file in your app folder

2. Import the necessary modules
    ```
    from django.db.models.signals import post_save # post_save event
    from django.dispatch import receiver # receiver of signal
    from [models] import [model]
    from [models2] import [model2]
    ```
    
3. Create signal methods

    Set reciever decorator to accept 
    ```
    @receiver(post_save, sender=[model])
    def create_[model2](sender, instance, created, **kwargs):
        if created:
            [model2].objects.create([model2_connecting_field]=instance)
    
    ```
    Set receiver decorator to accept post_save signal and model
    ```
    @receiver(post_save, sender=[model])
    def save_model2(sender, instance, **kwargs):
        instance.[model2].save()
    ```
    
4. Connect signals to **app.py**

    ```
    def ready(self):
        import [app].signals
    ```