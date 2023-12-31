# Bookmarks

This is a simple django project that allows users to create account and also share images.

## PS

- Locate `/etc/hosts`(linux) or `C:\Windows\System32\Drivers\etc\hosts`(windows). Edit This file to include:

```
127.0.0.1 mysite.com
```

This is to allow your pc to redirect to localhost when you enter `https://mysite.com:8000` in your browser.

- Edit `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY` and `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET` values with your own values. You can
  follow this [article](https://python-social-auth.readthedocs.io/en/latest/backends/google.html#google-oauth2) to
  know how to get these values.

## Running the application

You can use the default `python manage.py runserver` to run the project or `python manage.py runserver_plus --cert-file cert.crt` to run the project using https.

## What was learnt

- Authentication.
- Password change and reset.
- Social Authentication(Google).
- Downloading Images.
- Like and Unlike images.
- Infinite Scroll.
- Follow and Unfollow.
- Activity System.

## Preview

![Activities Page](preview/activities.png)
![Favicon](preview/favicon.png)
![Login Page](preview/login_page.png)
![Sign Up Page](preview/sign_up_page.png)
![Password Change Page](preview/password_change.png)
![Password Reset Page](preview/password_reset.png)
![Peoples Page](preview/peoples_page.png)

## Libraries used

- [pillow](https://pypi.org/project/Pillow/) - for image processing.
- [social-auth-app-django](https://github.com/python-social-auth/social-app-django) - for social authentication.
- [django-extensions](https://github.com/django-extensions/django-extensions) - this extension also includes the installation of:
  - [werkzeug](https://pypi.org/project/Werkzeug/) - which is required by RunServerPlus extension of Django extensions.
  - [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) - which is required to use SSL/TLS functionality of RunServerPlus.
- [requests](https://requests.readthedocs.io/en/latest/) - for downloading image by its URL.
- [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) - for generating thumbnails of images. -[js-cookie](https://github.com/js-cookie/js-cookie) - javascript script API for handling cookies.
- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - to see relevant debug information about the current request/response cycle.
- [redis](https://redis-py.readthedocs.io/en/stable/) - for storing the image views count.
