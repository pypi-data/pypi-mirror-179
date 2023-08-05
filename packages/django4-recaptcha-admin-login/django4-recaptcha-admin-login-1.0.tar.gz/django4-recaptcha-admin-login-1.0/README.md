# Django4_reCAPTCHA_admin_login_page
Will add an reCAPTCHA field to Django Admin Login Page to provide a more secure page

========================================================================

Steps to fast deployment:

1. Sign up for reCAPTCHA [Google reCAPTCHA](https://www.google.com/recaptcha/about/).

2. Install using: pip3 install django4-recaptcha-admin-login

3. Add 'django4_recaptcha_admin_login' and 'captcha' to your INSTALLED_APPS in settings.py

```

INSTALLED_APPS = [
    ...,
    'django4_recaptcha_admin_login',
    'captcha',
    ...
]

```

4. Add the Google reCAPTCHA keys generated in step 1 to your Django production settings with RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY.

Example: in settings.py:

```
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
```

And in env.py:

```
os.environ.setdefault('RECAPTCHA_PUBLIC_KEY',
                      'your public key')
os.environ.setdefault('RECAPTCHA_PRIVATE_KEY',
                      'your private key')
```

5. Edit project urls.py file and change the import of admin:

From:

```
from django.contrib import admin
```
To:

```
from django4_recaptcha_admin_login import admin
```

This is all.

This package is depending on django-recaptcha 3.0.0 package.
For extended informations and suport for django-recaptcha please see:
https://pypi.org/project/django-recaptcha/

This package was tested on Django==4.1.2 and Python 3.10.8
