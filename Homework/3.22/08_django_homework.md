# 08_django_homework

### 1.

```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
```



### 2.

```
from django.contrib.auth.forms import UserCreationForm
```



### 3. 

```
from django.views.decorators.http import require_POST
```

