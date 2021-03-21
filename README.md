# odoohub-django

## viewflow
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/viewflow-login.jpg)
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/viewflow-index.jpg)

## PyJWT
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/pyjwt.jpg)

## channels
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/channels.jpg)
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/channels-fronted.jpg)

## restframework
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/restframework.jpg)

## Avatar
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/avatar.jpg)

##  django-simple-history
[官方文档](https://django-simple-history.readthedocs.io/en/latest/index.html)

get_change_reason_from_object:
```python
def get_change_reason_from_object(obj):
    if hasattr(obj, "_change_reason"):
        return getattr(obj, "_change_reason")

    if hasattr(obj, "changeReason"):
        warning_msg = (
            "Using the attr changeReason to populate history_change_reason is"
            " deprecated in 2.10.0 and will be removed in 3.0.0. Use "
            "_change_reason instead. "
        )
        warnings.warn(warning_msg, DeprecationWarning)
        return getattr(obj, "changeReason")

    return None
```

_change_reason：
```python
from django.db import models
from simple_history.models import HistoricalRecords


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self._change_reason = 'this is save (UPDATE)'
        super().save(*args, **kwargs)
```

![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/history-db.jpg)

## Django AdminLTE2 👍

[官方文档](https://django-adminlte2.readthedocs.io/en/latest/index.html)
```python
pip install django-adminlte2
```
```python
INSTALLED_APPS = [
    # Any apps which will override adminlte's templates (i.e. your apps)
    ...

    # The general purpose templates
    'django_adminlte',

    # Optional: Skin for the admin interface
    'django_adminlte_theme',

    # Any apps which need to have their templates overridden by adminlte
    'django.contrib.admin',
    ...
]
```
```html
{% extends 'adminlte/base.html' %}

{% block title %}{{ site }}{% endblock %}
{% block content %}
    Just some example content - {{ site }}
    <div>{{ docs }}</div>
{% endblock %}
```
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/adminlte.png)

## Django AdminLTE3
[官方文档](https://pypi.org/project/django-adminlte-3/)
```python
pip install django-adminlte3
```
```python
INSTALLED_APPS = [
     # General use templates & template tags (should appear first)
    'adminlte3',
     # Optional: Django admin theme (must be before django.contrib.admin)
    'adminlte3_theme',
    ...
]
```
```html
// 同AdminLTE2的用法
{% extends 'adminlte/base.html' %}

{% block title %}{{ site }}{% endblock %}
{% block content %}
    Just some example content - {{ site }}
    <div>{{ docs }}</div>
{% endblock %}
```
![Image text](https://github.com/huakkai/odoohub-django/blob/master/git-img/adminlte3.png)
