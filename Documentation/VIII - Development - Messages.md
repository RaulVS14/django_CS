# Development - Messages

1. Import messages modules

    ```
    from django.contrib import messages
    ```  
2. Selection of messages to use
    ```
    # messages.debug
    # messages.info
    # messages.success
    # messages.warning
    # messages.error
    ```
3. Example of sending message
   ```
   messages.success(request, f'Account created for {username}')
   ```
4. Example of handling message in template
    ```
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        {% endif %}
    ```