=====
Django Site Extend
=====

Django-Site is a Django app to extend django sites framework.


Quick start
-----------

1. Add "django_site" to your INSTALLED_APPS setting like this (you'll need the Sites app enabled)::

    INSTALLED_APPS = [
        ...
        "django.contrib.sites",
        "django_site",
    ]

2. Run ``python manage.py migrate`` to create the Site Config models.

3. Visit http://127.0.0.1:8000/admin/sites/site/ to participate in the Site.
