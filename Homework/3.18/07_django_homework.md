# 07_django_homework

### 1. 

```
STATICFILES_DIRS = [BASE_DIR/'project_name'/'assets']
```



### 2. 

```
MEDIA_ROOT = BASE_DIR / '프로젝트이름'/ 'uploaded_files'
MEDIA_URL = '/uploaded_files/' (꼭 media url은 일치 안해도됨)
```



### 3.

```
(a) settings
(b) django.conf.urls.static
(c) static
(d) settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
```



